# Opções
print("Selecione uma das cinco cidades:")
print("1. Paris")
print("2. Nova York")
print("3. Tóquio")
print("4. Rio de Janeiro")
print("5. Sydney")

# Obter a cidade
escolha = input("Digite o número correspondente à cidade: ")

# Retorno
if escolha == "1":
    print("Paris é a capital da França e uma das cidades mais visitadas do mundo, conhecida por sua arquitetura icônica, cultura rica e história fascinante.")
elif escolha == "2":
    print("Nova York é uma cidade vibrante e diversificada, conhecida por seus arranha-céus imponentes, vida noturna agitada, cultura cosmopolita e amplas opções de entretenimento.")
elif escolha == "3":
    print("Tóquio é uma metrópole moderna e frenética, conhecida por sua tecnologia de ponta, culinária deliciosa, cultura pop única e tradições antigas.")
elif escolha == "4":
    print("Rio de Janeiro é uma cidade deslumbrante, famosa por suas praias icônicas, carnaval animado, montanhas majestosas e estilo de vida descontraído.")
elif escolha == "5":
    print("Sydney é uma cidade cosmopolita e vibrante, conhecida por sua bela baía, a icônica Opera House, praias de areias brancas e estilo de vida ao ar livre.")
else:
    print("Escolha inválida. Por favor, digite um número de 1 a 5 para selecionar uma cidade.")
