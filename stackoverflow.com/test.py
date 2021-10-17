num = int(input("Enter a positive number to test: "))
while  num < 0: 
    print("Invalid input, try again")
    num = int(input("Enter a positive number to test: "))
prime = False 
for i in range(2,num):
    if num % i == 0: #if remainder is zero, then there is a factor
        print(i, "is a factor of", num, "...stopping")
        print("")
        print(num, "is a not a prime number")
        break
    if num % i != 0:
        print(i, "is not a divisor of", num, "... continuing")
        prime = True
if prime == True: #once the condition from earlier is met, then it'll prove it's a prime numer
    print(num, "is a prime number")