for i in range(1,4):
    for space in range(2,1,-1):
            print(" ",end="")
    for j in range(1,6):
        if j==1 or j==2*i-1 :
            print("*",end="")
        else:
            print(" ",end="")

    for space in range(3,1,-2):
                print(" ",end="")
    for j in range(1,6):
        if j==1  :
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
    
