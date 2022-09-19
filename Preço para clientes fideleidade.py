import urllib.request
preço = 15
while preço >=4.70:
    pagina = urllib.request.urlopen(
        'http://beans.itcarlow.ie/prices-loyalty.html') 
    texto = pagina.read().decode('utf8')
    onde= texto.find('>$')
    inicio=onde +2
    fim = inicio+4
    preço = float(texto[inicio:fim])
    if preço > 4.70:
        time.sleep(600)
    
print (f' Comprar: R$ {preço:.2f}')
