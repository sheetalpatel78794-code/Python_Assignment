arr = [1,3,5,7,6,9,1]

non_repeat=None
for i in range(len(arr)-1):
    count = 0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count+=1
        
    if count == 1:
        non_repeat=arr[i]
        break
if non_repeat is not None:
    print(non_repeat)

else:
    print("Not found")
    
