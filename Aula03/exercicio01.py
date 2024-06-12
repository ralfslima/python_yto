""""
    Criar uma lista imutável de cargos.

    O cliente informa um cargo e precisamos retornar
    se o cargo existe ou não na lista.
"""

# Criar tupla contendo cargos
cargos = ("Atendente", "Financeiro", "Gerente", "Vendedor", "Suporte")

# Variál contendo a situação da pesquisa
existe = False

# Obter o cargo
print("Qual cargo está procurando?")
cargo = input()

# Pesquisar o cargo informado
for c in cargos:
    if c == cargo:
        existe = True

# Retorno
if existe:
    print("O cargo existe na tupla.")
else:
    print("Cargo não encontrado.")