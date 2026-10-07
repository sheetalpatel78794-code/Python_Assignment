k=5
for i in range(1,6):
   
    for j in range(5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(k,end="")
    k-=1
    print()
