# Crie uma tupla contendo 5 valores inteiros. 
# Utilizando uma função random, gere um número entre 0 e 4, 
# em seguida exiba o valor da tupla utilizando sua posição 
# através do número gerado.

# Importar a biblioteca random
import random

# Gerar valores aleatórios
valor1 = random.randint(0, 4)
valor2 = random.randint(0, 4)
valor3 = random.randint(0, 4)
valor4 = random.randint(0, 4)
valor5 = random.randint(0, 4)

# Criar tupla
numeros = (valor1, valor2, valor3, valor4, valor5)

# Exibir os valores contidos na tupla
print(numeros)
