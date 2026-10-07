arr = []
n = int(input("Enter a length of arrray:"))
sum = 0
for i in range(n):
    j = int(input("Enter a number:"))
    arr.append(j)
    sum = sum + arr[i]
average = sum//n

print("array:",arr)
print("sum:",sum)
print("average",average)
