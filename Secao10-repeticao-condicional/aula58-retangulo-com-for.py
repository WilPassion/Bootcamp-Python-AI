'''
Retângulo 6 x 6 com for

@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@

'''
linha = 6
coluna = 6  
caracter = "@"

for c in range(coluna):
    for l in range(linha):
        print(caracter, end="")
    print() # pular linha/enter