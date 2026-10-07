num = int(input("Enter a number:"))
a = 1
b = 2

for i in range(num+1):
    print(a,end=" ")
    c= a*b
    a = b
    b = c
    