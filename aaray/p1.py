arr = [1,2,3,4,5]

for i in range(len(arr)):
    if i == 0:
        if arr[i]>=arr[i+1]:
            print(f"{arr[i]},index : {i}")
            break
    elif i==len(arr)-1:
        if arr[i]>=arr[i-1]:
            print(f"{arr[i]},index : {i}")
            break

    else:
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            print(f"{arr[i]} index {i}")
            break


        