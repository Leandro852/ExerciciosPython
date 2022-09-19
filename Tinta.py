m = (float(input('Insira o tamanho, em m², do comodo: ')))
if m % 54 == 0:
    latas = m/54
else:
    latas =int((m/54)+1)

valor = latas*80

print(f'O número de latas de tinta é de {latas}')
print(f'O custo é de R$ {valor}')
    
  
    
