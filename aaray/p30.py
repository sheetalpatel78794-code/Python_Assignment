A = [10,40,50]
b = [90,30,20,5]
B=[]
C= []
n = len(A)
m = len(b)
o = n+m

i=m-1
while(i>=0):
    B.append(b[i])
    i-=1


i = 0
j= 0
while(i<n and j<m):
    if A[i]>=B[j]:
        C.append(B[j])
        j+=1
    elif B[j]>=A[i]:
        C.append(A[i])
        i+=1

while(i<n):
    C.append(A[i])
    i+=1
while(j<m):
    C.append(B[j])
    j+=1

print(C)