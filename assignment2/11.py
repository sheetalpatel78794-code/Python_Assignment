age = int(input("Enter the age:"))
gender = input("Enter gender male or female:")
marital_status = input("Enter the marital status Y or N:")

if(gender == "female"):
    print(f"You work on urban/city area:")
elif(gender == "male"):
    if(age>=20 and age<40):
        print(f"You will work anywhere:")
    elif(age>=40 and age<60):
        print("You can work urban/city area:")
    else:
        print("ERROR")