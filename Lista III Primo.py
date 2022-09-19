n = int(input('Número: '))
k=2
while n%k != 0:
    k=k+1
    if n%k==0:
        if k == n :
            print(' é primo')
        else:
            print('não é primo')
        
