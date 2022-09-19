Ano = int(input('insira o ano: '))

if Ano %4==0 and (Ano%100!=0 or Ano %400==0):
    print (f'O ano de {Ano} é bissexto')
else:
    print (f'O ano de {Ano} não é bissexto')
