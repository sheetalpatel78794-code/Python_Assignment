quantity = int(input("Enter the quantity:"))
cost = quantity*100

if(cost>1000):
    discount = (cost*10)/100
    cost = cost - discount
    print(f"discount is available bill is {cost}")

else:
    print(f" no discount is available the bill is {cost}")