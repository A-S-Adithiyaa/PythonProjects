''' Python program for the game "MAD-LIB" '''

questions = ['''Today I went to the zoo. I saw a(an) _ jumping up and down in its tree. He _ through the large tunnel that led to its _. I got some peanuts and passed them through the cage to a gigantic gray _ towering above my head. Feeding that animal made me hungry. I went to get a _ of ice cream. It filled my stomach. Afterwards I had to _ to catch our bus. When I got home, I _ my mom for a _ at the zoo. ''']

another_question = True

while another_question:
	entered_words = []
	entered_para = ""

	for question in questions:
		unknowns = 0
		for ch in question:
			if ch == '_':
				unknowns += 1

	print("Enter", unknowns, "number of words: ")

	for i in range(unknowns):
		entered_word = input("Enter a word: ")
		entered_words.append(entered_word)

	i = 0

	for ch in question:
		if ch == '_':
			entered_para += entered_words[i]
			i += 1
		else:
			entered_para += ch

	questions.remove(question)

	print(entered_words)
	print(entered_para)

	another_question = input('Want to try again? (y/n)')

	if another_question.lower() == 'y':
		another_question = True
	elif another_question.lower() == 'n':
		another_question = False

'''
def add_question(q):
	question = ""
	words = q.split()
	for word in words:
		#print(len(word))
		if word.count("_") == len(word):
			print(word.count("_"))
			print(len(word))
			question += ""
		if word[0] == "(":
			question += ""
		else:
			question += word + " "

	questions.append(question)

add_question('''''')
'''