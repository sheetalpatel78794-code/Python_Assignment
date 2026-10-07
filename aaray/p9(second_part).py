a = [1,2,3,4,3]
b = [5,4,3,2]

i=0
intersection = []

while(i<len(a)):
    j=0
    while(j<len(b)):
        if a[i]==b[j]:
            if a[i] not in intersection:
                intersection.append(a[i])
        j+=1
    i+=1

print(intersection)
print(len(intersection))