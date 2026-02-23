def calcular_total(df):
    return df["Valor"].sum()
def calcular_media(df):
    return df["Valor"].mean()
def calcular_por_categoria(df):
    return df.groupby("Categoria")["Valor"].sum()