k=1
for i in range(1,6):
    for j in range(1,i+1):
            if i==j or j==1 or i==5:
                print(chr(k+96),end="")
                k+=1
            else:
                 print(" ",end="")    
    print()
    