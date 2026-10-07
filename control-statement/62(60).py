for i in range(1,6):
    for space in range(5-i):
        print(" ",end="")

    for j in range(1,i+1):
            if i==5 or j==1 or i==j:
                print("X",end="")
                print(" ",end="")
            else:
                print("__",end="")
    
    print()