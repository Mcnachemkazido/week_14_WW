import pandas as pd

def add_an_analysis_column(df):
    df["risk_level"] = pd.cut(x=df["range_km"], bins=[-float('inf'), 20, 100, 300, float('inf')],
    labels=["low", "medium", " high", "extreme"])
    return df

def replacing_missing_values(df):
    df["manufacturer"] = df["manufacturer"].fillna("Unknown")
    return df


