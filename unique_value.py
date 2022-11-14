ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique_values = []

for item in ids.values():
    for index in item:
        unique_values.append(index)
print(set(unique_values))