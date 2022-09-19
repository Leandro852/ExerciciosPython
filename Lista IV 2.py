from random import sample
vetor = sample(range(100), 20)
par = []
impar = []
for x in vetor [1:]:
    if x%2 == 0:
        par.append(x)
    if x%2!=0:
        impar.append(x)
print('vetor',vetor)
print('pares',par)
print('impares', impar)
