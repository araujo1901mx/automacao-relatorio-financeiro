import pandas as pd

def gerar_relatorio(df, resumo_categoria, caminho_saida):
    with pd.ExcelWriter(caminho_saida) as writer:
        df.to_excel(writer, sheet_name="Dados Originais", index=False)
        resumo_categoria.to_excel(writer, sheet_name="Resumo por Categoria")