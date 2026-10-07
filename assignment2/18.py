unit = int(input("Enter the electricity unit charges:"))

if(unit<=50):
    bill = unit*0.50
    
elif(unit>=51 and unit<150):
    bill = (50*0.50)+(unit-50)*0.75
    
elif(unit>=150 and unit<250):
    bill = (50*0.50)+(100*0.75)+(unit-150)*1.20
    
elif(unit>=250):
    bill = (50*0.50)+(100*0.75)+(100*1.20)+(unit-250)*1.50
    

subcharges = (bill*20)/100
total = bill + subcharges

print(f"Bill: {total}")
