
for i in range(1,6):
    for space in range(5-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        k=64
        print(chr(j+k),end="")
        print(" ",end="")
        k+=1
    
    print()