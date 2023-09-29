"""
3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd'].
Распечатайте значения 1, 2, 3
"""

# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])
# print(*my_list[2], sep='\n')

"""
3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'
"""

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# list_2 = []
# for i in list_1:
#     if isinstance(i, int):
#         list_2.append(i)
# print(sum(list_2))

# sum = 0
# for i in list_1:
#     if isinstance(i, int):
#         sum += i
# print(sum)

# print(sum([x for x in list_1 if isinstance(x, int)]))

# list_3 = []
# for i in list_1:
#     if isinstance(i, str):
#         list_3.append(i)
#
# for i in list_3:
#     if 'a' in i:
#         print(i)

# print(*[x for x in list_1 if isinstance(x, str) and 'a' in x], sep = ', ')

"""
3.3 Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
"""

# list_4 = ['cat', 'dog', 'horse', 'cow']
# my_tuple = tuple(list_4)
# print(my_tuple)

"""
3.4 Напишите программу, которая определяет, какая семья больше. 
      1) Программа имеет два input() - например, family_1, family_2. 
      2) Членов семьи нужно перечислить через запятую. 
     Ожидаемый результат - программа выводит семью с бОльшим составом. 
     Если состав одинаковый, print("Equal')
"""

# family_1 = [item for item in input('Please enter the members of the first family: ').split(',')]
# print(family_1)
# family_2 = [item for item in input('Please enter the members of the second family: ').split(',')]
# print(family_2)

# family_1 = input('Please enter the members of the first family: ')
# family_1_num = family_1.split(',')
# family_2 = input('Please enter the members of the second family: ')
# family_2_num = family_2.split(',')
#
# if len(family_1_num) > len(family_2_num):
#     print(family_1)
# elif len(family_2_num) == len(family_1_num):
# family_1 = (tuple(input('Please enter the members of the first family: ').split(',')))
# family_2 = (tuple(input('Please enter the members of the second family: ').split(',')))
#
# if len(family_1) > len(family_2):
#     print(family_1)
# elif len(family_2) == len(family_1):
#     print('Equal')
# else:
#     print(family_2)

"""
3.5 Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение
"""
# film = {
#     'title': 'Titanic',
#     'director': 'James Francis Cameron',
#     'year': '1997',
#     'budget': '218 billion dollars',
#     'main_actor': 'Leonardo DiCaprio',
#     'slogan': 'Nothing on Earth can separate them'
# }
# print(film.keys())
# print(film.values())
# print(film.items())
"""
3.6 Найдите сумму всех значений в словаре my_dictionary = 
{'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
"""
# my_dictionary = {
#     'num1': 375,
#     'num2': 567,
#     'num3': -37,
#     'num4': 21
# }
# print(sum(my_dictionary.values()))
"""
3.7 Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
"""
# my_list = [1, 2, 3, 4, 5, 3, 2, 1]
# my_new_list = list(set(my_list))
# print(my_new_list)
"""
3.9 Даны два множества: 
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, 
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга 
"""
# set_1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set_2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

# print(set_1 & set_2)
# print(set_2.intersection(set_1))

# print(set_1 ^ set_2)
#
# print(set_2.difference(set_1))
# print(set_1.difference(set_2))

# print(set_1.issubset(set_2))
# print(set_1.symmetric_difference(set_2))

# print(set_1.issubset(set_2))
# print(set_2.issubset(set_1))

# seq = list('абвгде')
# for i, val in enumerate(seq, 1):
#     print(f'№ {i} => {val}')

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
# print('www.example.com'.lstrip('w.'))











