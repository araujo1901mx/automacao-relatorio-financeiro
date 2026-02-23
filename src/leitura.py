import pandas as pd

def carregar_dados(caminho):
    try:
        df = pd.read_excel(caminho, engine="openpyxl")
        return df
    except FileNotFoundError:
        print ("Arquivo não encontrado")
        return None