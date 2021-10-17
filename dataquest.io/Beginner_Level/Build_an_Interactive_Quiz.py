import json


questions = ["You regularly make new friends", "You spend a lot of your free time exploring various random topics that pique your interest", "Seeing other people cry can easily make you feel like you want to cry too", "You often make a backup plan for a backup plan", "You usually stay calm, even under a lot of pressure", "At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know", "You are more inclined to follow your head than your heart", "You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine", "You rarely worry about whether you make a good impression on people you meet", "You enjoy participating in group activities", "You like books and movies that make you come up with your own interpretation of the ending", "Your happiness comes more from helping others accomplish things than your own accomplishments", "You are interested in so many things that you find it difficult to choose what to try next", "You are prone to worrying that things will take a turn for the worse", "You avoid leadership roles in group settings", "You are definitely not an artistic type of person", "You think the world would be a better place if people relied more on rationality and less on their feelings", "You prefer to do your chores before allowing yourself to relax"]

answers = json.load(open('PersoTestData.json'))

# answers = {}
# for i in range(len(questions)):
#     answers['q'+str(i+1)] = []
# j = json.dumps(answers)
# with open('PersoTestData.json', 'w') as f:
#         f.write(j)
#         f.close()
def check_perso():
    percent_score = 0

    input("Answer the below questions on a scale of 1-5.\nAnswer to all the questions promptly, without thinking about it twice. \n\tHit ENTER to continue.")

    name = input("Enter your name : ")
    for i in range(len(questions)):
        answer = input(questions[i] + " : ")
        while True:
            if answer == "" or (not(0 <= int(answer) <= 5)):
                print("Enter a number between 0 and 5, both inclusive.")
                answer = input(questions[i] + " : ")
            else:
                break

        mean_others_answers = sum(answers['q' + str(i+1)]) / len(answers['q' + str(i+1)])
        percent_score += abs((mean_others_answers - int(answer)) * 100 / mean_others_answers)

        answers['q' + str(i+1)].append(int(answer))

    j = json.dumps(answers)
    with open('PersoTestData.json', 'w') as f:
        f.write(j)
        f.close()
    
    percent_score = percent_score / len(questions)
    print(percent_score)

check_perso()

