<<<<<<< HEAD
=======
# from functools import reduce
# from math import prod
#import math
# import math as m
# from math import *
# from my_module import sum_it
# import datetime
#
# birth_year = 1994
# current_day = datetime.date.today()
# print(current_day)
# current_age = current_day.year - birth_year
# print(current_age)

# def tests():
    # assert sum_it(5, 8) == 13, f'Wrong number, actual result is {sum_it(5, 8)}'
    # assert sum_it(5, 8) == 15, f'Wrong number, actual result is {sum_it(5, 8)}'

# tests()

# print(sum_it(7, 8))

# l = [1, 2, 5, 7]
# print(prod(l))
# print(math.prod(l))
# print(prod(l))

>>>>>>> f964908 (Initial commit)
"""
Встроенный метод min
"""
# min_item = min(15, 45, 27, 12)
# print(min_item)
#
# def person(age, first_name, last_name):
#     return f'Hello, my name is {first_name} {last_name}. I am {age} years old.'
#
# print(person(29, 'Sabina', 'Daneika'))
# print(person('Sabina', 'Daneika', 29))

# def person(age = 29, first_name = 'Sabina', last_name = 'Daneika'):
#      return f'Hello, my name is {first_name} {last_name}. I am {age} years old.'
#
# print(person(25))


# def person(age, first_name='Sabina', last_name='Daneika'):
#     return f'Hello, my name is {first_name} {last_name}. I am {age} years old.'


# print(person(first_name='Anna', last_name='Ivanova', 25))
# print(person(25, first_name='Anna', last_name='Ivanova'))

def pattern(length, char_1=' ', char_2='*'):
    return (char_2 + char_1) * length + char_1
# print(pattern(9))
# print(pattern(9, char_1='/'))
# print(pattern(char_1='/', 9))
# print(pattern(char_1='/', length=9))

"""
Декораторы
"""
<<<<<<< HEAD
# def decorator_function(func):
#     def wrapper():
#         print('Wrapper function')
#         print(f'Wrapped function: {func.__name__}')
#         print('Wrapped function in process')
#         print(func())
#         print('Exiting wrapper')
#     return wrapper
#
# @decorator_function
# def hello():
#     return 'I\'m wrapped function'
#
# hello()

# def decorator_function(func):
#     def wrapper(*args):
#         print('Wrapper function')
#         print(f'Wrapped function: {func.__name__}')
#         print('Wrapped function in process')
#         print(func(*args))
#         print('Exiting wrapper')
#     return wrapper
#
# @decorator_function
# def hello(item):
#     return f'{item} is wrapped'
#
# hello('Candy')

# def decorator_function(func):
#     def wrapper(*args):
#         print('Wrapper function')
#         print(f'Calling function: {func.__name__}')
#         print(f'With arguments: {args}')
#         print(func(*args))
#         print('Exiting wrapper')
#     return wrapper
#
# @decorator_function
# def hello(item):
#     return f'{item} is wrapped'
#
# hello('Candy')
=======
def decorator_function(func):
    def wrapper():
        print('Wrapper function')
        print(f'Wrapped function: {func.__name__}')
        print('Wrapped function in process')
        print(func())
        print('Exiting wrapper')
    return wrapper

@decorator_function
def hello():
    return 'I\'m wrapped function'

hello()

def decorator_function(func):
    def wrapper(*args):
        print('Wrapper function')
        print(f'Wrapped function: {func.__name__}')
        print('Wrapped function in process')
        print(func(*args))
        print('Exiting wrapper')
    return wrapper

@decorator_function
def hello(item):
    return f'{item} is wrapped'

hello('Candy')

def decorator_function(func):
    def wrapper(*args):
        print('Wrapper function')
        print(f'Calling function: {func.__name__}')
        print(f'With arguments: {args}')
        print(func(*args))
        print('Exiting wrapper')
    return wrapper

@decorator_function
def hello(item):
    return f'{item} is wrapped'

hello('Candy')
>>>>>>> f964908 (Initial commit)

"""
Пространство имён (Namespace):
Built-in - встроенные методы,функции
Global - на уровне основной программы
Enclosed - имена, определённые во внешней функции
Local - имена внутри функции
"""
# x = 15
# y = 25
# def sum_it(x, y):
#     print(f'Locals: {locals()}')
#     return x + y
#
# print(f'Inside the function: {sum_it(10, 18)}')
# print(f'Outside the function: {x + y}')
# print(f'Globals: {globals()}')

# name = 'Nick'
# def outer_function():
#     # name = 'Alex'
#     def inner_function():
#         # name = 'Alice'
#         return name
#     return inner_function()
#
# print(outer_function())
#
# closure = outer_function()
# print(closure)

# result = lambda n: n*n
# print(result(5))

<<<<<<< HEAD
# list_1 = [1, 100, 'Hello', None, 35, True, 76, 19]
=======
# list_1 = [1, 100, 'Hello', 'pizza', 'hi', 'ananas', None, 35, True, 76, 19]
>>>>>>> f964908 (Initial commit)
# new_list = []
# def filter_and_sum(lst):
#     for x in lst:
#         if isinstance(x, int):
#             new_list.append(x)
#     return sum(new_list)
#
# print(filter_and_sum(list_1))

<<<<<<< HEAD
=======
# new_list = sum(filter(lambda x: isinstance(x, int), list_1))
# print(new_list)
# filtered = list(filter(lambda x: isinstance(x, str), list_1))
# print(list(filter(lambda x: 'a' in x, filtered)))

# filtered = list(filter(lambda x: isinstance(x, str) and 'a' in x, list_1))
# print(filtered)

# result = reduce(lambda x, y: x*y, [1, 5, 8, 11, 13])
# print(result)

# result = reduce(lambda x, y: x+y, [1, 5, 8, 11, 13])
# print(result)

# result = list(map(lambda x: x**2, [1, 5, 8, 11, 13]))
# print(result)

# result = list(map(lambda x, y: x**2, [1, 5, 8, 11, 13]))
# print(result)

# lst = [2, 4, 6, 8, 1, 7, 9]
# print(id(lst))
# lst.sort()
# print(lst)
# print(id(lst))
# print(id(sorted(lst)))

# tup = (2, 4, 6, 8, 1, 7, 9)
# tup.sort()
# print(sorted(tup))
# my_set = {2, 4, 6, 8, 1, 7, 9}
# print(sorted(my_set))

my_dict = {1: 'q', 2: 'w', 3: 'z'}

# for keys in my_dict:
#     print(keys)

# for values in my_dict.values():
#     print(values)

# for key, value in my_dict.items():
#     print(f'{key} {value}')

# print(my_dict[1])
# print(my_dict.get(1))
# print(my_dict.get(10))

# b = my_dict.setdefault(1, 'qw')
# print(b)
# b = my_dict.setdefault(10, 'qwe')
# print(b)
# print(my_dict)

"""
**kwargs - именованные значения
*args - неименованные значения
"""
# def sum_1(*args, **kwargs):
#     a = args
#     b = kwargs
#     print(a)
#     print(b)
#
# sum_1([1, 4, 6, 8], a = 4, b = 'Hello', c = True)

# lst = [1, 2, 3, 4]
# for i in lst:
#     print(i, end=' ')
# print()

"""
Распаковка
"""
# print(*lst)

"""
Декораторы
"""
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('before')
#         func(*args, **kwargs)
#         print('after')
#     return wrapper
#
# def decorator_1(func):
#     def wrapper(*args, **kwargs):
#         print('before1')
#         func(*args, **kwargs)
#         print('after1')
#     return wrapper
# @decorator_1
# @decorator
# def run(a, b):
#     c = a + b
#     print(c)
#
# d = decorator(run)
# run(1, 2)
# @decorator
# def run_1(a, b):
#     c = a - b
#     print(c)
#
# run_1(1, 2)

"""
Замыкания - это когда функция вызывает саму же себя
"""
# def factorial(n):
#     if n < 0:
#         return None
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# print(factorial(5))

# def factorial_recursive(n):
#     if n < 0:
#         return None
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial_recursive(n - 1)
#
# print(factorial_recursive(5))

# def is_palindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrom(s[1:-1])
#
# print(is_palindrom('шалаш'))

# def is_palindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrom(s[1:-1])
#
# print(is_palindrom('шалаши'))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(filter(lambda x: x % 2 == 0, numbers)))








>>>>>>> f964908 (Initial commit)






