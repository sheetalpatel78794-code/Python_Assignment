n = 4
A = [1, 0, 1, 1]

count = 0

for i in range(n):
    count0 = 0
    count1 = 0

    for j in range(i, n):

        if A[j] == 0:
            count0 += 1
            
        else:
            count1 += 1
            

        if count0 == count1:
            count += 1
            print(i,j)

print(count)