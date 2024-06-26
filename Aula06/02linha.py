# Importações
import matplotlib.pyplot as plt
import numpy as np

# Vendedores
vendedor1 = np.array([3000, 5000, 9000, 7000, 8000])
vendedor2 = np.array([2000, 8000, 7000, 9000, 5000])
vendedor3 = np.array([1000, 2000, 6000, 10000, 7000])

# Rótulo de meses
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"]

# Criar gráfico
plt.plot(meses, vendedor1, marker="o", label="Vendedor 01", color="#5af2ca")
plt.plot(meses, vendedor2, marker="o", label="Vendedor 02", color="#3ea88c")
plt.plot(meses, vendedor3, marker="o", label="Vendedor 03", color="#226352")

# Adicionar legenda
plt.legend()

# Grid
plt.grid()

# Exibir gráfico 
plt.show()