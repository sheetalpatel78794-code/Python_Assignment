for i in range(1,5):
    for j in range(1,6):
        if i==1:
           print("*",end="")
        
        elif i==2:
            if j==2:
               print(" ",end="")

            else:
               print("*",end="")

        elif i==3:
           print("*",end="")

        elif i==4:
           if j==5:
               print("*",end="")
           else:
               print(" ",end="")

    print()
    