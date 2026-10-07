A = [1,-3,4,0]
n = 4
max_sum = A[0]
for i in range(n):
    sum =0
    for j in range(i,n):
        sum = sum + A[j]
    if sum>max_sum:
        max_sum = sum

print(max_sum)

        