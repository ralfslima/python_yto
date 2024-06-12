# Solicita o ano ao usuário
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto
if ano % 4 == 0:
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")
