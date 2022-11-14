def make_cook_book(file_path='recipes.txt'):
    cook_book = {}
    with open(file_path, 'r', encoding='UTF8') as file:
        for line in file:
            dish = line.strip()
            num_of_ingr = int(file.readline())
            cook_book[dish] = []
            for ingr in range(num_of_ingr):
                ingredient = file.readline().split(' | ')
                all_ingredients = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2].strip()}
                cook_book[dish].append(all_ingredients)
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        for ingredient in make_cook_book()[dish]:
            ingredient_name = ingredient.pop('ingredient_name')
            ingredient['quantity'] = int(ingredient['quantity']) * int(person_count)
            if ingredient_name in shopping_list:
                ingredient['quantity'] += (shopping_list[ingredient_name]['quantity'])
            shopping_list.update({ingredient_name: ingredient})

    view_shopping_list_by_dishes(shopping_list)


def view_shopping_list_by_dishes(shopping_list):
    print("\nДля приготовления этих блюд на данное кол-во персон нам понадобиться:")
    index = 1
    for key, value in shopping_list.items():
        print(f'{index} {key}: {value["quantity"]} {value["measure"]}')
        index += 1
    print("\nЧто-то из ингридиентов можно найти на кухне, остальное придётся докупить.")


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

import os
folder_path = 'Text_3_tasks/'

def files(folder_path: str):
    some_list = os.listdir(folder_path)
    some_dict = {}
    for name in some_list:
        finder = name.rfind('.txt', -4)
        if finder >= 0:
            with open(os.path.join(folder_path, name), 'r', encoding='utf8') as file:
                some_dict[name] = file.readlines()
    with open('new_file.txt', 'w', encoding='utf8') as some_file:
        for filename, rows in sorted(some_dict.items(), key=lambda x: len(x[1])):
            some_file.write(f'{str(filename)}\n')
            some_file.write(f'{str(len(rows))}\n')
            if '\n' not in rows[-1]:
                rows[-1] += '\n\n'
            some_file.write(''.join(rows))
    print('Выполнено')


files(folder_path)


def view_menu():
    for dish, ingridients in make_cook_book().items():
        print(f"\n{dish}:")
        for value in ingridients:
            print(f'     {value["ingredient_name"]} - {value["quantity"]} {value["measure"]}.')

print("Добро пожаловать!!!\n")

command_help = ('Вам необходимо ввести команду, чтобы программа выполнила определённое действие:'
    '\nДоступyные команды: "1", "2", "9" "0"'
    '\n"1" - Показать меню'
    '\n"2" - Список ингридиентов для выбранного блюда на введённое кол-во персон'
    '\n"9" - Помощь по командам'
    '\n"0" - Закрыть программу')
print(command_help)
while True:
    print('\n=====================================================================================\n')
    commands = input('Введите команду: ')

    if commands == "1":
        view_menu()

    elif commands == "2":
        try:
            dish_request = input("Введите через запятую названия блюд с заглавной буквы: ").split(", ")
            persons = input("Введите на какое колличество персон нужно приготовить: ")
            get_shop_list_by_dishes(dish_request, persons)
        except:
            print('Кажется Вы где-то ошиблись с вводом. Перепроверьте и введите заново, но без ошибок =)')

    elif commands == "9":
        print(command_help)

    elif commands == "0":
      print("Всего доброго, Запускайте ещё. Zzz")
      break
