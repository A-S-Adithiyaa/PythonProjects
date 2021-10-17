'''Program to generate acronyms for long words'''

phrase = input("Enter a phrase : ")

acronym = ""
words = phrase.split()
for word in words:
    acronym += word.upper()[0]

print(acronym)