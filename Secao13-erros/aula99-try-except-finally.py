# ERROS
# Para testes
# Não realiza o "stop" do programa

# * try -> tentar executar o código
# * except -> ocorreu algum erro, faça isso - SEMPRE EM CIMA DE UM ERRO Q VOU TER
# * finally -> sempre será executado (opcional)  

# Exemplo 1 - IndexError

try:
    letras = ['A', 'B', 'C']
    print(letras[3])  
except IndexError:
    print("Index não existe")


# Exemplo 2 - ValueError

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Favor digitar um valor válido")


# Exemplo 3 - ZeroDivisionError

try:
    a = 10
    b = 0
    resultado = a / b
    print(resultado)
except ZeroDivisionError:
    print("Não é possível dividir por zero.")


# Exemplo 4 - FileNotFoundError

try:
    with open("arquivo.txt", "r") as f:
        conteudo = f.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome do arquivo.")


# Exemplo 5 - Vários erros possíveis

try:
    num = int(input("Digite um número: "))
    print(10 / num)
except ValueError:
    print("Você não digitou um número válido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")


# Exemplo 6 - else e finally

try:
    num = int(input("Digite um número: "))
except ValueError:
    print("Erro: valor inválido.")
else:
    print(f"Você digitou {num}. Nenhum erro ocorreu.")
finally:
    print("Fim do programa (sempre executa).")

# Exemplo 7

try: 
    letras = ['A', 'B', 'C']
    print(letras[3])  
except IndexError:
    print("Index não existe")

# Exemplo 8
try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Favor digitar um valor válido")
finally:
    print("Código Ok!")