# Obter um número
print("Informe um número")
numero = int(input())

# Condicional
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# Operador ternário
print("Par" if numero % 2 == 0 else "Ímpar")