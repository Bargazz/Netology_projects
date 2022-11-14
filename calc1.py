interest_rate = 10
user_region = input('Введите ваш регион: ')
if user_region == 'Дальний Восток':
    interest_rate = 2
    print(f'Ваша процентная ставка: {interest_rate}%')
else:

    user_kids_count = int(input('Сколько у вас детей?: '))
    user_paid_project = input('У вас есть зарплатный проект?: ').lower()
    user_insurance = input('У вас есть страховка?: ').lower()

    if user_kids_count > 3:
        interest_rate -= 1

    if user_paid_project == 'да':
        interest_rate -= 0.5

    if user_insurance == 'да':
        interest_rate -= 1.5

    print(f'Ваша процентрая ставка: {interest_rate}%')
