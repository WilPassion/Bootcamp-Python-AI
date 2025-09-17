velocidade = 49

if velocidade > 100:
    print(f"Sua velocidade é {velocidade}")
    print("Reduza para o limite permitido")
elif velocidade  > 50 and velocidade <= 100:
    print("Você está dentro do limite de velocidade")
else:
    print("Velocidade permitida, mas cuidado")
    
print("FIM")