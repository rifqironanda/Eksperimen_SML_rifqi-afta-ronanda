import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from preprocessing.automate_rifqi import preprocess_data


def test_preprocess_not_empty():

    df = preprocess_data(
        "dataset_raw/WA_Fn-UseC_-Telco-Customer-Churn.csv",
        "preprocessing/dataset_preprocessing/temp.csv"
    )

    assert len(df) > 0