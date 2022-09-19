p=input('insira a palavra que desejas verificar a palindromidade: ')

if p==p[::-1]:
    print(f'A palavra {p} é palídrome')
else:
    print(f'A palavra {p} não é palíndrome')
