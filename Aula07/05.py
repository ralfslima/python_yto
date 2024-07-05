'''
Importe o arquivo 05.sql

1º Quantos funcionários têm menos de 30 anos?
2º Qual é a média de salário dos funcionários por departamento?
3º Quais são os três funcionários mais velhos?
4º Quantos funcionários são da cidade de Salvador?
5º Qual é a idade média dos funcionários que trabalham no departamento de Vendas?
6º Qual é o funcionário mais novo?
7º Quantos funcionários têm salário superior a 5000?
8º Qual é o salário máximo e mínimo na empresa?
9º Quantos funcionários trabalham em cada cidade?
10º Qual é o departamento com a maior média de idade dos funcionários?
11º Gráfico de barras mostrando a quantidade de funcionários por departamento
12º Gráfico de pizza mostrando a distribuição de funcionários por cidade
'''
# Importar pandas
import pandas as pd

# Importar Matllotlib
import matplotlib.pyplot as plt

# Dataframe
df = pd.read_sql("02.sql")

# Contando funcionários com menos de 30 anos
funcionarios_menos_30 = df[df['idade'] < 30]
resposta = len(funcionarios_menos_30)
print(f"Funcionários com menos de 30 anos: {resposta}")

# Qual é a média de salário dos funcionários por departamento?
media_salario_por_departamento = df.groupby('departamento')['salario'].mean()
print(media_salario_por_departamento)

# Quais são os três funcionários mais velhos?
funcionarios_mais_velhos = df.nlargest(3, 'idade')
print(funcionarios_mais_velhos['nome'])

# Quantos funcionários são da cidade de Salvador?
funcionarios_salvador = df[df['cidade'] == 'Salvador']
resposta = len(funcionarios_salvador)
print(f"Funcionários de Salvador: {resposta}")

# Qual é a idade média dos funcionários que trabalham no departamento de Vendas?
idade_media_vendas = df[df['departamento'] == 'Vendas']['idade'].mean()
print(f"Idade média dos funcionários de Vendas: {idade_media_vendas:.2f}")

# Qual é o funcionário mais novo?
funcionario_mais_novo = df.nsmallest(1, 'idade')
print(funcionario_mais_novo['nome'])

# Quantos funcionários têm salário superior a 5000?
funcionarios_salario_alto = df[df['salario'] > 5000]
resposta = len(funcionarios_salario_alto)
print(f"Funcionários com salário superior a 5000: {resposta}")

# Qual é o salário máximo e mínimo na empresa?
salario_maximo = df['salario'].max()
salario_minimo = df['salario'].min()
print(f"Salário máximo: {salario_maximo}")
print(f"Salário mínimo: {salario_minimo}")

# Quantos funcionários trabalham em cada cidade?
media_idade_por_departamento = df.groupby('departamento')['idade'].mean()
departamento_maior_media_idade = media_idade_por_departamento.idxmax()
print(f"Departamento com maior média de idade: {departamento_maior_media_idade}")

# Gráfico de barras mostrando a quantidade de funcionários por departamento
# Contagem de funcionários por departamento
contagem_departamento = df['departamento'].value_counts()

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
contagem_departamento.plot(kind='bar')
plt.title('Quantidade de Funcionários por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Quantidade de Funcionários')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
         
# Gráfico de pizza mostrando a distribuição de funcionários por cidade
# Contagem de funcionários por cidade
contagem_cidade = df['cidade'].value_counts()

# Plotando o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(contagem_cidade, labels=contagem_cidade.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Funcionários por Cidade')
plt.axis('equal')
plt.tight_layout()
plt.show()

