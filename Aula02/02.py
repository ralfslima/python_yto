# Variável para armazenar o voto
voto = 0

# Variáveis para contabilizar os votos
alice = 0
bianca = 0
cleiton = 0
daniel = 0

# Laço de repetição
while voto < 5:

    # Opções para votar
    print("1 - Alice")
    print("2 - Bianca")
    print("3 - Cleiton")
    print("4 - Daniel")
    print("5 - Finalizar votação")
    voto = int(input())

    # Contabilização
    match voto:
        case 1:
            alice+=1

        case 2:
            bianca+=1

        case 3:
            cleiton+=1

        case 4:
            daniel+=1

# Exibir votos
print("Alice obteve: {} voto(s)".format(alice))
print("Bianca obteve: {} voto(s)".format(bianca))
print("Cleiton obteve: {} voto(s)".format(cleiton))
print("Daniel obteve: {} voto(s)".format(daniel))