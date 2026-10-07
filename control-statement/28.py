n = int(input("Enter a value of n:"))
for i in range(1,n+1):
    if i%5==0:
        print(f"Hello",end=" ")
    else:
        print(f"{i}",end=" ")
