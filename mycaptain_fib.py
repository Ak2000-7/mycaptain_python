x=int(input('enter a no of term you want for fibanocci series'))
a=-1
b=1
for i in range(x+1):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
