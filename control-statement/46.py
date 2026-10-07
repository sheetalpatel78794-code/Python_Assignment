num = int(input("Enter a number:"))
last_digit = num%10
temp = num
count = 0
while(temp>0):
    temp = temp//10
    count +=1

while(count>1):
    num = num//10
    count-=1
first_digit = num

sum = last_digit+first_digit
print(f"SUM = {sum}")


  