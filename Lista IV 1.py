from random import sample
vetor =sample(range(100), 10)
maior = menor = vetor [0]
for x in vetor[1:]:
    if x > maior: maior = x
    if x< menor: menor = x
print('vetor', vetor)
print(f'maior:{maior}')
print(f'menor:{menor}')
