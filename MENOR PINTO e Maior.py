a= float(input('Primeiro numero: '))
b= float(input('Segundo numero: '))
c= float(input('Terceiro numero: '))

if a<=b and a<=c:
    print (f'O menor numero é {a}')
elif b<c:
    print (f'O menor numero é {b}')
else:
    print (f'O menor numero é {c}')

if a>b and a>c:
    print (f'O maior numero é{a}')
elif b>a and b>c:
    print (f'O maior numero é{b}')
else:
    print (f'O maior numero é{c}')
