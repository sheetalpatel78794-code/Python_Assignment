name = input("Enter the name of the customer:")
gender = input("Enter the gender of the customer:")
date = input("Enter the date:")
item = 10
first_price = 10
second_price = 20
third_price = 30
fourth_price = 40
five_price = 50
six_price = 60
seven_price = 70
eight_price = 80
nine_price = 90
ten_price = 100

first_item = input("Enter the first item name:")
first_quantity = int(input("Enter the first item quantity:"))
second_item = input("Enter the second item name:")
second_quantity = int(input("Enter the second item quantity:"))
third_item = input("Enter the third item name:")
third_quantity = int(input("Enter the third item quantity:"))
fourth_item = input("Enter the fourth item name:")
fourth_quantity = int(input("Enter the fourth item quantity:"))
five_item = input("Enter the five item name:")
five_quantity = int(input("Enter the five item quantity:"))
six_item = input("Enter the six item name:")
six_quantity = int(input("Enter the six item quantity:"))
seven_item = input("Enter the seven item name:")
seven_quantity = int(input("Enter the seven item quantity:"))
eight_item = input("Enter the eight item name:")
eight_quantity = int(input("Enter the eight item quantity:"))
nine_item = input("Enter the nine item name:")
nine_quantity = int(input("Enter the nine item quantity:"))
ten_item = input("Enter the ten item name:")
ten_quantity = int(input("Enter the ten item quantity:"))

if(first_quantity>4):
    total1 = first_price*first_quantity
    first_discount = (total1*5)/100
    total1 = total1 - first_discount
else:
    total1 = fourth_price*fourth_quantity

if five_item:
    total5 = five_price * five_quantity
    five_discount = (total5*10)/100
    total5 = total5 - five_discount

if ten_item:
    total10= ten_price * ten_quantity
    ten_discount = (total10* 15)/100
    ten_price = total10 - ten_discount

total = total1 + second_price + third_price + fourth_price  + total5 + six_price + seven_price + eight_price + nine_price + total10

if(total>10000):
    discount = (total *15)/100
    total = total - discount

elif(total>5000 and total<10000):
    discount = (total * 10)/100
    total = total - discount

gst = (total * 10)/100
total = total + gst

carry = input("You want carry:")
if(carry == "yes"):
    total = total + 10
else:
    total = total

if(gender == "she"):
    print("Gift Cadburry")
elif(gender == "he"):
    print("Gift leather purse")

print("                                                   D-Mart                                                  ")
print(f"Name  : {name}                                                                                                       date:{date}")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(" Item Name                Quantity                  Price                               total                                  After-Discount               ")
print(f"  {first_item}                   {first_quantity}                            {first_price}                                   {first_price *first_quantity}                                  {total1} ") 
print(f"  {second_item}                  {second_quantity}                            {second_price}                                  {second_price *second_quantity}                               {second_price *second_quantity}")
print(f"  {third_item}                   {third_quantity}                            {third_price}                                   {third_price *third_quantity}                                  {third_price *third_quantity}")
print(f"  {fourth_item}                  {fourth_quantity}                           {fourth_price}                                  {fourth_price *fourth_quantity}                                {fourth_price * fourth_quantity}")
print(f"  {five_item}                    {five_quantity}                             {five_price}                                    {five_price * five_quantity}                                   {total5}")
print(f"  {six_item}                     {six_quantity}                              {six_price}                                     {six_price *six_quantity}                                      {six_price *six_quantity}")
print(f"  {seven_item}                   {second_quantity}                           {seven_price}                                   {seven_price *seven_quantity}                                  {seven_price *seven_quantity}")
print(f"  {eight_item}                   {eight_quantity}                            {eight_price}                                   {eight_price *eight_quantity}                                  {eight_price *eight_quantity}")
print(f"  {nine_item}                    {nine_quantity}                             {nine_price}                                    {nine_price *nine_quantity}                                    {nine_price *nine_quantity}")
print(f"  {ten_item}                     {ten_quantity}                              {ten_price}                                     {ten_price *ten_quantity}                                      {total10}")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Total Bill {total}")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                      Thank you\n                                                      To Visit \n                                                      D-mart                                                       ")
