# def remove_every_other(my_list):
#     # a = 0
#     # while a < len(my_list):
#     #     if a % 2 != 0:
#     #         my_list.pop(a)
#     #     a += 1
#     # return my_list
#     res = []

# def cookie(x):
#     if type(x) == str:
#         name = 'Zach'
#         return f"Who ate the last cookie? It was {name}!"
#     elif type(x) == float or type(x) == int:
#         name = 'Monica'
#         return f"Who ate the last cookie? It was {name}!"
#     else:
#         name = 'the dog'
#         return f"Who ate the last cookie? It was {name}!"
#
# print(cookie(56))

"""
Дана сторона квадрата. Нужно посчитать его периметр и площадь
"""
# a = int(input())
# square = a ** 2
# perimetr = a * 4
# print(f'Square = {square}')
# print(f'Perimetr = {perimetr}')

"""
Выяснить является ли год високосным
"""
# year = int(input('Please enter a year: '))
#
# print(f'Високосный {year % 4 == 0}')
"""
Вывести для полученного 4-ёхзначного числа тысячи, сотни, десятки, единицы
"""
# number = (input('Please enter a number: '))
# print(f'Тысячи = {number[-4]}')
# print(f'Сотни = {number[-3]}')
# print(f'Десятки = {number[-2]}')
# print(f'Единицы = {number[-1]}')

"""
Квадратик
"""
# print("""
# * * * * * *
# *         *
# *         *
# * * * * * *
# """)

<<<<<<< HEAD
=======
"""
Write a function to convert a name into initials. 
This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""
def abbrev_name(name):
    first, second = name.upper().split(' ')
    return f'{first[0]}.{second[0]}'

"""
Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> 
["I", "love", "arrays", "they", "are", "my", "favorite"]
"""
def string_to_array(s):
    return s.split(' ')

>>>>>>> f964908 (Initial commit)






