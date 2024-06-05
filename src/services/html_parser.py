# src/services/html_parser.py

from bs4 import BeautifulSoup
from utils.logger import logger
def parse_html(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table')
        if table:
            logger.info('HTML table parsed successfully.')
            return table
        else:
            logger.warning('No table found in HTML content.')
            return None
    except Exception as e:
        logger.error(f'Error parsing HTML content: {e}')
        raise
