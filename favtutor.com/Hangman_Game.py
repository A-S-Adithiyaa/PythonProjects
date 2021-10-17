word = 'suriyha'
accepted_words = "abcdefghijklmnopqrstuvwxyz"
guessed_word = "_ " * len(word)
tries = 8

print(guessed_word)
print("\nTry to guess the word.\n")

while True:
    word_ind = []

    guess = input("Enter your guess : ")

    while (guess not in accepted_words) or (len(guess) != 1):
        print("It was an incorrect guess, try again.")
        guess = input("Enter your guess : ")

    if guess in word:
        for ch in word:
            if guess == ch:
                word_ind.append(word.index(ch))

        guessed_word_lst = guessed_word.split()

        for ind in word_ind:
            guessed_word_lst[ind] = guess
        
        guessed_word = " ".join(guessed_word_lst)
    
    else:
        tries -= 1

    if tries == 7:
        print(tries, ", tries are left")
        print("         ")
        print("         ")
        print("    O    ")
        print("         ")
        print("         ")
    if tries == 6:
        print(tries, ", tries are left")
        print("         ")
        print("         ")
        print("    O    ")
        print("    |    ")
        print("         ")
    if tries == 5:
        print(tries, ", tries are left")
        print("         ")
        print("         ")
        print("    O    ")
        print("   /|    ")
        print("         ")
    if tries == 4:
        print(tries, ", tries are left")
        print("         ")
        print("         ")
        print("    O    ")
        print("   /|\   ")
        print("         ")
    if tries == 3:
        print(tries, ", tries are left")
        print("         ")
        print("         ")
        print("    O    ")
        print("   /|\   ")
        print("   /     ")
    if tries == 2:
        print(tries, ", tries are left")
        print("         ")
        print("         ")
        print("    O    ")
        print("   /|\   ")
        print("   / \   ")
    if tries == 1:
        print(tries, ", tries are left")
        print(" _ _ _ _ ")
        print("        |")
        print("    O   |")
        print("   /|\  |")
        print("   / \  |")
    if tries == 0:
        print(tries, ", tries are left")
        print(":(   You killed the man!!!")
        print(" _ _ _ _ ")
        print("     /  |")
        print("    O   |")
        print("   /|\  |")
        print("   / \  |")

    if tries == 0:
        print("You have lost all your chances, QUITTING THE GAME")
        break
    if guessed_word == word:
        print("You have won the game")
        break

    print(guessed_word + "\n")