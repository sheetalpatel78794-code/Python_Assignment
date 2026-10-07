ram_age = int(input("Enter the age of ram:"))
shyam_age = int(input("Enter the age of shyam:"))
shivam_age = int(input("Enter the age of shivam:"))

if(ram_age>shyam_age and ram_age>shivam_age):
    print(f"Ram is older than shyam and shivam  {ram_age} year")
elif(shyam_age>shivam_age):
    print(f"shyam is older than ram and shivam {shyam_age} year  ")
else:
    print(f"shivam is older tham ram and shyam {shivam_age} year")