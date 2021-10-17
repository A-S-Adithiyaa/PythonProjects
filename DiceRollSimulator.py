import random
 
choice = count = 1
 
print("Throwing the die...")
while True:
  if choice == 1:
    roll_result = random.randint(1, 6)
    print("Roll", choice, "=", roll_result)
    count += 1
    print()
  else:
    print("Stopping the die simulator...")
    break
 
  choice = int(input("Enter 1 to continue rolling the die, Enter 0 to stop the simulator: "))