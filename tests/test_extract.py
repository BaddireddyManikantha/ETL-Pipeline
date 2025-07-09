
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from etl.extract import extract_data


def test_extract_data():
    df = extract_data("https://jsonplaceholder.typicode.com/users")
    assert not df.empty
    assert "id" in df.columns
