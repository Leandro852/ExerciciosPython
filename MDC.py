a= int(input('maior número: '))
b= int(input('menor número: '))

while a%b!=0:
    a, b=b, a%b
print (f'mdc = {b}')
        
    
