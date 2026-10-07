n = int(input("Enter a number:"))
for i in range(0,n+1,2):
    print(f"{i*i}",end=" ")

for j in range(1,n+1):
    print(f"{j}",end=" ")