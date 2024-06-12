"""
    Crie um set, enquanto não for informado o número
    zero, armazene um valor no set.

    Quando digitado o valor zero, liste os valores sem repetição e 
    exiba a soma dos valores informados.
"""

# Criar a estrutura set
numeros = {0}

# Variável número
numero = -1

# Variável soma
soma = 0

# Laço enquanto
while numero != 0:

    # Obter um número
    print("Informe um número")
    numero = int(input())

    # Realizar a soma dos valores informados
    soma += numero

    # Armazenar o valor da variável no set
    numeros.add(numero)

# Exibir a soma
print("A soma dos valores é {}".format(str(soma)))

# Exibir os números informados
print("Os valores informados são: {}".format(str(numeros)))