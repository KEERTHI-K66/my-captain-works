n=int(input('enter the no '))
x=[]
a=1
b=1
x.append(a)
x.append(b)
while a+b <=n:
    c=a+b
    x.append(c)
    a=b
    b=c
for k in range(0,len(x)):
    print(x[k])
