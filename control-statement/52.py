num1= int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))

if num1>num2:
    i = num2+1
else:
    i = num1+1

while(i<num1 or i<num2):
    j=i
    num=j
    count = 0
    while(j>0):
        j=j//10
        count+=1
    org = num
    sum = 0
    while(num>0):
        digit = num%10
        sum = sum + digit**count
        num = num//10
    if sum==org:
        print(f"{i} is amstrong")
    else:
        print(f"{i} not amstrong")


    
        
    
    i+=1