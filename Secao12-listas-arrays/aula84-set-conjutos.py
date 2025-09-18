'''
É uma coleção não ordenada e sem elementos duplicados.

remove duplicados automaticamente;

é otimizado para busca e teste de existência (in) mais rápido que lista;

permite operações matemáticas de conjuntos (união, interseção, diferença).

Quando usar:

* Quando você não precisa de ordem.

* Quando você não quer duplicados.

* Quando precisa fazer operações matemáticas de conjuntos (união, interseção, diferença).

* Quando o mais importante é verificar se algo existe (performance muito melhor que lista).

'''
list1 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]
list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # União
print(num1 & num2) # Interseção
print(num1 - num2) # Diferença
print(num1 ^ num2) # Diferença Simétrica
print(len(num1)) # Tamanho