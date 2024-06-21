# Importar o Pandas
import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv("pessoas.csv")

# Adicionar a coluna e-mail
emails = ["aline.silva@gmail.com", "marcelo_123@hotmail.com"]
df["email"] = emails

# Exportar novo arquivo CSV
df.to_csv("meu_arquivo.csv", index=False)

# Exibir a estrutura do CSV
print(df.to_string())