tempo = int(input('minutos gastos: '))
if tempo < 200:
    valor = tempo*0.20
    print(f'sua fatura é de R$:{valor}')
if tempo >= 200 and tempo <= 400:
    valor = tempo*0.18
    print(f'sua fatura é de R$: {valor}')
if 800 >= tempo >= 400:
    valor = tempo*0.15
    print(f'sua fatura é de R$:{valor}')
else:
    if tempo > 800:
        valor = tempo * 0.08
        print(f'sua fatura é de R$:{valor}')
