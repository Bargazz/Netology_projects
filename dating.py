boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    print('Идеальные пары!')
    boys.sort()
    girls.sort()
    for boy, girl in zip(boys,girls):
        print(boy, 'и', girl)
else:
    print('Количество участников не совпадает!')