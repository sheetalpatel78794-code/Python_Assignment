arr = [3,2,5,3,9]
s = 10
start = 0
sum = 0
for i in range(len(arr)):
    sum = sum +arr[i]

    while sum>s:
        sum = sum - arr[start]
        start = start+1

    if sum == s:
        print(f"{start+1} {i+1}")
        break
