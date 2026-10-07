for i in range(1,5):
    for space in range(4-i):
        print(" ",end="")
    for j in range(1,8):
        if (i==3 and j<=5 )  or j==1 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()