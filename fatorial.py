n= int(input('insira o numero a ser feito o fatorial: '))

k=1
fat=1
while k<=n:
    fat = fat*k
    k=k+1
print(f'fat({n})= {fat}')
