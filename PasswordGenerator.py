import random


password = ""
pass_length = int(input("Enter the length of password required: "))
ascii_numbers = list(range(33, 126))


for i in range(pass_length):
    password += chr(random.choice(ascii_numbers))

print("Here is your password -> " + password)
