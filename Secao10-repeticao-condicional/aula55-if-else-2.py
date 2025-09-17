# Enviar um e-mail com detalhes da compra online
# Máximo 3 tentativas para compras confirmadas

compra_confirmada = True
dados_compra = "Compra no valor de R$ 150,00 e entrega confirmada"

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("Detalhes enviados por e-mail")
        break
else:
    print("Falha na compra")