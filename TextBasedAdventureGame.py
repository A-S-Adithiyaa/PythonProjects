import random
from test import GeneratePaths

directions = ['l', 'r', 's', 'b']
path_followed = []
sucessful_paths = GeneratePaths.generate_paths()

play_again = 1
while play_again:
    steps_taken = 0
    i = random.randint(0, 9)
    sucessful_path = sucessful_paths[i]
    start_or_end = input("Shall we start the game? yes('y') or no('n'): ")
    if start_or_end == 'y':
        move = input("How should you move, left('l'), straight('s') or right('r'): ").lower()
        steps_taken += 1
    else:
        break

    path_followed.append(move)
    while True:
        move = input("How should you move, left('l'), straight('s'), right('r') or back('b'): ").lower()
        if move == 'b':
            path_followed.pop()
        else:
            path_followed.append(move)

        if path_followed in sucessful_path:
            print("Whoa!, you have reached the TREASURE")
            play_again = input("Wanna play again? yes('y') or no('n'): ")
            if play_again == 'n':
                print("Thankyou for playing!")
                play_again = 0
            break
        print("You are trapped, try moving back('b') and continue")
