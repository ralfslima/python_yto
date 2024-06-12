""""
    Dicionaty é um objeto.

    Objeto é um elemento que possui características
"""

# Criar um dictionary
pessoa = {
    "nome":"Ângela",
    "idade":36,
    "estuda":True
}

# Exibir uma informação
# print(pessoa)
#print(pessoa["nome"])

# Alterar o valor de um atributo
pessoa["nome"] = "Roberta"

# Remover característica
pessoa.pop("estuda")

# Exibir o dictionary
print(pessoa)