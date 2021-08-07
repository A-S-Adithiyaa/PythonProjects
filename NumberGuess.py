'''A Number guessing game, which allows user to choose a number between 1-10 or 1-100'''

import random

def comparision_hint(random_num, guess_num):
    if random_num > guess_num:
        print("The secret number is greater than your guess")
    else:
        print("The secret number is lower than your guess")

# def divisibility_hint(random_num):
#     lst = []
#     for i in range(2, random_num):
#         if random_num % i == 0:
#             lst.append(i)
#     length = len(lst)
#     index = random.randint(0, length-1)
#     if len(lst) == 0:
#         print("The secret number is a prime number")
#     else:
#         print("The secret number is divisible by", lst[index], ", try guessing it now")
#     del lst[index]

# def give_hint(random_num, guess_num):
#     if hint_num % 2 != 0:
#         comparision_hint(random_num, guess_num)
#     else:
#         divisibility_hint(random_num)

print("-------WELCOME TO THE NUMBER GUESSING GAME-------\n")

level_scale = {
    'e' : {
        'lower' : 0,
        'higher' : 10
    },
    'n' : {
        'lower' : 0,
        'higher' : 50
    },
    'h' : {
        'lower' : 0,
        'higher' : 100
    },
    'ex' : {
        'lower' : 0,
        'higher' : 150
    }
}

new_match = 0
while not new_match:
    score = 0
    hint_num = 0
    level = input("Choose the difficulty level from Easy('e'), Normal('n'), Hard('h') and Expert('ex') or 'quit' to exit the game:  ").lower()
    
    if level == 'quit':
        break
    else:
        lower = level_scale[level]["lower"]
        higher = level_scale[level]["higher"]
        
        print("\nSO YOU WILL BE CHOOSING A NUMBER FROM", lower, "to", higher)
        
        random_num = random.randint(lower, higher)
        
        print("***If you want to PLAY A NEW MATCH('n'), or END THE GAME('e'), enter 'n' and 'e' respectively, when asked to enter an input.***\n")

        play_again = 0
        while not play_again:
            
            guess_num = input("Enter an integer ranging from " + str(lower) + " to " + str(higher) + ": ")

            if guess_num.isdigit():
                guess_num = int(guess_num)
                if guess_num == random_num:
                    print("WHOA!, You have guessed the correct number\n")
                    play_again = 1
                    score += 4
                    print("You have scored", score, "point(s)")
                else:
                    print("SORRY!, It was an incorrect guess\n")
                    hint_num += 1
                    score -= 1
                    comparision_hint(random_num, guess_num)

            else:
                if guess_num == 'n':
                    play_again = 1
                elif guess_num == 'e':
                    print("You are quitting the game!\nThanks for playing")
                    print("You have scored", score, "point(s) in total")
                    play_again = 1
                    new_match = 1