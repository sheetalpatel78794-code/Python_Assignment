total_days = int(input("Enter the total no. of days:"))
class_held = int(input("Enter the number of classes miss:"))
class_attended = int(input("Enter the number of classes attended:"))
medical =input("Enter the medical suitation:")

print(f"No. of class missed: {class_held}")
print(f"No. of class attended: {class_attended}")

percent_held = (class_held*100)/total_days
percent_attended = (class_attended*100)/total_days

if(percent_attended>75 or medical == "Y" ):
    print("You are eligible:")
else:
    print("You are not eligible:")

