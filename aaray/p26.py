arr = [10,40,50,80,100]
max =arr[0]
min =arr[0]
for i in range(len(arr)):
    if arr[i]>=max:
        max = arr[i]
    if arr[i]<=min:
        min = arr[i]

print(f"Max= {max}")
print(f"Min= {min}")