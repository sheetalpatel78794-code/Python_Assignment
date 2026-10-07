num = int(input("Enter a decimal no"))

binary = 0
i = 1
while(num>0):
  rem= num%2
  binary = binary + rem*i
  i = i*10
  num=num//2
print(f"{binary}",end="" )
  