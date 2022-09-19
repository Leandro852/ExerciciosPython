import string

texto =open('alice.txt').read().lower()
for c in string.punctuation: 
    texto-texto.replace(c, ' ')
    
palavras = texto.split()

wc={}
for p in palavras:
    if p in wc: #se a palavra ja esta no wc, ela vai incrementar mais um no cotador#
        wc[p] +=1
    else:
        wc[p]=1 #caso contrario, ela vai se adicionada ao dicionário#


def contador(dupla):
    return dupla[1]
#key é a chave de ordenação, que nesse caso é por ordem de ocorrencia#

duplas = sorted(wc.items(), key=contador, reverse=True)

for dupla in duplas [:20]: #são as 20 duplas mais frequentes
    print(dupla[0], dupla [1])
