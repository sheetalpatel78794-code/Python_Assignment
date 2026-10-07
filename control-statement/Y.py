for i in range(1,8):
    for j in range(1,8):
        if j==8-i or (i==j and j<=4):
            print("*",end="")
        else:
            print(" ",end="")
    print()