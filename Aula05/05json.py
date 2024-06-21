# Importar o Pandas
import pandas as pd

# Ler o arquivo JSON
df = pd.read_json("pessoas.json")

# Exibir a estrutura do DataFrame
print(df.to_string())