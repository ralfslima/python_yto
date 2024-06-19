# Utilizando uma tupla e um dictionary, armazene 5 cidades e uma descrição. 
# Exiba as 5 cidades e peça para o cliente escolher uma, 
# em seguida exiba a descrição da cidade.

# Criar dictionaries
cidade1 = {"nome":"São Paulo", "descricao":"Maior cidade do país"}
cidade2 = {"nome":"Rio de Janeiro", "descricao":"Belas praias"}
cidade3 = {"nome":"Belo Horizonte", "descricao":"Pão de quejo Uai!"}
cidade4 = {"nome":"Florianópolis", "descricao":"Capital catarinense"}
cidade5 = {"nome":"Brasília", "descricao":"Capital do Brasil"}

# Criar a tupla
cidades = (cidade1, cidade2, cidade3, cidade4, cidade5)

# Índice
indice = 1

# Laço de repetição para listar as cidades
for c in cidades:
    print("{} - {}".format(indice, c["nome"]))
    indice += 1

# Armazenar o número da cidade
codigo = int(input())

# Exibir a desrição da cidade
print(cidades[codigo-1]["descricao"])