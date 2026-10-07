arr = [10,20,30,40,50]
n = len(arr)
print("Before:",arr)
temp = arr[0]
arr[0]= arr[n-1]
arr[n-1] = temp

print("After:",arr)