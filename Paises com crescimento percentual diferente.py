pa= 80000
pb=200000
a=1

while pa<=pb:
    pa = pa+pa*1.03
    pb = pb+pb*1.015
    a=a+1
    if pa>pb:
        print(f'a população do país A passou a de pb em {a} anos)')      
    
