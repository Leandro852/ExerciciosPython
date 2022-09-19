n = int(input('número: '))
x = 1
while n > x*(x+1)*(x+2) :
    x=x+1

print(x*(x+1)*(x+2) == n)
