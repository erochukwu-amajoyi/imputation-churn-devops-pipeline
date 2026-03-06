import pandas as pd
import numpy as np


def impute_median_mode(df: pd.DataFrame, num_cols, cat_cols) -> pd.DataFrame:
    """
    Median for numerical columns and mode for categorical columns.
    """
    d = df.copy()

    for col in num_cols:
        d[col] = d[col].fillna(d[col].median())

    for col in cat_cols:
        d[col] = d[col].fillna(d[col].mode()[0])

    return d


def missing_summary(df: pd.DataFrame) -> dict:
    """
    Return missing-value summary.
    """
    return df.isna().sum().to_dict()
