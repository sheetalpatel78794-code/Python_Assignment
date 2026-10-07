num = int(input("Enter a number:"))
count =0

for i in range(1,num+1):
    if num%i==0:
        count+=1


if count>=3 or num<=1:
        print(" NOt Prime No.")
else:
    print("Prime No.")