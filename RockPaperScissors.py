import random


valid_entries = ['r', 'p', 's']
winning_combos = {
    'r' : 's',
    's' : 'p',
    'p' : 'r',
}
cpu_score = player_score = 0

while True:
    player_choice = input("Enter your choice, r(Rock), p(Paper), s(Scissors): ")

    if player_choice.lower() == 'e':
        print("Player Score: ", player_score)
        print("CPU Score: ", cpu_score)
        break
    elif player_choice.lower() in valid_entries:
        cpu_choice = random.choice(valid_entries)
        print(cpu_choice)
    else:
        print("INVALID ENTRY!. choose one among 'r', 'p', 's'.")
        continue

    if winning_combos[player_choice] == cpu_choice:
        print("Player has won the round")
        player_score += 1
    elif winning_combos[cpu_choice] == player_choice:
        print("CPU has won the round")
        cpu_score += 1
    else:
        print("Tie")