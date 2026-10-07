term = int(input("Enter a number:"))

num = 1
add = 1
for i in range(term+1):
    print(f"{num}",end=" ")

    num = num +add
    add= add +1
