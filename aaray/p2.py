a= [2,1,3,8]
max=a[0]
min=a[0]

for i in range(len(a)):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]

print(max)
print(min)