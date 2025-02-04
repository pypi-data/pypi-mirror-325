from configparser import ConfigParser
from urllib.parse import urlparse

from vdl_tools.scrape_enrich.scraper.scrape_websites import BAD_URL_PATH_CHARS
from vdl_tools.shared_tools.prompt_management.prompt_manager import PromptManager
from vdl_tools.shared_tools.openai.prompt_response_cache import GeneralPromptResponseCache
from vdl_tools.shared_tools.tools.unique_ids import make_uuid


S3_DEFAULT_BUCKET_NAME = 'vdl-website-summary-cache'
S3_DEFAULT_BUCKET_REGION = 'us-east-1'
DEFAULT_FILE_CACHE_DIRECTORY = '.cache/website-summary'

WEB_SUMMARIZER_NAMESPACE_NAME = "WEB_SUMMARIZER"


GENERIC_ORG_WEBSITE_PROMPT_TEXT = """
You are an analyst researching organizations in order to write a summary of their work. Your data science team has scraped the websites of the organizations and it is your job to summarize the text to give a good description the organization.

The text is scraped from websites, so please ignore junk or repetitive text.
Please do not mention anything regarding donations or how to fund the organization.
Please take your time and ensure the information is accurate and well written.
Please do not include any references to the website or suggest visiting the website for more information.
Please only include the summary and nothing but the summary.
Please only return a single summary.
Please do not include copyright, legal text, or other citations such as address.

You will receive a set of webpage urls and the web text for a single organization. Each set will be delineated by a line break and <code>---</code> characters.

{INPUT TEXT}
{SUMMARY}
"""


class WebsiteSummarizationCache(GeneralPromptResponseCache):
    _cached_keys = []
    _local_cache_keys = []

    def __init__(
        self,
        prompt_str: str = GENERIC_ORG_WEBSITE_PROMPT_TEXT,
        prompt_name: str = "",
        aws_region: str = S3_DEFAULT_BUCKET_REGION,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
        file_cache_directory: str = DEFAULT_FILE_CACHE_DIRECTORY,
        prompt_manager: PromptManager = None,
        config: ConfigParser = None,
    ):

        # If None or "" is passed in
        prompt_str = prompt_str or GENERIC_ORG_WEBSITE_PROMPT_TEXT
        prompt_name = prompt_name or "generic_org_website"
        super().__init__(
            prompt_str=prompt_str,
            prompt_name=prompt_name,
            namespace_name=WEB_SUMMARIZER_NAMESPACE_NAME,
            bucket_name=S3_DEFAULT_BUCKET_NAME,
            aws_region=aws_region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            file_cache_directory=file_cache_directory,
            prompt_manager=prompt_manager,
            config=config,
        )

    def create_search_key(self, id: str) -> str:
        parsed_url = urlparse(id)
        netloc = parsed_url.netloc

        if not netloc:
            if 'http' not in id:
                url = f'http://{id}'
                parsed_url = urlparse(url)

            else:
                raise ValueError(f"Invalid source url {id}")

        netloc = parsed_url.netloc
        if netloc.startswith("www."):
            netloc = netloc[len("www."):]

        website_key = netloc

        parsed_url_args = ["path", "params", "query", "fragment"]
        for arg in parsed_url_args:
            arg_val = getattr(parsed_url, arg, "")
            # Replace all bad characters with an underscore
            if arg_val and arg_val != '/':
                replaced_values = arg_val.translate({ord(char): '_' for char in BAD_URL_PATH_CHARS})
                replaced_values = replaced_values.strip("_")
                website_key+=f"_{replaced_values}"

        return f"{self.prompt.id}/{website_key}"
