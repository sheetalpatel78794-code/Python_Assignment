A = [6,-3,-10,0,2]
n = 5
max_mult = A[0]
for i in range(n):
    mult = 1
    for j in range(i,n):
        mult = mult * A[j]
        if mult>max_mult:
            max_mult = mult

print(max_mult)

        