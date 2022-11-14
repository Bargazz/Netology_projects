side_sq_length = int(input('Введите длину стороны квадрата: '))
perimeter_sq = side_sq_length*4
square_of_sq = side_sq_length**2
print()
print('Вывод:')
print(f'Периметр: {perimeter_sq}')
print(f'Площадь: {square_of_sq}')
print()
length_of_rect = int(input('Введите длину прямоугольника: '))
width_of_rect = int(input('Введите ширину прямоугольника: '))
per_of_rect = length_of_rect*2 + width_of_rect*2
sq_of_rect = length_of_rect*width_of_rect
print()
print('Вывод')
print(f'Периметр: {perimeter_sq}')
print(f'Площадь: {sq_of_rect}')
print()
divider_symbol = input('Введите символ: ')
divider = (perimeter_sq+sq_of_rect)*divider_symbol
print(divider_symbol)
print('Вывод:')
print(divider)

month_salary = int(input('Введите заработную плату в месяц: '))
percent_of_mortgage = int(input('Введите, какой процент(%) уходит на ипотеку: '))
percent_of_life = int(input('Введите, какой процент(%) уходит на жизнь: '))
year_of_mortgage = (month_salary*12)/100*percent_of_mortgage
year_savings = (month_salary*12)/100*percent_of_life- year_of_mortgage
print('Вывод')
print(f'На ипотеку было потрачено: {year_of_mortgage}')
print(f'Было накоплено: {year_savings}')