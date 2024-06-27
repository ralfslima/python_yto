# Importações
import matplotlib.pyplot as plt
import numpy as np

# Posição das bolinhas
x = np.array([5, 6, 7])
y = np.array([99, 86, 55])
t = [300, 40, 10]

# Criar gráfico
plt.scatter(x, y, s=t)

# Exibir gráfico
plt.show()