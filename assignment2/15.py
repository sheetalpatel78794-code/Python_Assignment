bike_price = int(input("Enter the bike price:"))

if(bike_price>100000):
    tax = (bike_price*15)/100
    bike_price=bike_price+tax
    print(f"The bike price included with gst {tax}: price {bike_price}")
elif(bike_price>50000 and bike_price<=100000):
    tax = (bike_price*10)/100
    bike_price = bike_price+tax
    print(f"The bike price included with gst {tax}: price {bike_price}")
elif(bike_price<=50000):
    tax = (bike_price*5)/100
    bike_price= bike_price+tax
    print(f"The bike price included with gst {tax}: price {bike_price}")