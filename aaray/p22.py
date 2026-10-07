n = int(input("Enter a  size of number:"))
a = []

for i in range(n):
    num = int(input("Enter a number:"))
    a.append(num)

print(a)
target = int(input("Enter a number which available in array"))
lesser = None
greater = None

for i in range(n):
    if a[i]<target:
        if lesser is None or a[i]>lesser:
            lesser = a[i]

    if a[i]>target:
        if greater is None or a[i]<greater:
            greater = a[i]

print("Element lesser than ",target,"is",lesser)
print("Element greater than",target,"is",greater)