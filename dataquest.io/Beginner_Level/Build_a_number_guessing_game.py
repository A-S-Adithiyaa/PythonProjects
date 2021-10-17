import random


def generate_num(start, end):
    return random.randint(start, end)


def higher_or_lower(user_num, winning_num):
    if user_num > winning_num:
        print("Hint-1 : Try entering a LOWER NUMBER\n")
    elif user_num < winning_num:
        print("Hint-1 : Try entering a HIGHER NUMBER\n")


def show_multiples(winning_num, count):
    multiples = []
    for i in range(2, 10):
        if winning_num % i == 0:
            multiples.append(i)

    if count > len(multiples):
        print("Sorry there are only these many hints possible.")
    else:
        print("Hint-2 : The number to be guessed is a multiple of the following -> ", end = "")
        for i in range(count):
            print(multiples[i], end=', ')

    print("\n")


def num_guess():
    winning_num = generate_num(0, 10)

    user_num = int(input("Enter a number : "))

    i = 0
    while user_num != winning_num:
        print("\nSorry, you have entered an incorrect number. Try again!")
        if i == 0:
            higher_or_lower(user_num, winning_num)
        else:
            show_multiples(winning_num, i)

        i += 1
        
        user_num = int(input("Enter a number : "))

    
    print("\nYou have entered the correct number!. CONGRATULATIONS...")


num_guess()