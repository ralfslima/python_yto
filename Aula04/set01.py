# Peça vários números, até que seja informado o número zero. 
# Exiba a soma dos valores, a média e a quantidade de números 
# maiores ou iguais a média.

# Criar set
numeros = {0}

# Variável número
numero = -1

# Variável para somar
soma = 0

# Variável contendo a quantidade de números maiores ou iguais a média
contadorMaiorIgualMedia = 0

# Laço de repetição
while numero != 0:
    # Obter número
    print("Informe um número")
    numero = int(input())

    # Somar
    soma += numero

    # Armazenar o número no SET
    numeros.add(numero)

# Realizar a média
media = soma / len(numeros)

# Laco de repetição
for n in numeros:
    if n >= media:
        contadorMaiorIgualMedia += 1

# Retornos
print("Soma dos valores: {}".format(str(soma)))
print("Média dos valores: {}".format(str(media)))
print("Números maiores ou iguais a média: {}".format(str(contadorMaiorIgualMedia)))
