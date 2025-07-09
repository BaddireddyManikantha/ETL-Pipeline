import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl.extract import extract_data
from etl.logger import get_logger

def test_extract_data():
    logger = get_logger("test_extract_data", "test_etl.log")  # added log_file argument

    df = extract_data("https://jsonplaceholder.typicode.com/users", logger)

    assert not df.empty
    assert "id" in df.columns
