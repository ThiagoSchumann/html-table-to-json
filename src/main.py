# src/main.py

import sys
import os
from services.file_handler import read_file, write_file
from services.html_parser import parse_html
from services.json_converter import table_to_json
from utils.logger import logger

def convert_html_table_to_json(html_file):
    try:
        html_content = read_file(html_file)
        table = parse_html(html_content)
        if table:
            json_data = table_to_json(table)
            return json_data
        else:
            logger.warning('No table found to convert to JSON.')
            return None
    except Exception as e:
        logger.error(f'Error in convert_html_table_to_json function: {e}')
        raise

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    html_file = sys.argv[1]
    try:
        json_data = convert_html_table_to_json(html_file)
        if json_data:
            output_file = os.path.join('output', 'out.json')
            write_file(output_file, json_data)
            logger.info(f"JSON saved to {output_file}")
            print(f"JSON saved to {output_file}")
        else:
            logger.warning('No JSON data to save.')
            print('No JSON data to save.')
    except Exception as e:
        logger.error(f"Error processing file: {e}")
        print(f"Error processing file: {e}")
