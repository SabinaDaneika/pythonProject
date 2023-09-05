import time
from math import sqrt
from functools import reduce
from my_calc import *
"""
4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую
     3 значения (с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата.
"""
# a = int(input('Enter the square side: '))
# print(a*a, a*4, round(a*(2**0.5)))
# def square(a):
#     lst = []
#     perimetr = a * 4
#     lst.append(perimetr)
#     sq = a **2
#     lst.append(sq)
#     diagonal = float(sqrt(a**2 + a**2))
#     lst.append(diagonal)
#     return tuple(lst)
#
# print(square(2))

"""
4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов 
     и выводит их построчно 
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35 
	position: web developer
"""
# my_dict = {'name': 'John',
#            'last_name': 'Smith',
#            'age': 35,
#            'position': 'web developer'}
# print(my_dict)

# def dictionary(**kwargs):
#     print(*kwargs.items(), sep = '\n')
#
# dictionary(name='John', last_name='Smith', age=35, position='web developer')

"""
4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] 
     создайте новый список, содержащий только 
     положительные числа
"""
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x >= 0, my_list))
# print(new_list)

"""
4.4. Используя лямбда выражение, получите результат перемножения значений 
     в предыдущем списке 
"""
# print(reduce(lambda x, y: x * y, my_list))

"""
4.5. Напишите декоратор, который высчитывает время работы функции, 
     которую он принимает в качестве параметра
"""
# def decorator_function(func):
#     def wrapper(*args):
#         start = time.perf_counter()
#         print(start)
#         func(*args)
#         end = time.perf_counter()
#         print(end)
#         final = end - start
#         print(final)
#     return wrapper
#
# def decorator_function_2(func):
#     def wrapper(*args):
#         print('Hello')
#         func(*args)
#         print('Bye')
#     return wrapper
#
# @decorator_function
# @decorator_function_2
# def say_Hello(*args):
#     print(f'Hello, {args}')
#
# say_Hello('Sabina')

"""
4.6 Создайте файл my_calc.py и пропишите в нем минимум 4 функции, 
    выполняющие базовые арифметические вычисления. 
    Примените эти функции в качестве методов в другом файле.
"""
print(sum(4,5))
print(sub(6,3))
print(multiply(4,5))
print(divide(20,5))