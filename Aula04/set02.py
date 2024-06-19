# Armazene 5 nomes, retorne os nomes que possuem
# o maior número de caracteres.

# Set
nomes = {""}

# Contador de caracteres
qtdCaracteres = 0

# Armazenar cinco nomes
for i in range(5):
    print("Informe o {}º nome".format(str(i+1)))
    nome = input()

    if len(nome) > qtdCaracteres:
        qtdCaracteres = len(nome)

    nomes.add(nome)

# Exibir os nomes com a maior quantidade de caracteres
for n in nomes:
    if len(n) == qtdCaracteres:
        print(n)