for i in range(1,6):
    k=65
    for j in range(5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(k),end="")
        k+=1
    print()