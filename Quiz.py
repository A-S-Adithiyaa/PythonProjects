import random


score = 0
questions_with_answers = {
    "what is the favourite colour in the world?" : 'green',
    "what is the fastest animal on earth?" : 'cheetah',
    "what is the fastest bird on earth?" : 'falcon',
    "which is the largest animal on earth?" : 'blue whale',
}

print("Enter 'q' to quit the game")
for question in questions_with_answers.keys():
    answer = input(question.capitalize() + " : ")
    if answer == 'q':
        break
    else:
        if answer == questions_with_answers[question]:
            score += 1

print("Your final score is, ", score)