for i in range(1,6):
    for j in range(i):
        if j==1 or j==3 or j==5:
            print("#",end="")
        else:
            print("*",end="")
    print()