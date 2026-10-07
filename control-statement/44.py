num = int(input("Enter a number:"))

last = num%10
temp = num
count =0

while temp>0:
    temp = temp//10
    count+=1

first = num//(10**(count-1))

middle = (num%(10**(count-1)))//10

new_num = last*(10**(count-1))+middle*10+first

print(new_num)