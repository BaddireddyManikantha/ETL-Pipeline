import pandas as pd

def transform_data(df: pd.DataFrame, logger) -> pd.DataFrame:
    """Perform simple data cleaning."""
    logger.info("Starting data transformation.")
    try:
        df = df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"))
        if 'id' in df.columns:
            df = df.dropna(subset=['id'])
        logger.info("Transformation completed.")
        return df
    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        raise
