num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
choice = input("Enter the choice:")

if(choice == "+"):
    sum = num1 + num2
    print(f"addition : {sum}")

elif(choice == ">"):
    if(num1>num2):
        print("num1 is greater than num2")
    else:
        print("num2 is greater than num1")

elif(choice == "=="):
    if(num1 == num2):
        print(f"Both number is equal")
