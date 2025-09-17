### FUNÇÃO SIMPLES

def boas_vindas():
    print("Olá William")
    print("Estamos treinando Python")
    
boas_vindas()


# FUNÇÃO COM PARÂMETROS

def welcome(name, quantidade):
    print(f"Olá {name}")
    print(f"Você tem {str(quantidade)}")
    
welcome("William", 23)

# FUNÇÃO COM PARÂMETROS DEFAULT
# Default = qdo definimos um valor padrão para o parâmetro
# Non-default = qdo não definimos um valor padrão para o parâmetro

def welcome2(name, quantidade=6):  # ordem non-default > default
    print(f"Olá {name}")
    print(f"Você tem {str(quantidade)}")
    
welcome2("William", 23)

### FUNÇÃO COM RETURN
# O return armazena o valor enquanto o print apenas exibe o valor e descarta

def cliente1(nome):
    print(nome)

cliente1("William")

# 

def cliente2(nome):
    return nome

print(cliente2("William"))

### XARG - FUNÇÃO USADO QDO NÃO SABEMOS A QUANTIDADE DE PARÂMETROS

def soma(*args):  # args = argumentos
    resultado = 0
    for numeros in args:
        resultado += numeros
    return resultado

x = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(x)

'''
XARG ** -> a função pode receber argumentos nomeados (chave=valor) em quantidade variável.

Esses argumentos são guardados em um dicionário Python.

No caso: carro vai ser um dict com todas as chaves e valores que você passar.

'''

def agencia(**carro):
    return carro

print(agencia(marca="Ford", modelo="Ka", cor="Prata", ano=2020))


