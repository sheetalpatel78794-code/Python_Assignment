physics = int(input("Enter the mark of physics:"))
chemistry = int(input("Enter the mark of chemistry:"))
biology = int(input("Enter the mark of biology:"))
mathematics = int(input("Enter the mark of mathematics:"))
computer = int(input("Enter the mark of computer:"))

total = physics + chemistry + biology + mathematics + computer
percent = total/5

print(f"Total : {total}")
print(f"percent {percent}")
if(percent>=90):
    print("Grade A")
elif(percent>=80):
    print("Grade B")
elif(percent>=70):
    print("Grade C")
elif(percent>=60):
    print("Grade D")
elif(percent>=40):
    print("Grade E")
elif(percent<40):
    print("Grade F")