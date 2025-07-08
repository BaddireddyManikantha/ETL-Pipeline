from etl.config import load_config
from etl.logger import get_logger
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def main():
    config = load_config()
    logger = get_logger("ETL_Pipeline", config['logging']['file'], config['logging']['level'])
    logger.info("ETL pipeline started.")

    try:
        # Extract
        df = extract_data(config['api']['url'], logger)
        # Transform
        transformed_df = transform_data(df, logger)
        # Load
        load_data(transformed_df, config['snowflake'], logger)
        logger.info("ETL pipeline completed successfully.")
    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")
        raise

if __name__ == "__main__":
    main()
