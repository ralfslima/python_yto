# Importações
import pandas as pd
import sqlite3

# Selecionar o arquivo SQL
arquivo_sql = "pessoas.sql"

# Criar banco de dados temporário (memória)
conexao = sqlite3.connect(":memory:")

# Ler e executar arquivo SQL
with open(arquivo_sql, "r") as arquivo:
    script = arquivo.read()
    conexao.executescript(script)

# Comando SQL
#comando_sql = "SELECT * FROM pessoa"
#comando_sql = "SELECT COUNT(*) AS 'Quantidade' FROM pessoa"
comando_sql = "SELECT * FROM pessoa WHERE idade >= 30"

# DataFrame
df = pd.read_sql_query(comando_sql, conexao)

# Exibir os dados
print(df.to_string(index=False))