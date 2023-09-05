"""
Задание 2.1
Напишите программу, которая проверяет здоровье персонажа в игре.
Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
"""
# hp = int(input('Please enter health points: '))
# if hp > 0:
#     print('True')
# else:
#     print('False')
"""
Задание 2.2
Напишите программу, которая проверяет является ли введенное число четным. 
Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
"""
# num = int(input('Please enter a number: '))
# if num % 2 == 0:
#     print('Чётное')
# else:
#     print('Нечётное')

# num = int(input('Please enter a number: '))
# if num % 2 == 0:
#     print('Чётное')
# else:
#     print('Нечётное')

# num = int(input('Please enter a number: '))
# if num % 2:
#     print('Нечётное')
# else:
#     print('Чётное')

"""
Задание 2.3
Напишите программу, которая проверяет является ли год високосным. 
Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и 
не являются столетиями (500, 600). Однако, если год делится без остатка  на 400, 
он также считается високосным (1200, 2000)
"""
# year = int(input('Please enter a year: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Високосный')
# else:
#     print('Невисокосный')

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Високосный')
#         else:
#             print('Невисокосный')
#     else:
#         print('Високосный')
# else:
#     print('Невисокосный')

"""
Задание 2.4
Напишите программу, которая печатает введенный текст заданное количество раз, построчно. 
Текст и количество повторений нужно ввести с помощью input()
"""
# x = input('Enter some text: ')
# y = int(input('Enter repeat value: '))
# i = 0
# while i < y:
#     print(x)
#     i += 1

# for i in range(y):
#     print(x)

"""
Задание 2.5.
Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), 
производит заданное арифметическое действие и печатает результат в формате: 
{num1} {operator) {num2) = {result}
"""
# num1 = int(input('Please enter the first number: '))
# num2 = int(input('Please enter the second number: '))
# operator = input('Please choose one of the following operators: +, -, *, /, %: ')
# result = 0
# result2 = 'Division by zero is impossible'
# if operator == '/' and num2 != 0:
#     result = num1 / num2
# elif operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '%':
#     result = num1 % num2
# else:
#     result = result2
#
# if result == result2:
#     print(result2)
# else:
#     print(f'{num1} {operator} {num2} = {result}')
