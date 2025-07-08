import snowflake.connector

def load_data(df, sf_config, logger):
    """Load DataFrame into Snowflake table."""
    logger.info("Starting data load into Snowflake.")
    try:
        conn = snowflake.connector.connect(
            user=sf_config['user'],
            password=sf_config['password'],
            account=sf_config['account'],
            warehouse=sf_config['warehouse'],
            database=sf_config['database'],
            schema=sf_config['schema']
        )
        cursor = conn.cursor()
        # Create table if it doesn't exist
        logger.info(f"Creating table {sf_config['table']} if it does not exist.")
        create_stmt = f"""
        CREATE TABLE IF NOT EXISTS {sf_config['table']} (
            id INT,
            name STRING,
            username STRING,
            email STRING
        )
        """
        cursor.execute(create_stmt)

        # Insert data
        for _, row in df.iterrows():
            insert_stmt = f"""
            INSERT INTO {sf_config['table']} (id, name, username, email)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_stmt, tuple(row[['id', 'name', 'username', 'email']]))
        conn.commit()
        logger.info(f"Loaded {len(df)} rows into Snowflake table {sf_config['table']}.")
    except Exception as e:
        logger.error(f"Loading failed: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
        logger.info("Snowflake connection closed.")
