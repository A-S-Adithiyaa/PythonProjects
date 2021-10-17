cards = ['09H', '04C', '12H', '07H', '04S', '09S', '03S', '04D', '06C', '11S', '07D', '12C', '12S']


def check_trial(cards):
    """Function that checks for trial possibilities in a random set of 13 cards"""

    numbers = [card[:2] for card in cards]
    trials = list(set([number for number in numbers if numbers.count(number) == 3]))

    # print(numbers, trials)
    return trials

cards_atc = [card for card in cards if card[0:2] not in check_trial(cards)]


def check_sequence(cards):
    # numbers = [int(card[0:2]) for card in cards]
    numbers = [5, 6, 7, 7, 9, 9, 11]
    # numbers.sort()

    print(numbers)

    sequence = []
    for i in range(len(numbers) - 1,  1, -1):
        if numbers[i] - numbers[i-1] == numbers[i-1] - numbers[i-2] == numbers[i-2] - numbers[i-3]
            sequence.append(numbers[i])
            numbers
            

check_sequence(cards_atc)

from random import sample


cards = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD']

print(sample(cards, 13))