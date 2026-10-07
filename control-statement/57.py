num1= int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))

if num1>num2:
    i = num2+1
else:
    i = num1+1

while(i<num1 or i<num2):
  
  j=i
  count =0
  while(j>=1):
    if i%j ==0:
       count +=1
    j-=1

  if(count==2):
     print("prime")
  else:
     print(f"{i}")
    

  i+=1
    
    
  