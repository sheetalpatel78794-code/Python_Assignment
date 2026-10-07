for i in range(5,0,-1):
    for space in range(5-i):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or i==5 or j==2*i-1 :
            print(j,end="")
        else:
            print(" ",end="")
    print()