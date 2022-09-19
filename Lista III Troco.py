troco = int(input('valor: '))
k = 0
x = 0
restante = troco

while restante != 0:
    if troco >=50:
        x = 50
        restante = troco - x
        k= k+1
    elif restante >= 20:
        x = 20
        restante = troco - x
        k= k+1
    elif restante >= 10:
        x = 10
        restante = troco - x
        k= k+1
    elif restante >= 5:
        x = 5
        restante = troco - x
        k= k+1
    elif restante >= 2:
        x = 2
        restante = troco - x
        k= k+1
    else:
        x=1
        restante = troco-x
        k= k+1
print(f'o número de notas é de {k}')
