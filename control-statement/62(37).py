for i in range(5,0,-1):
    for j in range(0,i):
        if i==1 or i==3 or i==5:
            print("*",end="")
        else:
            print("#",end="")
        
    print()