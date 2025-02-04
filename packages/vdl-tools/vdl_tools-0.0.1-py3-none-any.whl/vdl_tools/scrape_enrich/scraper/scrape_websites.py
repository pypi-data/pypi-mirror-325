from concurrent.futures import ThreadPoolExecutor as ThreadPool
import threading

from enum import Enum
from more_itertools import chunked
import pandas as pd
from urllib.parse import urljoin, urlparse

import vdl_tools.scrape_enrich.scraper.direct_loader as dl
import vdl_tools.scrape_enrich.scraper.page_scraper as ps
from vdl_tools.scrape_enrich.scraper.website_cache import WebsiteCache
import vdl_tools.scrape_enrich.scraper.website_processor as wp
from vdl_tools.shared_tools.tools.logger import logger as log
from vdl_tools.shared_tools.database_cache.models.web_scraping import WebPagesScraped
from vdl_tools.shared_tools.tools.text_cleaning import clean_scraped_text


thread_local = threading.local()


def __get_driver():
    Driver = getattr(thread_local, 'driver', None)
    if Driver is None:
        Driver = ps.page_scraper()
        Driver.set_page_load_timeout(25)
        setattr(thread_local, 'driver', Driver)

    return Driver

class PageType(Enum):
    INDEX = "index",
    PAGE = "page"

MAX_ERRORS = 5


# if the page from one of these websites is to be scraped
# then the scraper should only take the first page
SINGLE_PAGE_WEBSITES = [
    'medium.com',
    'facebook.com',
    'linkedin.com',
    'linktr.ee',
    'about.me',
    'wikipedia.org',
    'github.com',
    'scholar.google.com/',
    'meetup.com',
]


BAD_URL_PATH_CHARS = '/?=&#@'

__selenium_instance = None


def check_is_single_page_websites(url: str, single_page_websites: list = []):
    return len([x for x in [*SINGLE_PAGE_WEBSITES, *single_page_websites] if x in url.lower()]) > 0


def __clean_website_path(value: str) -> str:
    '''
    Clean the website subpath

    /pages/contact -> pages_contact
    /pages/contact/ -> pages_contact
    /about-us -> about-us
    /page?page_title=about-us -> page_page_title_about-us
    '''
    if 'www' in value:
        log.warn("Invalid value because path contains 'www': {value}")
        return None
    try:
        path = value.split(
            '/', maxsplit=1)[1] if value.startswith('/') else value
        path = path[:-1] if path.endswith('/') else path

        for c in BAD_URL_PATH_CHARS:
            path = path.replace(c, '_')

        return path
    except Exception as ex:
        log.warn(f'Error cleaning website path: {value}')
        return None


def extract_website_name(value: str) -> str:
    '''
    Clean the website name

    https://google.com -> google.com
    https://google.com/ -> google.com
    https://somewebsite.com:port -> somewebsite.com_port
    https://coolwebsite.com/inner/page/1 -> coolwebsite.com_inner_page_1
    https://anotherwebsite.com?query=my-query -> anotherwebsite.com
    '''
    try:
        if "//" in value:
            website = value.split('//')[1].strip()
        else:
            website = value
        website = website.split('?')[0].strip()
        # remove trailing slash
        website = website[:-1] if website.endswith('/') else website
        return website.replace('/', '_').replace(':', '_')
    except Exception as ex:
        log.warning(f'Error getting website name: {value}')
        return None


def process_website_text(url, data, add_section_links=False):
    return wp.get_page_text(url, data, add_section_links=add_section_links)


def get_netloc(url):
    if not url:
        return
    netloc = urlparse(url).netloc
    if 'www.' in netloc:
        netloc = netloc.replace('www.', '')
    return netloc


def load_website_psql(url, scraper, filter_no_body=True):
    data, status_code = dl.load_website_psql(
        url,
        filter_no_body=filter_no_body,
    )

    if data:
        return scraper, data, status_code

    data = ps.scrape_website(url, scraper)
    if data:
        status_code = 200

    return scraper, data, status_code


def load_website(url, scraper):
    data = dl.load_website(url)

    if data:
        return scraper, data

    if not data:
        if scraper is None:
            scraper = ps.page_scraper()

        data = ps.scrape_website(url, scraper)

    return scraper, data


def __get_page_data_psql(
    url: str,
    cache_id: str,
    data_type: PageType = PageType.INDEX,
    clean_path: str = None,
    root_path: str = None,
    subpage_type: str = 'all',
    single_page_websites: list = [],
    clean_text=True,
    max_per_subpath: int = 6,
    scraper=None,
    return_raw_html: bool = False,
    filter_no_body: bool=True,
    add_section_links=False,
):
    res = []
    root_url = url if not root_path else root_path
    subpath = '/' if data_type == PageType.INDEX else clean_path

    scraper, web_content, status_code = load_website_psql(
        url,
        scraper=scraper,
        filter_no_body=filter_no_body,
    )

    log.info("Getting page data for %s", url)
    if web_content:
        website_text = process_website_text(
            url,
            web_content,
            add_section_links=add_section_links,
        )
        res.append({
            "cleaned_key": cache_id,
            "full_path": url,
            "home_url": root_url,
            "subpath": subpath,
            "raw_html": web_content,
            "parsed_html": website_text,
            "response_status_code": status_code,
            "num_errors": 0,
            "page_type": str(data_type),
            "raw_html": web_content if return_raw_html else "",
        })

        is_single_page = check_is_single_page_websites(url, single_page_websites)

        if data_type == PageType.INDEX and not is_single_page:
            res.extend(process_internal_pages_psql(
                url,
                web_content,
                subpage_type,
                max_per_subpath,
                scraper=scraper,
                return_raw_html=return_raw_html,
                filter_no_body=filter_no_body,
                add_section_links=add_section_links,
            ))
        elif is_single_page:
            log.debug(f'{url} is marked as single page website, proceeding without scraping the internal pages')
    else:
        log.warn(f"Failed to receive data for {url}, marking it as error")
        res.append({
            "cleaned_key": cache_id,
            "full_path": url,
            "home_url": root_url,
            "subpath": subpath,
            "raw_html": "",
            "parsed_html": "",
            "response_status_code": status_code,
            "num_errors": 1,
            "page_type": str(data_type)
        })

    if clean_text:
        for row in res:
            row['parsed_html'] = clean_scraped_text(row['parsed_html'])
            row['parsed_html'] = row['parsed_html'].replace("\x00", "\uFFFD")
            # Have to replace NULL text for SQL to work
            if isinstance(row['raw_html'], bytes):
                row['raw_html'] = "PDF file"
            row['raw_html'] = row['raw_html'].replace("\x00", "\uFFFD")

    return res


def process_internal_pages_psql(
    url: str,
    website_content: str,
    subpage_type:str,
    max_per_subpath:int = 6,
    scraper=None,
    return_raw_html: bool = False,
    filter_no_body: bool=True,
    add_section_links=False,
):
    links = wp.extract_website_links(url, website_content, subpage_type, max_per_subpath)
    res = []
    for link in links:
        website_id = extract_website_name(url)
        log.debug(f'({website_id}) Processing {link}')
        clean_path = __clean_website_path(link)
        if not clean_path:
            continue
        full_path = f'{website_id}/{clean_path}'
        page_data = __get_page_data_psql(
            url=urljoin(url, link),
            cache_id=full_path,
            data_type=PageType.PAGE,
            clean_path=link,
            root_path=url,
            scraper=scraper,
            return_raw_html=return_raw_html,
            filter_no_body=filter_no_body,
            add_section_links=add_section_links,
        )
        res.extend(page_data)

    return res


def scrape_websites_psql(
    urls: list,
    session,
    skip_existing: bool = True,
    subpage_type='all',
    single_page_websites: list = [],
    n_per_commit: int = 10,
    max_errors: int = MAX_ERRORS,
    max_workers: int = 5,
    return_raw_html: bool = False,
    filter_no_body: bool = True,
    add_section_links: bool = False,
) -> pd.DataFrame:
    '''
    `urls`: `pandas.Series` of strings, containing the URLs to be scraped
    `skip_existing`: `bool`, if False then tries to rescrape the websites marked as error
    `configuration`: `dict`, dictionary with configuration values - AWS access, cache path
    if `None`, then tries to get the values from `config.ini` in the project working directory
    `subpage_type`: `str`, defaults to `"all"`, defines the strategy to select the
    subpages:
    - `all` - scrapes everything
    - `about` - heuristically determines only the about pages
    '''
    urls_ids = [(url, extract_website_name(url)) for url in urls]


    log.info("Starting to pull previous home pages from the database...")
    previous_rows = (
        session
        .query(
            WebPagesScraped.num_errors,
            WebPagesScraped.cleaned_key,
            WebPagesScraped.page_type,
            WebPagesScraped.home_url,
        )
        .filter(
            WebPagesScraped.cleaned_key.in_([x[1] for x in urls_ids]),
            WebPagesScraped.page_type == str(PageType.INDEX)
        )
        .all()
    )
    found_keys_to_errors = {x.cleaned_key: x.num_errors for x in previous_rows}

    if skip_existing:
        log.info("Starting to pull previous home pages from the database...")
        previous_rows = (
            session
            .query(
                WebPagesScraped.num_errors,
                WebPagesScraped.cleaned_key,
                WebPagesScraped.page_type,
                WebPagesScraped.home_url,
            )
            .filter(
                WebPagesScraped.cleaned_key.in_([x[1] for x in urls_ids]),
                WebPagesScraped.page_type == str(PageType.INDEX)
            )
            .all()
        )
        found_keys_to_errors = {x.cleaned_key: x.num_errors for x in previous_rows}

        unfound_rows = [
            x for x in urls_ids
            if x[1] not in found_keys_to_errors or 1 <= found_keys_to_errors[x[1]] < max_errors
        ]

        previous_home_urls = [x.home_url for x in previous_rows if x.num_errors == 0]
        log.info("Starting to pull previous data from the database...")
        columns = [
            WebPagesScraped.num_errors,
            WebPagesScraped.page_type,
            WebPagesScraped.home_url,
            WebPagesScraped.subpath,
            WebPagesScraped.parsed_html,
            WebPagesScraped.response_status_code,
        ]
        if return_raw_html:
            columns.append(WebPagesScraped.raw_html)
        found_rows = (
            session
            .query(*columns)
            .filter(
                WebPagesScraped.home_url.in_(previous_home_urls),
            )
        )
        res = [
            {
                "num_errors": x.num_errors,
                "page_type": x.page_type,
                "home_url": x.home_url,
                "subpath": x.subpath,
                "parsed_html": x.parsed_html,
                "response_status_code": x.response_status_code,
                "raw_html": x.raw_html if return_raw_html else "",
            }
            for x in found_rows
        ]
        log.info("Finished pulling previous data from the database...")
    else:
        unfound_rows = urls_ids
        res = []

    def __get_page_data_psql_parallel(
        url_website_id,
    ):
        url, website_id = url_website_id
        scraper = __get_driver()
        try:
            response = __get_page_data_psql(
                url,
                website_id,
                data_type=PageType.INDEX,
                subpage_type=subpage_type,
                single_page_websites=single_page_websites,
                scraper=scraper,
                return_raw_html=return_raw_html,
                filter_no_body=filter_no_body,
                add_section_links=add_section_links,
            )
            return response
        except Exception as ex:
            log.warning(f'Error processing website: {url} {ex}')
            return []

    if unfound_rows:
        log.info("Starting to scrape %s websites...", len(unfound_rows))
        with ThreadPool(max_workers=max_workers) as executor:
            for chunk in chunked(unfound_rows, n_per_commit):
                try:
                    results = list(executor.map(__get_page_data_psql_parallel, chunk))
                    flat_results = [page for pagelist in results if pagelist  for page in pagelist]
                    for row in flat_results:
                        if row['num_errors']:
                            row['num_errors'] += found_keys_to_errors.get(row['cleaned_key'], 0)
                        webpage_obj = WebPagesScraped(**row)
                        session.merge(webpage_obj)
                        res.append(webpage_obj.to_dict())
                    session.commit()
                except KeyboardInterrupt:
                    log.warn("Received KeyboardInterrupt, returning the currently scraped data...")
                    break

    final_res = _format_scraped_sites(res)
    return final_res


def __get_page_data(
    url: str,
    cache_id: str,
    cache: WebsiteCache,
    skip_existing: bool,
    data_type: PageType = PageType.INDEX,
    clean_path: str = None,
    root_path: str = None,
    subpage_type: str = 'all',
    single_page_websites: list = [],
    max_per_subpath: int = 6,
):
    global __selenium_instance
    res = []
    root_url = url if not root_path else root_path
    subpath = '/' if data_type == PageType.INDEX else clean_path
    data = cache.get_cache_item(cache_id)

    if skip_existing and not data and cache.is_error(cache_id):
        log.warn(
            f"Item '{cache_id}' is marked as website with error, skipping")
        return res

    if not data:
        __selenium_instance, data = load_website(
            url, scraper=__selenium_instance)

    if data:
        cache.store_item(cache_id, data)
        website_text = process_website_text(url, data)
        res.append({'type': data_type, 'source': root_url,
                   'subpath': subpath, 'text': website_text})

        is_single_page = check_is_single_page_websites(url, single_page_websites)

        if data_type == PageType.INDEX and not is_single_page:
            res.extend(process_internal_pages(url, data, skip_existing, cache, subpage_type, max_per_subpath))
        elif is_single_page:
            log.debug(f'{url} is marked as single page website, proceeding without scraping the internal pages')
    else:
        log.warn(f"Failed to receive data for {url}, marking it as error")
        cache.save_as_error(cache_id)

    return res


def process_internal_pages(
    url: str,
    website_content: str,
    skip_existing: bool,
    cache: WebsiteCache,
    subpage_type:str,
    max_per_subpath: int = 6,
):
    links = wp.extract_website_links(url, website_content, subpage_type, max_per_subpath=max_per_subpath)
    res = []
    for link in links:
        website_id = extract_website_name(url)
        log.warn(f'({website_id}) Processing {link}')
        clean_path = __clean_website_path(link)
        if not clean_path:
            continue
        full_path = f'{website_id}/{clean_path}'
        page_data = __get_page_data(urljoin(
            url, link), full_path, cache, skip_existing, PageType.PAGE, clean_path=link, root_path=url)
        res.extend(page_data)

    return res


def scrape_websites(urls: pd.Series,
                    skip_existing: bool = True,
                    configuration: dict = None,
                    subpage_type='all',
                    single_page_websites: list = []) -> pd.DataFrame:
    '''
    `urls`: `pandas.Series` of strings, containing the URLs to be scraped
    `skip_existing`: `bool`, if False then tries to rescrape the websites marked as error
    `configuration`: `dict`, dictionary with configuration values - AWS access, cache path
    if `None`, then tries to get the values from `config.ini` in the project working directory
    `subpage_type`: `str`, defaults to `"all"`, defines the strategy to select the
    subpages:
    - `all` - scrapes everything
    - `about` - heuristically determines only the about pages
    '''
    cache = WebsiteCache(config=configuration)
    res = []
    total = len(urls)
    idx = 0

    for _, value in urls.items():
        idx = idx + 1
        website_id = extract_website_name(value)
        if not website_id:
            continue
        log.warn(f'({idx} / {total}) Processing {value}')
        index_key = f'{website_id}/index'
        try:
            res.extend(__get_page_data(value, index_key, cache, skip_existing, subpage_type=subpage_type, single_page_websites=single_page_websites))
        except KeyboardInterrupt:
            log.warn("Received KeyboardInterrupt, returning the currently scraped data...")
            break
        except Exception as ex:
            log.warn(f'Error processing website {value}: {ex}')

    return pd.DataFrame(res)


if __name__ == '__main__':
    from vdl_tools.shared_tools.database_cache.database_utils import get_session
    urls = [
        'https://python.org',
        'https://google.com',
        'https://www.vibrantdatalabs.org',
    ]
    with get_session() as session:
        res_psql = scrape_websites_psql(urls, session)
        print(res_psql.head())
        session.commit()

    res = scrape_websites(pd.Series(urls))
    print(res.head())


def _format_scraped_sites(results):
    final_res = []
    for row in results:
        final_res.append({
            "type": row['page_type'],
            "source": row['home_url'],
            "subpath": row['subpath'],
            "text": row['parsed_html'],
            "response_status_code": row['response_status_code'],
            "raw_html": row.get('raw_html', ''),
        })
    return pd.DataFrame(final_res)
