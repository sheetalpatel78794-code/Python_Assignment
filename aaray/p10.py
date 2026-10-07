x = [10,20,30,40,50]

item = x[-1]

for i in range(len(x)-1,0,-1):
    x[i]=x[i-1]
x[0]=item

print(x)