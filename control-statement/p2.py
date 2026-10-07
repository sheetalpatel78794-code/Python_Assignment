num = int(input("Enter a number:"))
n = len(str(num))
term = n//2
sum = 0

for i in range(term+1):
    if num%i == 0:
        sum = sum+i

if(sum==num):
    print("Perfect no.")
else:
    print("Not perfect")
