# pip3 install geopandas

# Importações
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd

# Criar bolinha
x = np.array([-50])
y = np.array([-20])

# Importar o mapa do Brasil
brasil = gpd.read_file("BR_Pais_2022/BR_Pais_2022.shp")

# Criar o mapa
mapa, eixo = plt.subplots()
brasil.plot(ax=eixo, color="lightgrey")

# Criar o gráfico
plt.scatter(x, y)

# Exibir o gráfico
plt.show()