documents = [
{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
	'1': ['2207 876234', '11-2', '5455 028765'],
	'2': ['10006'],
	'3': []
}


def number_and_name(number, document):
    for dictionary in document:
        if dictionary['number'] == number:
            return print(f"Докумет под номером {dictionary['number']}, принадлежит: {dictionary['name']}")
    return print('Ошибка')

# number_and_name('2207 876234', documents)

def shelf_and_num(num, shelf):
    for key, value in shelf.items():
        for item in value:
            if item == num:
                return print(f'Документ {item} находится на {key} полке')
    return print('Ошибка')


# shelf_and_num('10006', directories)

def doc_list(names):
    print('Все документы:')
    for name in names:
        print(*name.values())



# doc_list(documents)

def add_to_dict(types, numbers, names, shelfs, lists, dicts):
    if shelfs not in dicts:
        return print('Ошибка')
    added_docs = {"type": types.capitalize(), "number": numbers, "name": names.capitalize()}
    lists.append(added_docs)
    dicts[shelfs].append(numbers)
    return print('Документ добавлен')


# add_to_dict('passport', '10', 'name none', '3', documents, directories)



while True:
    ask_command = input('Введите команду: ')
    if ask_command == 'p':
        number = input('Номер документа?: ')
        number_and_name(number, documents)
    elif ask_command == 's':
        ask_number = input('Номер документа?: ')
        shelf_and_num(ask_number, directories)
    elif ask_command == 'l':
        doc_list(documents)
    elif ask_command == 'a':
        types = input('Тип документа: ')
        numbers = input('Номер документа: ')
        names = input('Фамилия, имя: ')
        shelfs = input('Номер полки: ')
        add_to_dict(types, numbers, names, shelfs, documents, directories)
        print(documents)
        print(directories)
    elif ask_command == 'e':
        break
    else:
        print('Ошибка')