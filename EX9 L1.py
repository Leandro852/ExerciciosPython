dist = float(input('distância, em quilômetros, percorrida: '))
dias = int(input('dias de uso do carro: '))
custo = float(dias*60 + dist*0.15)
print (f'Total a pagar: {custo}')
