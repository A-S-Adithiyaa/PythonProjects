import string
import random


def generate_random():
    alphabets = string.ascii_letters + '0123456789'
    random_code = random.choice(alphabets)

    return random_code

decoder = {}
final_code = ""
secret_word = input("Enter a word, to be kept secret from all... : ")

for ch in secret_word:
    if ch == " ":
        code = " "
    else:
        code = generate_random()
    decoder[ch] = code
    final_code += code


print(decoder, final_code)