# src/services/json_converter.py

import pandas as pd
from utils.logger import logger
def table_to_json(table):
    try:
        df = pd.read_html(str(table))[0]
        df.dropna(how='all', inplace=True)
        df.dropna(axis=1, how='all', inplace=True)
        json_data = df.to_json(orient='records', force_ascii=False)
        logger.info('Table converted to JSON successfully.')
        return json_data
    except Exception as e:
        logger.error(f'Error converting table to JSON: {e}')
        raise
