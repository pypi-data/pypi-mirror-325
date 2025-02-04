
import logging

import vdl_tools.scrape_enrich.scraper.page_scraper as ps
import vdl_tools.shared_tools.tools.log_utils as log


logging.getLogger("webdriver_manager").setLevel(logging.WARNING)

def get_organization(id: str):
    url = f'https://www.linkedin.com/company/{id}'
    scraper = ps.page_scraper()
    page_source = ps.scrape_website(url, scraper)
    if not page_source:
        log.warn(f"Failed to scrape organization {id}")
        return None

    if ('authwall' in scraper.current_url) or ('/login' in scraper.current_url):
        log.warn(f"Failed to send GET request for organization {id}. Redirected to {scraper.current_url}")
        return None
    
    if '<body' not in page_source:
        log.warn(f"Failed to send GET request for organization {id}. No body in response")
        return None
    
    if 'core-section-container__content' not in page_source:
        log.warn(f"Failed to send GET request for organization {id}. No core-section-container in response")
        return None
    
    return page_source

def get_profile(id: str):
    url = f'https://www.linkedin.com/in/{id}/'
    scraper = ps.page_scraper()
    page_source = ps.scrape_website(url, scraper)
    if not page_source:
        log.warn(f"Failed to scrape profile {id}")

    if ('authwall' in scraper.current_url) or ('/login' in scraper.current_url):
        log.warn(f"Failed to send GET request for profile {id}. Redirected to {scraper.current_url}")
        return None
    
    if '<body' not in page_source:
        log.warn(f"Failed to send GET request for profile {id}. No body in response")
        return None
    
    if 'core-section-container__content' not in page_source:
        log.warn(f"Failed to send GET request for profile {id}. No core-section-container in response")
        return None
    
    if 'could not be found' in page_source.lower():
        log.warn(f"Failed to send GET request for profile {id}. Data is not found")
        return None       
    
    return page_source
