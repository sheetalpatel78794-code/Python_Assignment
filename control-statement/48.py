num1 = int(input("Enter first number :"))
num2 = int(input("Enter secound number :"))

if num1<num2:
    i = num1+1
else:
    i = num2+1

while(i<num1 or i<num2):
    print(f"Factor of {i}")
    for j in range(1,i):
        if i%j ==0:
            print(f"{j}",end=" ")
    print()
    i+=1

