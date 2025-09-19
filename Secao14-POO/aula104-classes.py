'''

Em Python com Programação Orientada a Objetos (POO), uma instância é um objeto concreto criado a partir de uma classe.

Classe → funciona como um molde (ou blueprint). Define atributos (dados) e métodos (comportamentos).

Instância → é o objeto real que você cria usando esse molde. Cada instância pode ter seus próprios valores para os atributos.

'''
from datetime import datetime

class Cachorro:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def idade_real(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano_nascimento

# Criando instância
cachorro1 = Cachorro("Rex", 2020)

# Chamando a função
print(cachorro1.idade_real())  # Exemplo: 5 (se o ano atual for 2025)
from datetime import datetime

class Cachorro:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def idade_real(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano_nascimento

# Criando instância
cachorro1 = Cachorro("Rex", 2020)

# Chamando a função
print(cachorro1.idade_real())  # Exemplo: 5 (se o ano atual for 2025)