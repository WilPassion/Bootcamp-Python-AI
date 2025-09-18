'''
LISTAS

https://docs.python.org/3/tutorial/datastructures.html

'''

cidade =["São Paulo", "Rio de Janeiro", "Belo Horizonte"]


print(type(cidade)) # <class 'list'>
print(len(cidade)) # 3

print(cidade) 
print(cidade[0]) # São Paulo  

# Mudando valor de um índice
cidade[0] = "Curitiba"
print(cidade) # ['Curitiba', 'Rio de Janeiro', 'Belo Horizonte']

# Adicionando um novo valor ao final da lista
cidade.append("Recife")
print(cidade) # ['Curitiba', 'Rio de Janeiro', 'Belo Horizonte', 'Recife']

# Removendo um valor da lista
cidade.remove("Recife")
print(cidade) # ['Curitiba', 'Rio de Janeiro', 'Belo Horizonte']

# CONCATENANDO LISTAS

letras = ['a', 'b', 'c']
numeros = [1, 2, 3]

lista = letras + numeros

print(lista) # ['a', 'b', 'c', 1, 2, 3]
# ou
letras.extend(numeros) # modifica a lista letras
print(letras) # ['a', 'b', 'c', 1, 2, 3]