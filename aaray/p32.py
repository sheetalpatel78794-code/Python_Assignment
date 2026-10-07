A = [2,5,10,8,3]
B = [1,9,7,6,4,11]
even = []
odd_uo = []
odd = []

for i in range(len(A)):
    if A[i]%2==0:
        even.append(A[i])
    else:
        odd_uo.append(A[i])

for j in range(len(B)):
    if B[j]%2==0:
        even.append(B[j])
    else:
        odd_uo.append(B[j])

i = len(odd_uo)-1
while(i>=0):
    odd.append(odd_uo[i])
    i-=1

C = even+odd
print(C)
