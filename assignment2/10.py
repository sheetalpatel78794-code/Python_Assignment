year = int(input("Enter the year:"))

if(year%4==0 or year%400==0):
    print(f"Leap year:{year}")
else:
    print(f"Not Leap year:{year}")