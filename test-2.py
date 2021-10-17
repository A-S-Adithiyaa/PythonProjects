import pandas as pd
# cards = ['09H', '04C', '12H', '07H', '04S', '09S', '03S', '04D', '06C', '11S', '07D', '12C', '12S']

# numbers = [int(card[:2]) for card in cards]
# numbers.sort()


# for 
# print(numbers)

import numpy as np


lst = ['a', 'b', 'a']
l = []

for i in range(1, 4):
    splited = np.array_split(lst, i)
    l.extend(splited)

for array in splited:
    array.append(3)

lis = {1:"ewf"}

lis.extend([3, 6])

