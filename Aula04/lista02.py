# Crie um sistema para gerenciar produtos, será possível 
# cadastrar, selecionar, alterar e remover produtos, 
# além da possibilidade de finalizar o sistema. 
# Os dados que serão gerenciados são: nome do produto, marca e valor.

# Lista de produtos
produtos = []

# Opção
opcao = 0

# Laço de repetição
while opcao != 5:
    # Menu
    print("*** MENU ***")
    print("1 - Cadastrar")
    print("2 - Selecionar")
    print("3 - Alterar")
    print("4 - Remover")
    print("5 - Sair")
    opcao = int(input())

    # Estrutura de escolha
    match opcao:
        case 1:
            print("Qual é o nome do produto?")
            nome = input()

            print("Qual é a marca do produto?")
            marca = input()

            print("Qual o valor do produto?")
            valor = float(input())

            obj = {
                "nome":nome,
                "marca":marca,
                "valor":valor
            }

            produtos.append(obj)

        case 2:
            for p in produtos:
                print("Nome: {}".format(p["nome"]))
                print("Marca: {}".format(p["marca"]))
                print("Valor: {}".format(p["valor"]))
                print()

        case 3:
            indice = 0
            print("Informe o código do produto:")
            for p in produtos:
                print(str(indice)+" - "+p["nome"])
                indice += 1
            indice = int(input())

            print("Qual é o nome do produto?")
            nome = input()

            print("Qual é a marca do produto?")
            marca = input()

            print("Qual o valor do produto?")
            valor = float(input())

            obj = {
                "nome":nome,
                "marca":marca,
                "valor":valor
            }

            produtos[indice] = obj

        case 4:
            indice = 0
            print("Informe o código do produto:")
            for p in produtos:
                print(str(indice)+" - "+p["nome"])
                indice += 1
            indice = int(input())

            produtos.pop(indice)