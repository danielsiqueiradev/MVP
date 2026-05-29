import pandas as pd

print("1. Abrindo a base bruta da Ancine... 📚")
arquivo_bruto = "historico_ancine_mestre_2014_2026.csv"

try:
    df_bruto = pd.read_csv(arquivo_bruto, sep=";")
except:
    df_bruto = pd.read_csv(arquivo_bruto, sep=",")

print("2. Passando o rodo na base... 🧹")
# A régua tá nos 10.000 ingressos
df_limpo = df_bruto[df_bruto['PUBLICO'] >= 10000].copy()

# Salvando a base limpa pra usar depois
df_limpo.to_csv("ancine_filtrada.csv", index=False, sep=";", encoding='utf-8-sig')

print(f"✅ Tudo nosso! De {len(df_bruto)} filmes, sobraram {len(df_limpo)} casca-grossa.")
print("Arquivo 'ancine_filtrada.csv' gerado no esquema! 🏆")