# import json

# filename = 'your_file.json'
# lst = [{'alice': 24, 'bob': 27}]
# # Write the initial json object (list of dicts)
# with open(filename, mode='w') as f:
#     json.dump(lst, f)
# # Append the new dict to the list and overwrite whole file
# with open(filename, mode='a') as f:
#     lst.append({'carl':33})
#     json.dump(lst, f)
# f.close()
# with open(filename, mode='a') as f:
#     json.dump([3, 5, 7], f)

for (i, j) in ([1, 2, 3], [4, 5, 7]):
    print(i, j)