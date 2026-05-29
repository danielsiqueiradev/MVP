import requests
from datetime import datetime
import pandas as pd

api_key = "d586bba83710b6aa29d7c6776bcc3335"
hoje = datetime.now().strftime('%Y-%m-%d')
ano_alvo = 2026
data_fim = f"{ano_alvo}-12-31"

print("Preparando o terreno pro Megazord 2.0... 🛠️")

filmes_do_ano = []
pagina_atual = 1
total_paginas = 1 

print(f"Buscando a tropa de {hoje} até o fim do ano... 🍿\n")

while pagina_atual <= total_paginas:
    # 1. Busca a listagem básica da página
    url_discover = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&region=BR&release_date.gte={hoje}&release_date.lte={data_fim}&with_release_type=2|3&sort_by=release_date.asc&page={pagina_atual}"
    response_discover = requests.get(url_discover)
    
    if response_discover.status_code == 200:
        dados = response_discover.json()
        if pagina_atual == 1:
            total_paginas = dados['total_pages']
            print(f"Alvo: {dados['total_results']} filmes. Ativando o modo turbo (append_to_response)! 🚀")
        
        for filme_basico in dados['results']:
            id_filme = filme_basico['id']
            
            # --- O PULO DO GATO: DETALHES + CRÉDITOS NUMA CAJADADA SÓ ---
            url_detalhes = f"https://api.themoviedb.org/3/movie/{id_filme}?api_key={api_key}&language=pt-BR&append_to_response=credits"
            resp_detalhes = requests.get(url_detalhes).json()
            
            # Pegando os Gêneros (agora já vem com nome certinho da API)
            generos_lista = [g['name'] for g in resp_detalhes.get('genres', [])]
            texto_generos = ", ".join(generos_lista)
            
            # Pegando Produtoras (Warner, Universal, etc)
            produtoras_lista = [p['name'] for p in resp_detalhes.get('production_companies', [])]
            texto_produtoras = ", ".join(produtoras_lista)
            
            # Elenco e Diretor vêm na mesma sacola agora (credits)
            creditos = resp_detalhes.get('credits', {})
            elenco = creditos.get('cast', [])
            atores_principais = [ator['name'] for ator in elenco[:3]]
            texto_elenco = ", ".join(atores_principais)
            
            equipe = creditos.get('crew', [])
            diretor = "Desconhecido"
            for membro in equipe:
                if membro['job'] == 'Director':
                    diretor = membro['name']
                    break
            
            # Jogando tudo na nossa sacola final
            filmes_do_ano.append({
                "ID": id_filme,
                "Titulo": resp_detalhes.get('title'),
                "Data_Estreia": resp_detalhes.get('release_date', 'Sem data'),
                "Generos": texto_generos,
                "Produtoras": texto_produtoras,
                "Diretor": diretor,
                "Elenco_Principal": texto_elenco,
                "Popularidade_TMDB": resp_detalhes.get('popularity'),
                "Sinopse": resp_detalhes.get('overview')
            })
        
        print(f"Página {pagina_atual}/{total_paginas} dominada!")
        pagina_atual += 1
    else:
        print(f"O segurança barrou na página {pagina_atual}. Código {response_discover.status_code}")
        break

# Exportando a verdadeira mina de ouro
df_filmes = pd.DataFrame(filmes_do_ano)
df_filmes.to_csv("lancamentos_kinoplex_master.csv", index=False, sep=";", encoding='utf-8-sig')

print("\n✅ TUDO NOSSO, PAIZÃO! Tabela 'lancamentos_kinoplex_master.csv' salva com sucesso!")