A = [90,70,50]
B = [80,60,40,30]
C= []
n = len(A)
m = len(B)
o = n+m


i = 0
j= 0
while(i<n and j<m):
    if A[i]>=B[j]:
        C.append(A[i])
        i+=1
    elif B[j]>=A[i]:
        C.append(B[j])
        j+=1

while(i<n):
    C.append(A[i])
    i+=1
while(j<m):
    C.append(B[j])
    j+=1

print(C)