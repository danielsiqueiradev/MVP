import pandas as pd # type: ignore
import glob
import os

# Coloca o caminho certinho da tua pasta ANCINE2 aqui
caminho_pasta = r"C:\Users\Daniel Siqueira\Downloads\Bilheteria"

print("Infiltrando na pasta da Ancine... 👀")
# O glob vai listar todos os arquivos .csv que estão lá dentro
arquivos_csv = glob.glob(os.path.join(caminho_pasta, "*.csv"))

lista_dataframes = []

print(f"Achei {len(arquivos_csv)} arquivos! Começando o arrastão... 🚜\n")

for arquivo in arquivos_csv:
    try:
        # Lendo cada mês com a formatação padrão do governo
        df = pd.read_csv(arquivo, sep=';', encoding='utf-8')
        lista_dataframes.append(df)
        print(f"Sugado: {os.path.basename(arquivo)}")
    except Exception as e:
        print(f"Deu ruim no arquivo {os.path.basename(arquivo)}: {e}")

print("\nCosturando todos os meses num arquivo só... 🧵")
# Aqui a gente empilha tudo!
df_mestre = pd.concat(lista_dataframes, ignore_index=True)

print("Agrupando o público total do Brasil inteiro (2014 a 2026)... 📊")
# Soma o público de cada filme pra matar a charada
df_resumo = df_mestre.groupby('TITULO_ORIGINAL', as_index=False)['PUBLICO'].sum()
df_resumo = df_resumo.sort_values(by='PUBLICO', ascending=False)

# Salvando a obra de arte final
nome_arquivo_final = "historico_ancine_mestre_2014_2026.csv"
df_resumo.to_csv(nome_arquivo_final, index=False, sep=";", encoding='utf-8-sig')

print(f"\n✅ TUDO NOSSO, RAPA! Arquivo '{nome_arquivo_final}' gerado com sucesso!")
print("Os top 3 filmes da década:")
print(df_resumo.head(3).to_string(index=False))