# Contadores
alunos_aprovados = 0
alunos_reprovados = 0

while True:
    # Solicita o nome e as notas ao usuário
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    # Calcula a média
    media = (nota1 + nota2) / 2

    # Verifica a situação do aluno
    if media >= 7.0:
        situacao = "Aprovado"
        alunos_aprovados += 1
    else:
        situacao = "Reprovado"
        alunos_reprovados += 1

    # Exibe os resultados
    print("\nNome do aluno:", nome)
    print("Média:", media)
    print("Situação:", situacao)

    # Pergunta se deseja continuar cadastrando alunos
    continuar = input("\nDeseja cadastrar outro aluno? (s/n): ")
    if continuar.lower() != "s":
        break

# Exibe o total de alunos aprovados e reprovados
print("\nTotal de alunos aprovados:", alunos_aprovados)
print("Total de alunos reprovados:", alunos_reprovados)
