for i in range(1,8):
    for j in range(1,8):
        if i+j==8 or i==j:
            print("*",end="")
        
        else:
            print(" ",end="")
    print()