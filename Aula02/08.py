# Solicita os três números ao usuário
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

# Cria uma lista com os números e a ordena
numeros = [numero1, numero2, numero3]
numeros.sort()

# Exibe os números ordenados
print("Valores em ordem crescente:", numeros)
