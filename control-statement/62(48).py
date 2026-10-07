for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(1,i+1):
        if i==j or i==5 or j==1:
            print(chr(64+j),end="")
        else:
            print(" ",end="")
    print()