arr = [1,5,7,2,1,3]

count = 0
k =int(input("Enter a number to pair of sum:"))
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==k:
            count+=1

print(count)