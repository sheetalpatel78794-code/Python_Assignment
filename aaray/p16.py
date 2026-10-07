A = [1,2,-3,-4,2,3,-6,-2]

positive = []
negative = []

for i in range(len(A)):
    if A[i]>=0:
        positive.append(A[i])
    else:
        negative.append(A[i])

arr = []
i = 0
j = 0

while(i<len(positive) and j<len(negative)):
    arr.append(positive[i])
    arr.append(negative[i])
    i+=1
    j+=1

while(i<len(positive)):
    arr.append(positive[i])
    i+=1


while(j<len(negative)):
    arr.append(negative[i])
    j+=1

print(arr)
