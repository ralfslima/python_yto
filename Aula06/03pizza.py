# Importações
import matplotlib.pyplot as plt
import numpy as np

# Dados
dados = np.array([20, 25, 15, 30, 10])

# Rótulo
rotulos = ["Linguagem R", "Python", "Tableau", "Excel", "SQL"]

# Espaçamento
espacamento = [0.1, 0.1, 0.1, 0.1, 0.1]

# Cores
cores = ["#8b1ff0", "#6d15bf", "#5d278f", "#41215e", "#2b163d"]

# Criar gráfico
plt.pie(dados, labels=rotulos, explode=espacamento, shadow=True, colors=cores)

# Legenda
#plt.legend(title="Tecnologias")

# Exibir gráfico
plt.show()