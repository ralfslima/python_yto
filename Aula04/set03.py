# Peça 5 números, em seguida retorne a posição, onde o número digitado seja igual a 10. 
# Caso não tenha sido informado o número 10, exiba: ”O número 10 não foi encontrado”.

# Set
numeros = {0}

# Armazenar números
for indice in range(5):
    print("Informe o {}º número".format(str(indice+1)))
    numeros.add(int(input()))

# Variável lógica
existe10 = False

# Exibir a posição onde se encontra o número 10
indice = 0
for n in numeros:
    if n == 10:
        print("O número 10 foi encontrado na posição: {}".format(str(indice)))
        existe10 = True

    indice += 1

# Exibir o SET para validar
print(numeros)

# Caso não seja encontrado o número 10
if not existe10:
    print("O número 10 não foi encontrado!")