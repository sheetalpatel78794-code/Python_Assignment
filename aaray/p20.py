A = [1,2,4,20,3,7,6,5]

max_count = 0
n = 5
for i in range(n):
    count =1
    num = A[i]

    while num+1 in A:
        num = num+1
        count +=1

    if count>max_count:
        max_count = count
        

print(max_count)