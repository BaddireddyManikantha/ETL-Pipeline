from etl.extract import extract_data

def test_extract_data():
    df = extract_data("https://jsonplaceholder.typicode.com/users")
    assert not df.empty
    assert "id" in df.columns
