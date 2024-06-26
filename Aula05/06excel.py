# Importar biblioteca: pip3 install openpyxl

# Importar o Pandas
import pandas as pd

# Importar arquivo xlsx
df = pd.read_excel("Planilha.xlsx", sheet_name="Planilha02")

# Exibir conteúdo
print(df.to_string())