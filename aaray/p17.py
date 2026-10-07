A = [1,-3,0,5,4]
n = 5
k=0
found = False
for i in range(n):
    sum =0
    for j in range(i,n):
        sum = sum + A[j]

        if sum == k:
            found = True
            break
    if found:
        break
if found:
    print("Yes")
else:
    print("No")
