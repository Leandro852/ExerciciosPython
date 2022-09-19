velocidade = int(input('Velocidade do carro: '))
if velocidade > 110:
    multa = (velocidade-110)*5
    print (int(input(f'O usuário foi multado em R$:{multa:.2f}')))
else:
    print ('o usuário não foi multado')
