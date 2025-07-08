import pandas as pd
from etl.transform import transform_data

def test_transform_data():
    df = pd.DataFrame({"ID": [1, 2], "Name": ["A", "B"]})
    clean_df = transform_data(df)
    assert "id" in clean_df.columns
