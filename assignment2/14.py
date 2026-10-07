percent = int(input("Enter the percentage of the user:"))

if(percent>90):
    print("A")
elif(percent>80 and percent<=90):
    print("B")
elif(percent>=60 and percent<=80):
    print("C")
elif(percent<60):
    print("D")