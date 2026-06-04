# tests/test_preprocessing.py

from preprocessing.automate_rifqi import preprocess_data

def test_preprocess_not_empty():

    df = preprocess_data(
        "dataset_raw/telco.csv",
        "preprocessing/dataset_preprocessing/temp.csv"
    )

    assert len(df) > 0