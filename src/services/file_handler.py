# src/services/file_handler.py

import os
from utils.logger import logger
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            logger.info(f'File {file_path} read successfully.')
            return content
    except Exception as e:
        logger.error(f'Error reading file {file_path}: {e}')
        raise
def write_file(file_path, content):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            logger.info(f'File {file_path} written successfully.')
    except Exception as e:
        logger.error(f'Error writing file {file_path}: {e}')
        raise
