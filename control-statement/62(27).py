for i in range(1,6):
    for j in range(1,i+1):
        if i==5 or j==1 or i==j:
            if j%2==0:
                print("0",end="")
            else:
                print("1",end="")
        else:
            print(" ",end="")
           
       
    print()