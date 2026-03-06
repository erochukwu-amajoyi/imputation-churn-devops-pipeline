import pandas as pd


def preprocess_telco(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic preprocessing for the Telco churn dataset.
    """
    df = df.copy()

    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    if "SeniorCitizen" in df.columns:
        df["SeniorCitizen"] = df["SeniorCitizen"].map({0: "No", 1: "Yes"})

    return df


def get_feature_types(df: pd.DataFrame):
    """
    Split columns into numeric and categorical, excluding ID and target.
    """
    exclude = ["customerID", "Churn"]

    num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

    num_cols = [c for c in num_cols if c not in exclude]
    cat_cols = [c for c in cat_cols if c not in exclude]

    return num_cols, cat_cols
