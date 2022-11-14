user_month = input('Введите месяц: ').lower()
user_date = int(input('Введите число: '))

if user_date < 0:
    print('Ошибка')
elif user_date > 31:
    print('Ошибка')
else:
    if user_month == 'март' and 21 >= user_date <= 30 or user_month == 'апрель' and user_date <= 20:
        print('Ваш знак зодиака Овен')
    elif user_month == 'апрель' and 21 >= user_date <= 30 or user_month == 'май' and user_date <= 21:
        print('Ваш знак зодиака Телец')
    elif user_month == 'май' and 22 >= user_date <= 30 or user_month == 'июнь' and 21 <= user_date <= 21:
        print('Ваш знак зодиака Близнецы')
    elif user_month == 'июнь' and 22 >= user_date <= 30 or user_month == 'июль' and 22 <= user_date <= 22:
        print('Ваш знак зодиака Рак')
    elif user_month == 'июль' and 23 >= user_date <= 30 or user_month == 'август' and user_date <= 23:
        print('Ваш знак зодиака Лев')
    elif user_month == 'август' and 24 >= user_date <= 30 or user_month == 'сентябрь' and user_date <= 22:
        print('Ваш знак зодиака Дева')
    elif user_month == 'сентябрь' and 23 >= user_date <= 30 or user_month == 'октябрь' and user_date <= 23:
        print('Ваш знак зодиака Весы')
    elif user_month == 'октябрь' and 24 >= user_date <= 30 or user_month == 'ноябрь' and user_date <= 22:
        print('Ваш знак зодиака Скорпион')
    elif user_month == 'ноябрь' and 23 >= user_date <= 30 or user_month == 'декабрь' and user_date <= 21:
        print('Ваш знак зодиака Стрелец')
    elif user_month == 'декабрь' and 22 >= user_date <= 30 or user_month == 'январь' and user_date <= 20:
        print('Ваш знак зодиака Козерог')
    elif user_month == 'январь' and 21 >= user_date <= 30 or user_month == 'февраль' and user_date <= 18:
        print('Ваш знак зодиака Водолец')
    elif user_month == 'февраль' and 19 >= user_date <= 28 or user_month == 'март' and user_date <= 20:
        print('Ваш знак зодиака Рыбы')
