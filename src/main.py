from pathlib import Path
from leitura import carregar_dados
from tratamento import tratar_dados
from analise import calcular_total, calcular_por_categoria, calcular_media
from relatorio import gerar_relatorio

base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / "data" / "dados.xlsx"
output_path = base_dir / "output" / "relatorios.xlsx"

def main():
    print ("Iniciando automação...")

    df = carregar_dados(data_path)
    if df is None:
        return

    df = tratar_dados(df)

    total = calcular_total(df)
    media = calcular_media(df)
    resumo_categoria = calcular_por_categoria(df)

    print (f"Total gasto: R${total:.2f}")
    print (f"Media gasto: R${media:.2f}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    gerar_relatorio(df, resumo_categoria, output_path)

    print ("Relatorio gerado com sucesso")

if __name__ == "__main__":
    main()