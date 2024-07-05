# Importar pandas
import pandas as pd

# Importar matplotlib
import matplotlib.pyplot as plt

# 1º Crie um DataFrame para ler o arquivo CSV.
df = pd.read_csv("01.csv")

# 2º Exibir toda a estrutura do DataFrame
print(df.to_string())

# 3º Exiba apenas o nome e a cidade (não exibir o índice)
print(df[["Nome", "Cidade"]].to_string(index=False))

# 4º Informe a média das idades
print("A média das idades é {}".format(df["Idade"].mean()))

# 5º Exiba a quantidade de registros
print("A quantidade de registros é {}".format(df["Nome"].count()))

# 6º Exiba apenas os dados das pessoas que moram em São Paulo
print(df[df["Cidade"] == "São Paulo"])

# 7º Exiba apenas os dados das pessoas que moram em São Paulo com idade superior a 30 anos
print(df[(df["Cidade"] == "São Paulo") & (df["Idade"] > 30)])

# 8 Exiba apenas os dados das pessoas que moram em Florianópolis ou Rio de Janeiro
print(df[(df["Cidade"] == "Florianópolis") | (df["Cidade"] == "Rio de Janeiro")])

# 9º Ordenar os dados através da idade (da menor para a maior)
print(df.sort_values(by=["Idade"]).to_string())

# 10º Liste os 5 últimos registros
print(df.tail())

# 11º Liste as cidades sem repetição
print(df["Cidade"].unique())

# 12º Exiba o nome das cidade e a quantidade que se repetem
print(df.groupby(["Cidade"])["Cidade"].count())

# 13º Exiba os dados, onde a pessoa tenha entre 27 e 32 anos e ordene da menor idade para a maior
filtro = (df["Idade"] >= 27) & (df["Idade"] <= 32)
print(df[filtro].sort_values(by=["Idade"]).to_string())

# 14º Exiba um gráfico que mostre a quantidade de pessoas em cada cidade
#cidades = df["Cidade"].unique()
cidades = df.groupby(["Cidade"])["Cidade"].count().index
quantidade = df.groupby(["Cidade"])["Cidade"].count().values

plt.pie(quantidade, labels=cidades, autopct="%1.1f%%")

plt.show()

# 15º Exiba um gráfico que mostre a quantidade de pessoas por idade
idade = df.groupby(["Idade"])["Idade"].count().index
quantidade = df.groupby(["Idade"])["Idade"].count().values

plt.bar(idade, quantidade)

plt.show()