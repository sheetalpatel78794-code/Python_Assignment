num1= int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))

if num1>num2:
    i = num2+1
else:
    i = num1+1

while(i<num1 or i<num2):
  j=i
  sum =0
  while(j>0):
    digit = j%10
    fact=1
    while(digit>1):
      fact = fact*digit
      digit -=1
    sum = fact+sum
    j=j//10
    
  if sum==i:
    print(f"{i} strong")   
  i+=1