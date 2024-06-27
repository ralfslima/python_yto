# Importações
import matplotlib.pyplot as plt
import numpy as np

# Informações
nomes = np.array(["Renato", "Cristiane", "Alan", "Julia"])
vendas = np.array([12800, 11300, 14000, 9870])
cores = ["red", "purple", "blue", "pink"]

# Criar gráfico
plt.bar(nomes, vendas, color=cores)

# Exibir o gráfico
plt.show()