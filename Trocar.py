p=input('palavra: ')
k=0
troca=''
while k < len(p):
    if p[k] in 'aeiou':
        troca=troca+'*'
    else:
        troca=troca+p[k]
    k=k+1
print (troca)
