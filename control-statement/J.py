for i in range(1,5):
    for j in range(1,6):
        if i==1 or (i==4 and j<=3)or (i==3 and j==1) or j==3  :
            print("*",end="")
        
        else:
            print(" ",end="")
    print()