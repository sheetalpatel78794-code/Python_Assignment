math = int(input("Enter the mark of maths:"))
science = int(input("Enter the mark of science:"))
english = int(input("Enter the mark of english:"))
hindi = int(input("Enter the mark of hindi:"))
chemistry = int(input("Enter the mark of chemistry:"))

total = math + science + english + hindi + chemistry
percent = total/5

if(percent<25):
    print("F")
elif(percent>=25 and percent<45):
    print("E")
elif(percent>=45 and percent<50):
    print("D")
elif(percent>=50 and percent<60):
    print("C")
elif(percent>=60 and percent<80):
    print("B")
else:
    print("A")
