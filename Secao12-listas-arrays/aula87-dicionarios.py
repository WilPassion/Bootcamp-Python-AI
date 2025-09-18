# DICIONARIOS
# Index no formato chave:valor

aluno = {
    "nome": "Ana", 
    "idade": 25, 
    "curso": "Ciência da Computação", 
    "nota": 8.5, 
    "aprovação": True}

print(aluno)

print(aluno['nome']) # Acessa o valor da chave nome

aluno.update({"idade": 26}) # Atualiza o valor da chave idade
print(aluno)

print(aluno.keys()) # Mostra as chaves

print(aluno.values()) # Mostra os valores

print(len(aluno)) # Tamanho do dicionário

################

print(aluno.get("endereço")) # None -> PJ3
print(aluno.get("endereço", "Endereço não existe")) # Endereço não existe

################

del aluno["curso"] # Remove a chave curso

# LOOPING

for v in aluno.values():  
    print(v, end=' ')   # Ana 26 8.5 True
    
for k in aluno.keys():
    print(k, end=' ')   # nome idade nota aprovação    
    
for key, value in aluno.items():
    print(key, value, end=' | ')   # nome Ana | idade 26 | nota 8.5 | aprovação True |