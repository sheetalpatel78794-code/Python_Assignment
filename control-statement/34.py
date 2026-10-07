num  = int(input("Enter a number:"))

sum = 0
temp =num

for i in range(1,num):
    if num%i==0:
        sum = sum+i

if sum==temp:
    print("perfect No.")
else:
    print("Not perfect")