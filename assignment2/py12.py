number = int(input("Enter the four digit number:"))
reverse = 0

rem = number%10
reverse = (reverse * 10) + rem
number= number//10

rem = number%10
reverse = (reverse * 10) + rem
number= number//10

rem = number%10
reverse = (reverse * 10) + rem
number= number//10

rem = number%10
reverse = (reverse * 10) + rem
number= number//10

print(f"reverse of number: {reverse}")
