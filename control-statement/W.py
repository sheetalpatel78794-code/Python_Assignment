for i in range(1,5):
    for j in range(1,8):
            if j==8-i or i==j:
                print("*",end="")
            else:
                print(" ",end="")
    for j in range(1,8):
        if j==8-i or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    


    print()