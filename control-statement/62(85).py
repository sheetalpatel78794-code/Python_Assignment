for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    for space in range(5-i):
        print(" ",end="")
    for j in range(i,0,-1):
        print("*",end="")
    print()