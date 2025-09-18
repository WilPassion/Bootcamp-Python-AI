# LISTAS DENTRO DE LISTAS

#itens = [[lista1], [lista2]]
#itens = [[index1], [index2]]

itens = [["item1", "item2"], ["item3", "item4"]] 

print(itens[0][1]) # print(itens[posicao-lista][posicao-item]) -> item2

# UNPACKING LISTAS
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7, 8]
#             0        1        2         3       4  5  6  7

item1, item2, *outros, item8, = produtos

print(item1)
print(item2)
print(outros)

# LOOPING EM LISTAS

valores = [1, 2, 3, 4, 5, 6]

for v in valores:
    print(f'Valor atual: {v}')

# AGREGANDO LISTAS COM ZIP

cores1 = ["verde", "amarelo", "azul"]
valores = [10, 20, 30, 40]

duas_listas = zip(cores1, valores) 
print(list(duas_listas)) # [('verde', 10), ('amarelo', 20), ('azul', 30)]
    
# CONDICIONAL EM LISTAS

cor_cliente = str(input("Digite a cor desejada: "))
disponibilidade_cores = ["verde", "branco", "amarelo", "roxo", "azul" ]

if cor_cliente in disponibilidade_cores:
    print("Em estoque!")
else:
    print("Cor indisponível!")