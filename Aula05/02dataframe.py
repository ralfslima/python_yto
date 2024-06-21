# Importar o Pandas
import pandas as pd

# Estrutura de dados
dados = {
    "nomes":["Ana", "Aline", "Paulo", "Ricardo"],
    "cidades":["São Paulo", "Campinas", "Niterói", "Belo Horizonte"]
}

# Criar um DataFrame
df = pd.DataFrame(dados)

# Exibir estrutura do DataFrame
#print(df) # Para poucas linhas
#print(df.to_string()) # Força a exibição de dados as linhas
print(df.to_string(index=False)) # Ocultar o índice (linhas)