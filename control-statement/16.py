num = int(input("Enter a number"))

for i in range(-(num+1),(num+1),1):
    if i%3==0:
        print(f"{i}",end=" ")
    