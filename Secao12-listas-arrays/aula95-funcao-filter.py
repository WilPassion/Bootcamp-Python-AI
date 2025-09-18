# FILTER FUNCTION  

valores = [10, 20, 30, 40, 50, 60]

def remover20(x):   # parâmetro preparado para receber um número,e não uma lista inteira, por isso usar FILTER
    return x > 20

print(list(filter(remover20, valores)))  # filter recebe dois parâmetros: uma função e um iterável (lista, tupla, etc

# Usando LAMBDA

print(list(filter(lambda x: x > 20, valores)))