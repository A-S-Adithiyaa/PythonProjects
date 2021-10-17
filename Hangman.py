import random


dict_of_words = {
    'heuristic' : 'Any approach to problem solving, learning, or discovery that employs a practical method, not guaranteed to be perfect, but instead sufficient for reaching an immediate goal.',
    'algorithm' : 'In mathematics and computer science, it is an unambiguous specification of a design or how to solve a problem.',
    'template' : 'Something that establishes or serves as a pattern.',
    'abruptly' : 'Suddenly and unexpectedly.',
    'hyphen' : 'Used to separate the parts of some compound words, to link the words of a phrase, and between syllables of a word split between two consecutive lines of writing or printing.',
    'vortex' : 'A whirling mass of fluid or air, especially a whirlpool or whirlwind.'
}

words_guessed = []

# def check_guess_correct(guess, word):
#     if guess in word:
#         return True
#     else:
#         return False


# def generate_random():
#     word_index = random.randint(1, len(dict_of_words))
#     word = dict_of_words(word_index)
#     if word not in words_guessed:
#         return word
#     else:
#         generate_random()

# stop_game =  0
# while not stop_game:
#     word = generate_random()
#     print(word)
#     stop_game = int(input)

print(len(dict_of_words))
print(dict_of_words.values()[2])