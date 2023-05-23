import requests
from bs4 import BeautifulSoup
import pandas as pd
from google.oauth2 import service_account
import io
import csv
import base64
#iniciando project Le'go


# Fazer a requisição à API e obter os dados dos deputados
url_deputados = "https://dadosabertos.camara.leg.br/api/v2/deputados"
response_deputados = requests.get(url_deputados)
data_deputados = response_deputados.json()

# Extrair os links para as APIs individuais de cada deputado
links_deputados = [deputado["uri"] for deputado in data_deputados["dados"]]

# Criar uma lista para armazenar os dados individuais de cada deputado
dados_individuais = []

# Percorrer os links dos deputados e obter os dados individuais
for link in links_deputados:
    response_individual = requests.get(link)
    data_individual = response_individual.json()
    dados_individuais.append(data_individual["dados"])

# Criar um DataFrame com os dados individuais dos deputados
df_deputados = pd.DataFrame(dados_individuais)

deputado_id = 220593

# Fazer a requisição à API e obter os gastos do deputado
url_despesas = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/despesas"
response_despesas = requests.get(url_despesas)
data_despesas = response_despesas.json()
data_despesas

# normalizando Json e criando DataFrame
cria_df = pd.json_normalize(data_despesas)
df_despesas_total = pd.DataFrame(cria_df)

#selecionei so os dados
df_despesas = df_despesas_total['dados']
dados = df_despesas.transpose()
print(dados)



