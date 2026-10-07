num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

if num1>num2:
    i = num2+1
else:
    i = num1+1

while(i<num1 or i<num2):
    if(i%400==0 or (i%4==0 and i%100!=0)):
        print(f"Leap Year {i}")
    i+=1

