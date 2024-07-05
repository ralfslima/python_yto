# Importar o Pandas
import pandas as pd

# Importar o MatPlotLib
import matplotlib.pyplot as plt

# Ler arquivo CSV
df = pd.read_csv('03.json')

#1º Calcular a média e criar uma nova coluna
df['media'] = (df['nota1'] + df['nota2']) / 2

#2º Função para definir a situação do aluno
def situacao_aluno(media):
    if media >= 7:
        return 'Aprovado(a)'
    else:
        return 'Reprovado(a)'

df['situacao'] = df['media'].apply(situacao_aluno)

#3º Contar os valores únicos na coluna 'situacao'
aprovados = df[df['situacao'] == 'Aprovado(a)'].shape[0]
reprovados = df[df['situacao'] == 'Reprovado(a)'].shape[0]

print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos reprovados: {reprovados}")

#4º Ordenar o DataFrame pela coluna 'media' em ordem decrescente
df_sorted = df.sort_values(by='media', ascending=False)[['nome', 'media']]

print(df_sorted)

#5º Filtrar os alunos com média entre 7 e 8
qtd_media_7_8 = df[(df['media'] >= 7) & (df['media'] < 8)].shape[0]

print(f"Quantidade de alunos com média entre 7 e 8: {qtd_media_7_8}")

#6º Calcular a média geral
media_geral = df['media'].mean()

print(f"Média geral dos alunos: {media_geral:.2f}")

#7º Filtrar os alunos com média maior ou igual à média geral
alunos_acima_media_geral = df[df['media'] >= media_geral][['nome', 'media']]

print(alunos_acima_media_geral)

#8º Contar os alunos com média 5 ou inferior
qtd_media_5_ou_inferior = df[df['media'] <= 5].shape[0]

print(f"Quantidade de alunos com média 5 ou inferior: {qtd_media_5_ou_inferior}")

#9º Criar uma nova coluna chamada 'faltas' e gerar de maneira aleatória um número de faltas entre 0 e 20:
import random

df['faltas'] = [random.randint(0, 20) for _ in range(len(df))]

#10º Atualizar a situação do aluno considerando a média e as faltas
def situacao_aluno_com_faltas(row):
    if row['media'] >= 7 and row['faltas'] <= 10:
        return 'Aprovado(a)'
    else:
        return 'Reprovado(a)'

df['situacao'] = df.apply(situacao_aluno_com_faltas, axis=1)

#11º Contar os alunos com média 7 ou superior e faltas até 10
qtd_aprovados_com_faltas = df[(df['media'] >= 7) & (df['faltas'] <= 10)].shape[0]

print(f"Quantidade de alunos aprovados com média 7 ou superior e faltas até 10: {qtd_aprovados_com_faltas}")

#12º Exportar o DataFrame para um arquivo JSON
df.to_json('alunos.json', orient='records', indent=4)

#13º Gere um gráfico exibindo a quantidade de alunos aprovados e reprovados
situacao_counts = df['situacao'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(situacao_counts, labels=situacao_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Proporção de Alunos Aprovados e Reprovados')
plt.axis('equal')
plt.show()

#14º Gere um gráfico exibindo quantos alunos faltaram até 10 vezes e quantos tem mais de 10 faltas.
df['faltas_categoria'] = pd.cut(df['faltas'], bins=[-1, 10, 20], labels=['Até 10 faltas', 'Mais de 10 faltas'])
faltas_counts = df['faltas_categoria'].value_counts()

# Gerar o gráfico de barras
plt.figure(figsize=(8, 6))
faltas_counts.plot(kind='bar', color=['blue', 'red'])
plt.title('Quantidade de Alunos por Categoria de Faltas')
plt.xlabel('Categoria de Faltas')
plt.ylabel('Quantidade de Alunos')
plt.xticks(rotation=0)
plt.show()

#15º Gere um gráfico informando a quantidade de alunos com as seguintes notas:
#   1 - 4.9 (Necessita auxílio)
#   5 - 6.9 (Trabalhos extras para recuperar nota)
#   7 - 7.9 (Regular)
#   8 - 8.9 (Bom)
#   9 - 9.9 (Ótimo)
#   10 - (Parabéns)
def categorizar_nota(nota):
    if nota >= 10:
        return '10 - (Parabéns)'
    elif nota >= 9:
        return '9 - 9.9 (Ótimo)'
    elif nota >= 8:
        return '8 - 8.9 (Bom)'
    elif nota >= 7:
        return '7 - 7.9 (Regular)'
    elif nota >= 5:
        return '5 - 6.9 (Trabalhos extras)'
    else:
        return '1 - 4.9 (Necessita auxílio)'

df['categoria_nota'] = df['media'].apply(categorizar_nota)

categoria_counts = df['categoria_nota'].value_counts()

plt.figure(figsize=(10, 6))
categoria_counts.sort_index().plot(kind='bar', color='green')
plt.title('Quantidade de Alunos por Categoria de Nota')
plt.xlabel('Categoria de Nota')
plt.ylabel('Quantidade de Alunos')
plt.xticks(rotation=45)
plt.show()