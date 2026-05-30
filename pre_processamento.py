import pandas as pd

print("1. Abrindo o cofre: Carregando a base completa... 📂")
# Quando o extrator terminar, ele vai cuspir esse arquivo. 
# Se der erro de leitura, testa com sep=","
df = pd.read_csv("base_treino_mvp_v1.csv", sep=";")

print("Tamanho original da base:", df.shape)

print("\n2. Começando a feitiçaria do One-Hot Encoding... 🪄")

# A Classificação Etária é um valor único por filme (ex: "14", "Livre").
# Pra ela, o get_dummies padrão resolve lindamente.
df = pd.get_dummies(df, columns=['CLASSIFICACAO'], dummy_na=False, dtype=int)

# As colunas casca-grossa: têm vários nomes separados por vírgula.
colunas_texto = ['GENEROS', 'ATORES_PRINCIPAIS', 'DIRETORES', 'PRODUTORAS']

for coluna in colunas_texto:
    # A malandragem: .str.get_dummies() quebra os textos pela vírgula e espaço
    print(f"Binarizando a coluna: {coluna}...")
    dummies = df[coluna].str.get_dummies(sep=', ')
    
    # Bota o nome da coluna original na frente pra não dar confusão 
    # (ex: vai virar 'GENEROS_Ação', 'ATORES_PRINCIPAIS_Tom Cruise')
    dummies = dummies.add_prefix(f'{coluna}_')
    
    # Gruda essas novas colunas de 0 e 1 no nosso DataFrame original
    df = pd.concat([df, dummies], axis=1)

print("\n3. Passando a vassoura final... 🧹")
# O algoritmo não entende texto, então a gente deleta as colunas originais 
# que a gente acabou de transformar.
df = df.drop(columns=colunas_texto)

# Opcional: Se tiver algum filme com campo vazio (NaN) em PÚBLICO, a gente tira pra não quebrar a conta
df = df.dropna(subset=['PUBLICO'])

# Convertendo o ano de lançamento para número (tirando de texto caso tenha vindo como string)
df['ANO_LANCAMENTO'] = pd.to_numeric(df['ANO_LANCAMENTO'], errors='coerce')
df = df.dropna(subset=['ANO_LANCAMENTO']) # Se algum filme ficou sem data, a gente corta

print("\nTamanho da base depois do One-Hot Encoding:", df.shape)
print("Transformação concluída, mermão! Base 100% mec pra entrar na arena!")

# Salvando a base blindada pronta pro Machine Learning
df.to_csv("base_ml_pronta.csv", index=False, sep=";")
print("Arquivo 'base_ml_pronta.csv' salvo com sucesso! 🏆")