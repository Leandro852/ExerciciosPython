cpd = int(input('Quantos maços por dia: '))
tf = float(input('Quantos anos fumando: '))
vida = float(cpd*10*(tf*365))/(60*24)
print (f' Dias de vida perdidos {vida}')
