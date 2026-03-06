import pandas as pd
from src.preprocess import preprocess_telco
from src.data_loader import load_csv


def test_preprocess_runs():
    df = pd.DataFrame({
        "TotalCharges": ["100", "200", "300"],
        "SeniorCitizen": [0, 1, 0]
    })

    processed = preprocess_telco(df)

    assert processed is not None
    assert "TotalCharges" in processed.columns


def test_loader_exists():
    assert callable(load_csv)
