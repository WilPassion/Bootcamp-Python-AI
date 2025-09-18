'''LAMBDA FUNCTION

* É uma função (pequena) sem nome
* Muito utilizada em conjunto com outras funções
* Código mais limpo e enxuto

* Pode ter vários argumentos (x), mas apenas uma expressão (x + 10)

* Use lambda → quando for uma função simples, de 1 linha, geralmente passada como parâmetro.

* Use def → quando a função for mais complexa, precisar de mais linhas, comentários ou reutilização.
'''

dobro = lambda x: x * 2
print(dobro(5))  

#############

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))



