a = [3,1,2,8]
max_sum = 0
n = len(a)


for _ in range(len(a)):
    sum = 0
    for i in range(len(a)):
        sum = sum + (a[i]*i)

    if sum>max_sum:
        max_sum=sum
    temp = a[0]
    for j in range(len(a)-1):
        a[j] = a[j+1]
    a[n-1]=temp
    print(a)

print(max_sum)
