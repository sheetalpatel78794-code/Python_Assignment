num1= int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))

if num1>num2:
    i = num2+1
else:
    i = num1+1

while(i<num1 or i<num2):
    j=i
    rev = 0
    while(j>0):
        rem = j%10
        rev = rev*10+rem
        j//=10
        
    if rev==i:
        print(f"{i} palindrome")
    else:
        print(f"{i} not palindrome")
    i+=1