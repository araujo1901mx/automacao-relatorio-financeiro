import pandas as pd
def tratar_dados(df):
    df["Data"] = pd.to_datetime(df["Data"], dayfirst=True)
    df["Valor"] = pd.to_numeric(df["Valor"])
    return df