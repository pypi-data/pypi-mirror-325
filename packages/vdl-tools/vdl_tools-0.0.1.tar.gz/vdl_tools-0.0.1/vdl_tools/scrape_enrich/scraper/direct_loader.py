from bs4 import BeautifulSoup
import requests

from vdl_tools.shared_tools.tools.logger import logger


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}


def load_website_psql(url: str, filter_no_body=True):
    try:
        if not url.startswith('http'):
            url = f'https://{url}'
        res = requests.get(
            url,
            headers=HEADERS,
            timeout=60,
        )
    except requests.RequestException as re:
        logger.warning('Caught exception for %s', url)
        logger.error(re)
        return None, 400

    if res.status_code >= 400:
        logger.warning('Received status %s for %s', res.status_code, url)
        return None, res.status_code

    if filter_no_body:
        html = BeautifulSoup(res.text, 'lxml')
        body = html.find('body')

        if not body:
            logger.warning('Received empty page for %s', url)
            return None, res.status_code

        if not body.text.strip():
            logger.warning('Received empty page content for %s', url)
            return None, res.status_code

    if res.headers.get('content-type', '').startswith('application/pdf'):
        return res.content, res.status_code
    return res.text, res.status_code


def load_website(url: str):
    try:
        if not url.startswith('http'):
            url = f'https://{url}'
        res = requests.get(url, headers=HEADERS)
    except requests.RequestException as re:
        logger.warn(f'Caught exception for {url}')
        logger.error(re)
        return None

    if res.status_code >= 400:
        logger.warn(f'Received status {res.status_code} for {url}')
        return None

    html = BeautifulSoup(res.text, 'lxml')
    body = html.find('body')

    if not body:
        logger.warn(f'Received empty page for {url}')
        return None

    if not body.text.strip():
        logger.warn(f'Received empty page content for {url}')
        return None

    return res.text
