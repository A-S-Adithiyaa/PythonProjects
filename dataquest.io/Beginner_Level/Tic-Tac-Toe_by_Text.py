import random
import sys


moves = {11: ' ', 12: ' ', 13: ' ', 21: ' ', 22: ' ', 23: ' ', 31: ' ', 32: ' ', 33: ' '}
xo = ['X', 'O']


def display_xo(moves):
    print(moves[11] + " | " + moves[12] + " | " + moves[13])
    print("---------")
    print(moves[21] + " | " + moves[22] + " | " + moves[23])
    print("---------")
    print(moves[31] + " | " + moves[32] + " | " + moves[33])


def check_xo(dict):
    finalised = False
    for i in range(1, 4):
        row = []
        for j in range(1, 4):
            row.append(moves[10 * i + j])
        
        if row[0] == row[1] == row[2]:
            if row[0] in ['X', 'O']:
                display_xo(moves)
                print(str(moves[10 * i + j]) + ", You have won!")
                finalised = True

    if not finalised:
        for i in range(1, 4):
            col = []
            for j in range(1, 4):
                col.append(moves[10 * j + i])
            
            if col[0] == col[1] == col[2]:
                if col[0] in ['X', 'O']:
                    display_xo(moves)
                    print(str(col[0]) + ", You have won!")
                    finalised = True
                
    if not finalised:
        diag_lr = [moves[10 * (i+1) + i+1] for i in range(3)]
        if diag_lr[0] == diag_lr[1] == diag_lr[2]:
            if diag_lr[0] in ['X', 'O']:
                display_xo(moves)
                print(str(diag_lr[0]) + ", You have won!")
                finalised = True

    if not finalised:
        diag_rl = [moves[i] for i in [13, 22, 31]]
        if diag_rl[0] == diag_rl[1] == diag_rl[2]:
            if diag_rl[0] in ['X', 'O']:
                display_xo(moves)
                print(str(diag_rl[0]) + ", You have won!")
                finalised = True

    if finalised:
        sys.exit()


def play_xo():
    player_choice = input("Which letter do you choose 'X' or 'O'? : ").upper()
    cpu_choice = 'X'
    if player_choice == 'X':
        cpu_choice = 'O'

    while (player_choice not in xo) or (cpu_choice not in xo):
        player_choice = input("Which letter do you choose 'X' or 'O'? : ").upper()
        cpu_choice = 'X'
        if player_choice == 'X':
            cpu_choice = 'O'

    places_occup = []

    print("While entering position to place your letter, follow the below instructions.\nType 11 for entering your letter in 1st row and 1st column element, 32 to place your letter in 3rd row and 2nd columns element and so on...")

    for i in range(5):
        round_count = 1
        position = int(input("Enter the position : "))


        while position in places_occup:
            position = int(input("Sorry, the provided position is already occupied.\nEnter another position : "))

        while True:
            if position not in moves.keys():
                position = int(input("Sorry, the provided position is out of range.\nEnter another position : "))
            else:
                break

        places_occup.append(position)

        # row = position // 10
        # col = position - row * 10
        moves[position] = player_choice

        check_xo(moves) 
        if round_count < 5:
            i = random.randint(1, 3)
            j = random.randint(1, 3)
            while (i * 10 + j) in places_occup:
                i = random.randint(1, 3)
                j = random.randint(1, 3)
        
            position = 10 * i + j
            places_occup.append(position)

            moves[position] = cpu_choice
            round_count += 1
        check_xo(moves) 
        # print(moves)
        display_xo(moves)
        

play_xo()