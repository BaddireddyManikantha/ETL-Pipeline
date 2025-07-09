import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl.transform import transform_data
from etl.logger import get_logger
import pandas as pd

def test_transform_data():
    logger = get_logger("test_transform_data", "test_etl.log")

    df = pd.DataFrame({"ID": [1, 2], "Name": ["A", "B"]})
    clean_df = transform_data(df, logger)

    assert not clean_df.empty
    assert "id" in clean_df.columns
