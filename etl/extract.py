import pandas as pd
import requests

def extract_data(api_url: str, logger) -> pd.DataFrame:
    """Fetch data from API and return as DataFrame."""
    logger.info(f"Starting data extraction from {api_url}")
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        logger.info(f"Successfully extracted {len(df)} records.")
        return df
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise
