for i in range(1,4):
    for j in range(1,6):
        if (i==1 and j>=3) or (i==3 and j<=3)  or j%2!=0  :
            print("*",end="")
        
        else:
            print(" ",end="")
    print()