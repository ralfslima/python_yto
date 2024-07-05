# Importar o Pandas
import pandas as pd

# Importar o MatPlotLib
import matplotlib.pyplot as plt

# Ler arquivo CSV
df = pd.read_csv('02.csv')

#1º Contar o número de produtos 
print('1ª Questão:')
print('A quantidade de produtos é: {}'.format(df['Produto'].count()))
print()

#2º Qual é o produto mais caro? (Dica, pesquise pela função idxmax()) 
print('2ª Questão:')
print(df.loc[(df['Valor'].idxmax())])
print()

#3º Qual é a marca com mais produtos listados? 
nome_marca = df["Marca"].value_counts().idxmax() # idxmax -> Retorna o nome
qtd_marca = df["Marca"].value_counts().max()     # max -> Retorna a qtd
print('3ª Questão:')
print('{} tem o maior números de produtos com: {}'.format(nome_marca, qtd_marca))
print()

#4º Quais são os produtos que custam mais de R$ 5000,00? 
print('4ª Questão:')
lista_produtos = df[df['Valor'] > 5000]
print(lista_produtos.to_string())
print()

#5º Qual é a média de preços dos produtos? 
print('5ª Questão:')
print('A média dos preços é: {:.2f}'.format(df['Valor'].mean()))
print()

#6º Quantos produtos cada marca possui? 
print('6ª Questão:')
print(df['Marca'].value_counts().to_string())
print()

#7º Quais são os produtos da marca Sony? 
print('7ª Questão:')
lista_sonys = df[df['Marca'] == 'Sony']
print(lista_sonys.to_string())
print()

#8º Quais são os produtos que contêm a palavra 'Smart' no nome? 
print('8ª Questão:')
lista_smarts = df[df['Produto'].str.contains('Smart')]
print(lista_smarts.to_string())
print()

#9º Quais são os produtos com valor entre R$ 1000,00 e R$ 2000,00? Dica: &
print('9ª Questão:')
lista_produtos_valores = df[(df['Valor'] >= 1000) & (df['Valor'] <= 2000)]
print(lista_produtos_valores.to_string())
print()

#10º Qual é o valor máximo de um produto? Dica: max
print('10ª Questão:')
print(df['Valor'].max())
print()

#11º Quais são os produtos que têm a palavra 'Câmera' no nome? 
print('11ª Questão:')
lista_cameras = df[df['Produto'].str.contains('Câmera')]
print(lista_cameras.to_string())
print()

#12º Qual é o produto mais barato? 
print('12ª Questão:')
print(df.loc[df['Valor'].idxmin()])
print()

#13º Quais são os produtos que começam com a letra 'C'? str.startsWith
print('13ª Questão:')
produtos_iniciam_c = df[df['Produto'].str.startswith('C')]
print(produtos_iniciam_c.to_string())
print()

#14º Qual é a marca com o produto mais caro listado? 
print('14ª Questão:')
print(df.loc[df['Valor'].idxmax(), 'Marca'])
print()

#15º Quais são os produtos que têm um preço exato de R$ 300,00?
print('15ª Questão:')
produtos_valor_300 = df[df['Valor'] == 300]
print(produtos_valor_300.to_string())
print() 

#16º Crie um gráfico, exibindo a quantidade de produtos por marca 
print(df["Marca"].value_counts().to_string())

#17º Crie um gráfico exibindo a quantidade de produtos de até R$1.000,00, entre R$1.000,01 a R$3.000,00 e acima de R$3.000,00
contagem_marca = df['Marca'].value_counts()

nomes_marca = contagem_marca.index
quantidades_produtos = contagem_marca.values

plt.figure(figsize=(12, 8))
plt.barh(nomes_marca, quantidades_produtos, color='skyblue')
plt.xlabel('Quantidade de Produtos')
plt.ylabel('Marca')
plt.title('Quantidade de Produtos por Marca')
plt.gca().invert_yaxis()  # Inverte a ordem das marcas para melhor visualização
plt.tight_layout()
plt.show()

#18º Crie um gráfico exibindo a quantidade de produtos de até R$1.000,00, entre R$1.000,01 a R$3.000,00 e acima de R$3.000,00
faixas_valor = ['Até R$ 1000', 'R$ 1001 a R$ 3000', 'Acima de R$ 3000']

def categoriza_valor(valor):
    if valor <= 1000:
        return faixas_valor[0]
    elif valor <= 3000:
        return faixas_valor[1]
    else:
        return faixas_valor[2]
    
df['Faixa de Valor'] = df['Valor'].apply(categoriza_valor)

contagem_valor = df['Faixa de Valor'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(contagem_valor, labels=contagem_valor.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Produtos por Faixa de Valor')
plt.axis('equal')

plt.show()