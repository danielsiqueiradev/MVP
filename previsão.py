import pandas as pd #type: ignore
# Aqui em cima ficariam os teus imports do requests e tuas chaves de API...

print("Iniciando a varredura do Kinobot... 🤖🍿\n")

# ... (Todo aquele teu código batendo no TMDB, YT e OMDb entra aqui) ...

# 1. EM VEZ DE DAR PRINT, A GENTE GUARDA TUDO NUM DICIONÁRIO:
linha_do_filme = {
    "ID_TMDB": id_filme_tmdb,
    "Titulo": titulo_original,
    "Data_Estreia": data_lancamento,
    "Hype_Views_YT": views,
    "Hype_Likes_YT": likes,
    "Critica_IMDb": nota_imdb,
    "Critica_Rotten": nota_rotten
}

print("Dados coletados com sucesso! Gerando a tabela... 📊")

# 2. TRANSFORMANDO A CAIXA NUMA TABELA DO PANDAS (DataFrame)
tabela_hype = pd.DataFrame([linha_do_filme])

# 3. EXPORTANDO O ARQUIVO (A MÁGICA FINAL)
# Esse comando cria um arquivo CSV na mesma pasta do teu projeto
tabela_hype.to_csv("dados_previsao_bilheteria.csv", index=False, sep=";")

print("Tudo nosso! Arquivo 'dados_previsao_bilheteria.csv' salvo com sucesso! 🚀")