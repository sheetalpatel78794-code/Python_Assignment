ch = input("Enter a lowercase letter:")

i = 97
while(i<=122):
    if chr(i) == ch:
        letter = chr(i - 32)
        print(f"Letter in Uppercase: {letter}")
    i = i + 1
