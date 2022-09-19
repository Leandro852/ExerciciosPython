minutos = int(input('minutos: '))
if minutos < 200:
    preço = 0.2
elif minutos <= 400:
    preço = 0.18
elif minutos <=800:
    preço=0.15
else:
    minutos >800
    preço=0.08
print(f'Sua fatura é de R$:{minutos*preço:.2f}')
