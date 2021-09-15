
x=input('Enter no seprated by blank space')
y=x.split(" ")
print('your entered list is',y)
print('positive numbers are')
for i in y:
    if int(i)>0:
        print(i,end=' ')
    
