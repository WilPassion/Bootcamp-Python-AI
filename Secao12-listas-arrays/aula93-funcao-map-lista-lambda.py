# MAP FUNCTION
# Aplicar uma função a todos os itens de uma lista
# Retorna um map object (iterável)

# Mapeia/ associa cada item da lista à uma função

lista1 = [1, 2, 3, 4, 5]

def multi(x):
    return x * 2

lista2 = map(multi, lista1)  # map(funcao, iteravel)

print(list(lista2))  # [2, 4, 6, 8, 10] - convertendo para lista

# USANDO LAMBDA

print(list(map(lambda x: x * 2, lista1))) 