mensagem = "   Estou treinando métodos de string no Python.   "

print(mensagem.strip()) # remove espaços no início e no fim

print(mensagem.lower())
print(mensagem.upper())

print(mensagem.title()) 
print(mensagem.capitalize()) # Estou Treinando Métodos De String No Python.

print(mensagem.split()) # Divide em lista de palavras
print(mensagem.split("n")) # Divide em lista de palavras a partir de "n"

print(mensagem.replace("Python", "JavaScript"))

print(mensagem.startswith("E")) # False