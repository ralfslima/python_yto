# Importar Pandas
import pandas as pd

# Dados
dados = {
    "nome":["Smartphone Galaxy S24", "TV 45 polegadas", "Tablet Galaxy FE", None, "Smartphone Galaxy S24"],             
    "marca":["Samsung", "LG", "Samsung", "HP", "Samsung"],
    "valor":[4500, 2800, 3750, 700, 4500]
}

# DataFrame
df = pd.DataFrame(dados)

# Exibir toda a estrutura do DataFrame
#print(df.to_string())

# Exibir colunas específicas
#print(df["nome"].to_string())
#print(df[["nome", "valor"]].to_string())

# Somar todos os valores
#print("A soma dos valores é {}".format(df["valor"].sum()))

# Média de todos os valores
#print("A média dos valores é {}".format(df["valor"].mean()))

# Exibir o maior valor
#print("O maior valor é {}".format(df["valor"].max()))

# Exibir o menor valor
#print("O menor valor é {}".format(df["valor"].min()))

# Contar valores
#print("A quantidade de valores é {}".format(df["valor"].count()))

# Retornar a quantidade de informações em uma coluna sem duplicadas
#print(df["marca"].unique())

# Condicional (IF)
#print(df[df["valor"] >= 4000])

# Criar nova coluna
#quantidade = [75, 34, 22]
#df["quantidade"] = quantidade

# Exibir nova estrutura
#print(df.to_string())

# Remover coluna
#df = df.drop(columns=["quantidade"])

# Exibir nova estrutura
#print(df.to_string())

# Ordenação de dados
#print(df.sort_values(by=["marca"]))
#print(df.sort_values(by=["marca"], ascending=False))
#print(df.sort_values(by=["marca", "nome"], ascending=[False, False]))

# Agrupamento
#print(df.groupby(["marca"])["marca"].count())

# Selecionar dados iniciais
#print(df.head()) # Listar as 5 primeiras linhas
#print(df.head(1)) # Listar apenas a primeira linha

# Selecionar dados finais
#print(df.tail()) # Listar as 5 últimas linhas
#print(df.tail(1)) # Listar a última linha

# Verificar quais informações são nulas
#print(df.isnull())

# Atribuir valor em campos/células nulas
#df = df.fillna("Produto desconhecido")
#print(df)

# Remover linhas, onde existam informações nulas
#print(df.dropna())

# Remover linhas duplicadas
print(df.drop_duplicates())