for i in range(1,6):
    for space in range(5-i):
        print(" ",end="")
    for j in range(i,1,-1):
        print(j,end="")
    for k in range(1,i+1):
        print(k,end="")

    print()
