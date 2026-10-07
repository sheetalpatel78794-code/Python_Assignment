salary = int(input("Enter the salary:"))
year = int(input("Enter the year of experience:"))
bonus = 0

if(year>5):
    bonus = (salary*5)/100
    print(f"Net bonus {bonus}")
else:
    print(f"Net bonus {bonus}")