import random
from test import GeneratePaths

directions = ['l', 'r', 's', 'b']
sucessful_paths = GeneratePaths.generate_paths()

i = stop = 0

print(sucessful_paths)

path_states = {}
path_states[i] = sucessful_paths
while True:
    shorted_paths = []
    move = input("Make a move: ")
    for lst in sucessful_paths:
        if lst[i] == move:
            shorted_paths.append(lst)

    if len(shorted_paths) in [0, 1]:
        break
    i += 1
    sucessful_paths = shorted_paths
    path_states[i] = sucessful_paths

sucessful_paths = shorted_paths
path_states[i] = sucessful_paths

