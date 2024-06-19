# Peça 5 nomes e armazene na lista, em seguida exiba os nomes informados. 
# Não será possível cadastrar nomes iguais, valide ao efetuar o cadastro.

# Lista
nomes = []

# Índice
indice = 0

# Laço de repetição
while indice < 5:

    # Obter nome
    print("Informe o {}º nome.".format(str(indice+1)))
    nome = input()

    # Variável lógica
    existeNome = False

    # Verificação
    for n in nomes:
        if n == nome:
            existeNome = True

    # Retorno
    if existeNome == False:
        nomes.append(nome)
        indice += 1

# Exibir os cinco nomes
for n in nomes:
    print(n)