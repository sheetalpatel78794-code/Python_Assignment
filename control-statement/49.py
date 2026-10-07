num1= int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))

if num1>num2:
    i = num2+1
else:
    i = num1+1

while(i<num1 or i<num2):
    j=i-1
    sum = 0
    while(j>0):
        if i%j==0:
            sum = sum+j
        j-=1
    if sum==i:
        print(f"{i} perfect no.")
    else:
        print(f"{i} is not perfect no.")
    i+=1