import os
from multiprocessing.pool import ThreadPool
import threading

import pandas as pd
from more_itertools import chunked

from vdl_tools.shared_tools.openai.openai_api_utils import num_tokens_from_messages, get_num_tokens, contains_i_am
from vdl_tools.shared_tools.openai.openai_constants import MODEL_DATA
from vdl_tools.shared_tools.tools.logger import logger
from vdl_tools.shared_tools.tools.text_cleaning import clean_scraped_text, check_for_repeating_sequences
from vdl_tools.shared_tools.web_summarization.page_choice.choose_pages import filter_pages, ScrapedPageRecord
from vdl_tools.shared_tools.web_summarization.page_choice.constants import PATHS_TO_KEEP
from vdl_tools.shared_tools.web_summarization.website_summarization_cache_psql import (
    WebsiteSummarizationCache,
    GENERIC_ORG_WEBSITE_PROMPT_TEXT,
)


# Minimum number of tokens that need to be available for the summary
MIN_SUMMARY_LENGTH = 100
# Maximum number of tokens that can be used for the summary
MAX_SUMMARY_LENGTH = 500
MODEL = "gpt-4o-mini"


def _make_full_url(record: ScrapedPageRecord):
    """Utitility function that concatenates the source and subpath of a page record to make the full url."""
    return os.path.join(record['source'].strip('/'), record['subpath'].strip('/'))


def make_group_text(
    prompt_str: str,
    record_group: pd.DataFrame | list[ScrapedPageRecord],
    model: str = "gpt-4o-mini"
):
    """Makes the text for a group of page records for a given organization.
    This will be concatenated to the prompt_str text.

    Parameters
    ----------
    prompt_str: str
        The prompt (as a string) that will be used.

    record_group : list[ScrapedPageRecord]
        The list of page records for a single organization

    model : str, optional
        The OpenAI GPT model to be used for scoring, by default "gpt-4o-mini"
        This is used to get the token count for the messages to ensure we don't
        exceed the max context window.

    Returns
    -------
    str
        The text for the group of page records
    """
    if isinstance(record_group, pd.DataFrame):
        record_group = record_group.to_dict(orient="records")
    messages = [
        {"role": "system", "content": prompt_str},
        {"role": "user", "content": ""},
    ]

    model_name = MODEL_DATA[model]["model_name"]
    # The number of tokens in the prompt without any text yet added
    current_message_tokens = num_tokens_from_messages(messages, model_name)
    # The number of tokens available for the prompt
    num_tokens_available = MODEL_DATA[model]["max_context_window"] - \
        current_message_tokens - MIN_SUMMARY_LENGTH

    JOIN_CHARS = "\n----\n"

    url_texts = []
    num_tokens_used = 0
    num_too_long = 0

    for record in record_group:
        full_url = _make_full_url(record)
        if len(record['text']) < 50:
            logger.warning(
                "Skipping short text %s, only %s characters",
                full_url, len(record['text']),
            )
            continue

        record_text_w_url = f"URL: {full_url}\nTEXT: {record['text']}"

        num_tokens_in_record_w_url = get_num_tokens(
            JOIN_CHARS + record_text_w_url,
            model_name
        )

        if num_tokens_in_record_w_url + num_tokens_used < num_tokens_available:
            repeats_sequence, _ = check_for_repeating_sequences(record_text_w_url, (2, 3), 0.10)
            if repeats_sequence:
                logger.warning(
                    "Skipping text %s, repeating sequences",
                    full_url,
                )
                continue
            url_texts.append(record_text_w_url)
            num_tokens_used += num_tokens_in_record_w_url
        else:
            logger.warning(
                "Skipping text %s, too long (%s tokens)",
                full_url, num_tokens_in_record_w_url,
            )

    if not url_texts:
        logger.warning("No text for record url %s", record_group[0]['source'])
        if num_too_long == len(record_group):
            logger.warning("All records too long, using first record truncated")
            first_record = record_group[0]
            full_url = _make_full_url(first_record)
            record_text_w_url = f"URL: {full_url}\nTEXT: {first_record['text'][:5000]}"
            url_texts.append(record_text_w_url)
        else:
            return None

    return "\n----\n".join(url_texts)


def summarize_website(
    website_url: str,
    website_pages: pd.DataFrame | list[ScrapedPageRecord],
    prompt_str: str = None,
    website_summarization_cache: WebsiteSummarizationCache = None,
    filtering_keep_paths: tuple[str] = tuple(set(PATHS_TO_KEEP)),
    session=None,
    skip_existing=True,
):
    """Summarizes a scraped website from our website scraper. It assumes the website has been scraped and is formatted
    like our website scraper for a single url (`source` in the scraping output).

    This means it should be either a data frame with the columns:
        `type`
        `source`
        `subpath`
        `text`
    Also allows for a list of ScrapedPageRecord objects, which would be dictionaries with the same keys.

    This will first look in the cache for the hash of the prompt text if the exact text has been used in the past for this same url.

    Parameters
    ----------
    website_url : str
        The home url of the website that was scraped
    website_pages : pd.DataFrame | list[ScrapedPageRecord]
        The pages for a given website.
    configuration : configparser.ConfigParser
        Configuration object
    website_summarization_cache: WebsiteSummarizationCache, optional
        The WebsiteSummarizationCache object. This is used for caching and retrieving the websites
    filtering_keep_paths: set, optional
        The set of paths to keep when summarizing a website, by default PATHS_TO_KEEP, which is our
        opinionated set of paths.
    return_all: bool = False

    Returns
    -------
    str
        The summary of the website.
    """

    logger.info("Summarizing website %s", website_url)
    prompt_str = prompt_str or GENERIC_ORG_WEBSITE_PROMPT_TEXT
    if not website_summarization_cache:
        website_summarization_cache = WebsiteSummarizationCache(
            session=session,
            prompt_str=prompt_str,
        )

    filtered_pages = filter_pages(website_pages, keep_paths=filtering_keep_paths)
    filtered_pages["text"] = filtered_pages["text"].apply(clean_scraped_text)

    if isinstance(filtered_pages, pd.DataFrame):
        filtered_pages = filtered_pages.to_dict(orient="records")

    grouped_text = make_group_text(
        record_group=filtered_pages,
        prompt_str=website_summarization_cache.prompt.prompt_str,
    )
    if not grouped_text:
        logger.warning("No text for record url %s", website_url)
        return None

    messages = [
        {"role": "system", "content": website_summarization_cache.prompt.prompt_str},
        {"role": "user", "content": grouped_text},
    ]

    num_tokens_used = num_tokens_from_messages(
        messages,
        MODEL_DATA[MODEL]["model_name"]
    )

    num_available_context_window = MODEL_DATA[MODEL]["max_context_window"] - num_tokens_used
    # The maximum number of tokens that can be used for the summary
    # Take the minimum of the available context window and the max summary length
    max_tokens = min(num_available_context_window, MAX_SUMMARY_LENGTH)

    summary = website_summarization_cache.get_cache_or_run(
        given_id=website_url,
        text=grouped_text,
        use_cached_result=skip_existing,
        max_tokens=max_tokens,
        model=MODEL,
        temperature=0.2,
        stop="Summary:"
    )['response_text']
    return summary


def get_previous_summaries(
    given_ids,
    website_summarization_cache: WebsiteSummarizationCache = None,
    session=None,
):
    if not website_summarization_cache:
        website_summarization_cache = WebsiteSummarizationCache(
            session=session,
        )

    found_rows, _ = website_summarization_cache.get_prompt_response_obj_bulk(
        given_ids=given_ids
    )
    return {k: v for k, v in found_rows.items() if not contains_i_am(v)}

def summarize_scraped_df(
    scraped_df: pd.DataFrame,
    filtering_keep_paths: tuple[str] = tuple(set(PATHS_TO_KEEP)),
    website_summarization_cache: WebsiteSummarizationCache = None,
    session=None,
    skip_existing: bool =True,
    n_per_commit: int = 50,
    max_workers: int = 5,
) -> dict:
    """Runs website summarization on a dataframe that went through VDL's website_scraping code.

    Parameters
    ----------
    scraped_df : pd.DataFrame
        Dataframe formatted as that returned from `scrape_enrich.scraper.scrape_websites`
    prompt : str
        Prompt to use for the summarization
    website_summary_cache : WebsiteSummarizationCache
        Standard VDL configuration with the keys needed for summarization

    Returns
    -------
    dict
       Source url to summarization
    """

    if not website_summarization_cache:
        website_summarization_cache = WebsiteSummarizationCache(
            session=session,
        )

    filtered_pages_df = filter_pages(scraped_df, keep_paths=filtering_keep_paths)
    source_grouper = filtered_pages_df.groupby("source")

    given_ids = source_grouper.groups.keys()
    found_rows, _ = website_summarization_cache.get_prompt_response_obj_bulk(
        given_ids=given_ids
    )
    if skip_existing:
        found_rows = {
            x.given_id: x.response_text
            if not isinstance(x, dict)
            else x['response_text']
            for x in found_rows
        }
    else:
        found_rows = {}

    summaries = found_rows

    def _summarize_website(source_group_tuple):
        source, group = source_group_tuple
        data = found_rows.get(source)
        if not data:
            try:
                data = summarize_website(
                    website_url=source,
                    website_pages=group,
                    website_summarization_cache=website_summarization_cache,
                    filtering_keep_paths=filtering_keep_paths,
                    skip_existing=False,
                )
            except Exception as e:
                logger.error("Error summarizing %s: %s", source, e)
                data = ""
        if data and contains_i_am(data):
            logger.info("LLM Apologized for %s", source)
            data = ""
        return data

    for chunk in chunked(source_grouper, n_per_commit):
        sources, _ = zip(*chunk)
        try:
            with ThreadPool(processes=max_workers) as executor:
                results = list(executor.map(_summarize_website, chunk))
            for source, response in zip(sources, results):
                summaries[source] = response
            session.commit()
        except KeyboardInterrupt:
            logger.warn("Received KeyboardInterrupt, returning the currently scraped data...")
            break
    return summaries
