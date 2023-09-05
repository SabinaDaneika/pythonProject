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

# list_1 = [1, 100, 'Hello', None, 35, True, 76, 19]
# new_list = []
# def filter_and_sum(lst):
#     for x in lst:
#         if isinstance(x, int):
#             new_list.append(x)
#     return sum(new_list)
#
# print(filter_and_sum(list_1))







