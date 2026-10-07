n = int(input("Enter a number"))
for i in range(1,n+1):
    if i==1:
        print(f"{i}+",end=" ")
    else:
        print(f"1/{i}+",end=" ")