"""
    Criar um sistema para gerenciar pessoas.

    Será possível:
    - Listar todos os nomes
    - Cadastrar novos nomes
    - Remover
    - Finalizar
"""

# Criar lista de nomes
nomes = []

# Variável contendo a opção
opcao = 0

# Laço de repetição
while opcao != 4:

    # Obter opção
    print("1 - Listar")
    print("2 - Cadastrar")
    print("3 - Remover")
    print("4 - Finalizar")
    opcao = int(input())

    # Estrutura de escolha
    match opcao:
        # Listar
        case 1:
            for n in nomes:
                print(n)

        # Adicionar
        case 2:
            print("Informe um nome")
            nomes.append(input())

        # Remover
        case 3:
            print("Informe um nome")
            nomes.remove(input())

        # Finalizar
        case 4:
            print("Obrigado por utilizar o sistema.")