
for i in range(1,6):
    for space in range(5-i):
        print(" ",end="")

    for j in range(1,6):
        if i+j>=6: 
            print("*",end="")
            print(" ",end="")
    
    print()