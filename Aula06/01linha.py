# Importações
import matplotlib.pyplot as plt
import numpy as np

# Criar uma linha
eixoX = np.array([0,6])
eixoY = np.array([0,250])

# Criar o gráfico
plt.plot(eixoX, eixoY, color="green")

# Título do gráfico
plt.title("Meu primeiro gráfico!")

# Grid
plt.grid()

# Legenda dos eixos
plt.xlabel("Horizontal")
plt.ylabel("Vertical")

# Exibir gráfico
plt.show()