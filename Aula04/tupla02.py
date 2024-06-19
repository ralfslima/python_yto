# Crie uma tupla contendo 5 cores. 
# Peça para o cliente informar uma cor, 
# se a cor informada consta na tupla, 
# exiba: “A cor existe na tupla”, 
# caso contrário: “Cor não encontrada”

# Criar tupla
cores = ("verde", "amarelo", "azul", "vermelho", "rosa")

# Obter uma cor
print("Informe uma cor")
cor = input()

# Existência da cor
existe = False

# Laço de repetição
for c in cores:
    if c == cor:
        existe = True

# Retorno
if existe:
    print("A cor existe na tupla")
else:
    print("Cor não encontrada")