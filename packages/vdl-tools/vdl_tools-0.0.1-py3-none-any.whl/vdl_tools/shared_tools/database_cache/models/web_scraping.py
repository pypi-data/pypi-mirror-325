from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy_utils import generic_repr

from vdl_tools.shared_tools.database_cache.models.base import BaseMixin

@generic_repr
class WebPagesScraped(BaseMixin):
    """Table to hold scraped webpages"""
    __tablename__ = 'web_pages_scraped'

    cleaned_key = Column(String, nullable=False, primary_key=True)
    full_path = Column(String, index=True)
    home_url = Column(String, nullable=False, index=True)
    subpath = Column(String, nullable=False)
    raw_html = Column(String, nullable=True)
    parsed_html = Column(String, nullable=True)
    page_type = Column(String, nullable=False)
    response_status_code = Column(Integer, nullable=True)
    num_errors = Column(Integer, nullable=True)
