for i in range(5,0,-1):
    for j in range(5,0,-1):
        if i==5 or j==5 or i+j==6:
            print(i,end="")
        else:
            print(" ",end="")
    print()