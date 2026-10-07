for i in range(6,0,-1):
    for j in range(1,i+1):
        if i==5 or i==3:
            print(i-j+1,end="")

        else:
            print(j,end="")
    print()
