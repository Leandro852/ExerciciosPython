p = float(input('Peso do peixe: '))

if p>50:
    e = (p-50)
    m = (p-50)*4
    if e==1:
        print (f'O peso do peixe é {e} quilo maior do que o permitido')
    if e>1:
        print (f'O peso do peixe é {e} quilos maior do que o permitido')
    print(f'custo da multa ficará em R$ {m}')
else:
    print ('O peso está dentro do limite')
