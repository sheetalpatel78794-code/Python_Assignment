num = int(input("Enter a number binary no.:"))
decimal =0
i =0
while num>0:
    last_digit = num%10
    decimal = decimal+last_digit*(2**i)
    num = num//10
    i+=1

print(decimal)