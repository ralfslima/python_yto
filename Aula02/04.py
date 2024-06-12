# Solicita os três valores ao usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Verifica qual é o menor valor
if valor1 <= valor2 and valor1 <= valor3:
    menor_valor = valor1
elif valor2 <= valor1 and valor2 <= valor3:
    menor_valor = valor2
else:
    menor_valor = valor3

# Exibe o menor valor
print("O menor valor é:", menor_valor)