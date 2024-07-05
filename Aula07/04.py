# Importar o Pandas
import pandas as pd

# Importar o Matplotlib
import matplotlib.pyplot as plt

# Importar arquivo xlsx
df_colaboradores = pd.read_excel("Planilha.xlsx", sheet_name="Planilha01")
df_cargos_salarios = pd.read_excel("Planilha.xlsx", sheet_name="Planilha02")

#1º Em colaboradores, crie uma nova coluna contendo o nome do cargo baseado no código
df_colaboradores['Cargo'] = df_cargos_salarios['Cargo'].iloc[0]
print(df_colaboradores)

#2º Em colaboradores, crie uma nova coluna contendo o salário do colaborador
df_colaboradores['Salario'] = df_cargos_salarios['Salario'].iloc[0]  # Assumindo que há apenas um salário na lista
print(df_colaboradores)

#3º Exiba: nome do colaborador, cargo e salário
resultado = df_colaboradores[['Nome', 'Cargo', 'Salario']]
print(resultado)

#4º Exiba todos os cargos e informe a quantidade de pessoas em cada cargo
qtd_por_cargo = df_colaboradores['Cargo'].value_counts()
print("Quantidade de pessoas por cargo:")
print(qtd_por_cargo)

#5º Exiba o nome do cargo com o maior salário
cargo_maior_salario = df_colaboradores.loc[df_colaboradores['Salario'].idxmax(), 'Cargo']
print(f"Cargo com o maior salário: {cargo_maior_salario}")

#6º Liste o nome dos colaboradores que ocupem o cargo de Analista de RH
colaboradores_analista_rh = df_colaboradores[df_colaboradores['Cargo'] == 'Analista de RH']['Nome'].tolist()
print("Colaboradores que ocupam o cargo de Analista de RH:")
print(colaboradores_analista_rh)

#7º Liste o nome e o salário dos colaboradores em ordem de salário (do mais alto para o mais baixo)
df_sorted_salario = df_colaboradores.sort_values(by='Salario', ascending=False)[['Nome', 'Salario']]
print("Colaboradores ordenados por salário (do mais alto para o mais baixo):")
print(df_sorted_salario)

#8º Exporte o arquivo em formato XLSX
df_colaboradores.to_excel('dados_colaboradores.xlsx', index=False)

#9º Crie um gráfico exibindo todos os cargos ocupados e também a quantidade de colaboradores que ocupam determinado cargo
contagem_cargos = df_colaboradores['Cargo'].value_counts()

plt.figure(figsize=(10, 6))
contagem_cargos.plot(kind='bar', color='skyblue')
plt.title('Quantidade de Colaboradores por Cargo')
plt.xlabel('Cargo')
plt.ylabel('Quantidade de Colaboradores')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#10º Crie um grafico contente o nome de todos os colaboradores e seus respectivos salários
nomes = df_colaboradores['Nome']
salarios = df_colaboradores['Salario']

plt.figure(figsize=(10, 8))
plt.barh(nomes, salarios, color='lightgreen')
plt.xlabel('Salário')
plt.ylabel('Nome do Colaborador')
plt.title('Salário dos Colaboradores')
plt.gca().invert_yaxis()  # Inverter eixo y para melhor visualização
plt.tight_layout()
plt.show()