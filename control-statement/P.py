for i in range(1,7):
    for j in range(1,4):
        if i==1 or j==1 or i==3 or (j==3 and i<=3):
            print("*",end="")
        else:
            print(" ",end="")
    print()