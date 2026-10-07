num1= int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))

if num1>num2:
    i = num2+1
else:
    i = num1+1

while(i<num1 or i<num2):
  fact = 1
  j=i
  while(j>1):
    fact = fact*j
    j-=1
  print(f"factorial {i} {fact}")
    

  i+=1
    
    
  