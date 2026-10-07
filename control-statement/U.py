for i in range(1,4):
    for j in range(1,4):
        if j==1 or j==3 or i==3:
            print("*",end="")
        else:
            print(" ",end="")
    print()