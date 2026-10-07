num1 = int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))

if num1<num2:
    i = num1+1

else:
    i = num2+1

while(i<num1 or i<num2):
    print(f"Table of {i}")
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
    print()
    i += 1