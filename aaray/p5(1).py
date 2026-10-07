arr = [4,1,7,9,3,1,0,3,4,6]

n= int(input("Enter a number"))

count =0
for i in range(len(arr)):
    if arr[i]==n:
        count+=1
print(f"Count {count}")