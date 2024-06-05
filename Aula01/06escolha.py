# Obter cidade
print("Informe uma cidade")
cidade = input()

# Estrutura de escolha
match cidade:
    case "São Paulo":
        print("Capital do estado de São Paulo")
    
    case "Florianópolis":
        print("Capital do estado de Santa Catarina")
    
    case "Curitiba":
        print("Capital do estado do Paraná")

    case _:
        print("Sem informações...")