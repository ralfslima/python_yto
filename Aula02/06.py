# Solicita os dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica se os números são iguais
if numero1 == numero2:
    resultado = numero1 + numero2
else:
    resultado = numero1 * numero2

# Exibe o resultado
print("O resultado é:", resultado)
