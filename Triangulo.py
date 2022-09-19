a = float(input('primeiro lado do triangulo: '))
b = float(input('segundo lado do triangulo: '))
c = float(input('terceiro lado do triangulo: '))

if a+b<c or a+c<b or b+c<a:
    print('as arestas não formam um triangulo')
else:
    if a==b==c:
        print('o triangulo é equilátero')
    elif a==b!=c or a!=b==c or a==c!=b:
        print ('o triangulo é isósceles')
    else:
        print('o triangulo é escaleno')
