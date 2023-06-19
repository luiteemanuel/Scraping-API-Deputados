# Scraping-API-Deputados
projeto de web Scraping usando API publica da câmara dos Deputados. 

Projeto teve intuito de extrair dados da API do Governo Federal. 
essas APIs retornam dados, sobre despesas de cada deputados. 

# Primeiro desafio 
Por ser uma API publica os dados não tinham um padrão, foi feita então uma organização e Estruturação dos dados.. 
Após isso foi armazenado dados brutos em um Json. 

# Usando os Dados em cloud 
Usei o Big Query do GPC para armazenar esse Json, e uma tabela na Cloud. 
após isso utilizei o para fazer um ETL dos dados, e filtrar os dados de forma mais correta e assertiva. 

# Resultado
Ao finalizar a Pipeline extrair já melhorados para CSV.  
