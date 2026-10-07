N = int(input("Enter a size of array:")) 
arr = []
for i in range(N+1):
    element = int(input("Enter the element:"))
    arr.append(element)



print(arr)
pos = []
neg = []

for i in arr:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)

    result  = pos + neg
print(result)

