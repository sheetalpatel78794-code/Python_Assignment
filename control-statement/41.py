num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number: "))

if(num1>num2):
    i=num1
else:
    i=num2

while True:
    if i%num1==0 and i%num2==0:
        print(f"LCM",i)
        break
    i+=1

  
      
    


  