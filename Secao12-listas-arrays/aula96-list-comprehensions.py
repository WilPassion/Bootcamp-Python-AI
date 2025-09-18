''' 
Uma list comprehension em Python é uma forma curta de criar listas a 
partir de uma sequência (como uma lista, range, ou até strings), aplicando uma expressão e, opcionalmente, um filtro.

              [expressão for item in sequência if condição]

* expressão → o valor que vai ser colocado na nova lista.

* for item in sequência → itera sobre a sequência.

* if condição (opcional) → filtra os itens.

'''

# Filtrar apenas números pares de 0 a 10
pares = [x for x in range(11) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8, 10]

# Transformar strings (deixar todas maiúsculas)
nomes = ["ana", "joão", "maria"]
maiusculas = [nome.upper() for nome in nomes]
print(maiusculas)  # ['ANA', 'JOÃO', 'MARIA']

# Gerar uma lista com os quadrados de 0 a 9
quadrados = [x**2 for x in range(10)]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Gerar uma lista if conter uma letra específica
frutas = ["maçã", "banana", "cereja", "damasco"]
frutas2 = [item for item in frutas if "m" in item]  # filtra frutas que contém a letra "m"
print(frutas2)  # ['maçã', 'damasco']

# Contar de 0 a 9 e multiplicar por 10
valores = [x * 10 for x in range(10)]
print(valores)  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]