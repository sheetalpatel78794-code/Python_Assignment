arr = [1,0,2,1,0,2,2,0,1,0,1,2,2,0,1]

zc=0
oc=0
tc=0
for i in arr:
    if i==0:
        zc+=1
    elif i==1:
        oc+=1
    else:
        tc+=1
for i in range(zc):
    arr[i]=0
for i in range(zc,zc+oc):
    arr[i]=1
for i in range(zc+oc,zc+oc+tc):
    arr[i]=2

print(arr)