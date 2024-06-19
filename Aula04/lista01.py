# Desenvolva um sistema que peça um nome e duas notas. 
# Em seguida retorne a média e a situação do aluno (aprovado ou reprovado). 
# Armazene o nome, as notas, média e situação em um list. 
# Enquanto o cliente quiser cadastrar novos alunos, deverão ser executados
# todos os passos anteriores. 
# Quando sair do laço, exiba todos os dados (nome, notas, média e situação).

# Lista
alunos = []

# Continuar
continuar = 0

# Laço de repetição
while continuar != 2:
    # Obter nome
    print("Informe o nome")
    nome = input()

    # Obter a primeira nota
    print("Informe a primeira nota")
    nota1 = float(input())

    # Obter a segunda nota
    print("Informe a segunda nota")
    nota2 = float(input())

    # Realizar a média
    media = (nota1+nota2)/2

    # Realizar a situação
    situacao = "Aprovado" if media >= 7 else "Reprovado"

    # Retorno
    print("{} com média {}".format(situacao, str(media)))

    # Cadastrar aluno na lista
    alunos.append({
        "nome":nome,
        "nota1":nota1,
        "nota2":nota2,
        "media":media,
        "situacao":situacao
    })

    # Verificar se deseja cadastrar um novo aluno
    print("Deseja cadastrar um novo aluno?")
    print("1 - SIM")
    print("2 - NÃO")
    continuar = int(input())

# Listar todos os alunos
for a in alunos:
    print("Nome: " + a["nome"])
    print("Primeira nota: " + str(a["nota1"]))
    print("Segunda nota: " + str(a["nota2"]))
    print("Média: " + str(a["media"]))
    print("Situação: " + a["situacao"])
    print()