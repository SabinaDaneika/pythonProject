"""
Операторы сравнения: ==, >, <
Булевы (логические) операторы: AND, OR, NOT
"""
"""
Условные операторы: if/elif
"""
# num = 5
# if num == 5:
#     print('Five!')
# else:
#     print('Not equal to five')
#
# num = 8
# if num == 5:
#     print('Five!')
# else:
#     print('Not equal to five')

# num = 3
# if num == 5:
#     print('Five!')
# elif num > 5:
#     print('More than five')
# else:
#     print('Less than five')

"""
Цикл WHILE
"""
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
#
# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 5
# while i != 0:
#     print(i)
#     i -= 1

# i = 5
# while i != 0:
#     i -= 1
#     if i == 3:
#         continue
#     print(i)

"""
Цикл FOR
"""
# for i in range(6):
#     print(i)
#
# for i in range(1, 7, 1):
#     print(i)

# for i in range(10, 1, -1):
#     print(i)

"""
Значения, приравниваемые к булевым
"""
# print(bool(0))
# print(bool(''))
# print(bool(None))
# print(bool([]))
# print(bool({}))
# print(bool(0.0))
# print(bool(set()))

# print(bool(8))
# print(bool('G'))

# i = 10
# if i:
#     print('True')
# else:
#     print('False')

# i = 'Hello'
# if i:
#     print('True')
# else:
#     print('Empty')
#
# i = ''
# if i:
#     print('True')
# else:
#     print('Empty')

"""
Функция: def функция(парам1, парам2):
"""
def sum(x, y):
    return x + y

# result = sum(5, 8)
# print(result)
# print(sum(5, 8))

# def power(n):
#     x = sum(5, 8)
#     result = x ** n
#     return result
#
# print(power(2))

"""
Задача 1: Вход в заведение в зависимости от возраста
"""
# age = int(input('Please, enter your age: '))
# if age < 18:
#     print('Go home!')
# else:
#     print('Welcome')

x1 = 10
x2 = 'qwerty'
# for i in range(x1):
#     print(i)
# for i in x2:
#     print(i)

# for i in range(len(x2)):
#     print(i)

"""
Вложенные циклы
"""
# for i in range(len(x2)):
#     for j in x2:
#         print(f"{i} {j}")

# d = {
#     1: 'q',
#     2: 'w',
#     3: 'e'
# }
# for key, value in d.items():
#     print(f'{key} {value}')

# d = [(1, 2), (3, 4), (5, 6)]
# for i, j in d:
#     print(f'{i}, {j}')

# d = [(1, 2), (3, 4), (5, 6)]
# for i, j in d:
#     print(f'{i} {j}')
# for i in d:
#     print(i)

"""
Распаковка картежа
"""
# d = [(1, 2, 3, 56, 678), (3, 4, 5), (5, 6, 7)]
# for i, j, *c in d:
#     print(f'{i} {j} {c}')

"""
Лист - изменяемый объект
"""
# lst = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 'a', 'a', '1']
"""
Картеж - неизменяемый объект
"""
# tup = (1, 2, 3, 4, 5, 5)
"""
Множество - изменяемый неупорядоченный тип данных, содержит только уникальные элементы
"""
# set_1 = {1, 2, 3, 4, 4, 5}
# print(set_1)
# print(set(lst))
# print(set(tup))
"""
Словарь 
"""
# dict_1 = {1: 'q', 2: 'w', 3: 'e'}

# def summa(a, b):
#     print(a + b)
#     c = a + b
#     return c

# print(summa(5, 8))
# summa(3, 5)
# a = summa(3, 5)
# print(a)
# b = a * 10
# print(b)

# x = 10
# def change(x):
#     x = x + 5
#     return x
#
# print(change(x))

# for i in range(10):
#     if i == 5:
#         print(i)
#         break
#     print(i)

# for i in range(-5, 11):
#     if i % 2 == 0:
#         print(i)

"""
Задача 1. С передачи здоровья Анна узнала, что рекомендуется спать а часов в сутки, 
но пересыпать тоже вредно и не стоит спать более b часов. 
Аня сейчас спит n часов в сутки. Если режим сна Ани удовлетворяет передачи, 
то выведите: "Это нормально", Если Аня спит меньше а часов - "Недосып", 
если более b часов - "Пересып"
"""
# a = int(input())
# b = int(input())
# n = int(input())
# a, b, n = int(input()), int(input()), int(input())
# if n > b:
#     print('Пересып')
# elif n < a:
#     print('Недосып')
# else:
#     print('Это нормально')

"""
Задача 2. Ввести все точные квадраты натуральных чисел непревосходящего входного 
натурального числа
"""
# a = int(input())
# b = 1
# while b  2 <= a:
#     print(b  2)
#     b += 1

"""
Задача 3. На вход поступает слово. Нам необходимо воспроизвести процесс, 
в котором каждый раз у этого слова будет пропадать первая и последняя буква. 
Остановить процесс необходимо, когда останется одна буква либо пустая строка
"""
# word = input('Please enter a word: ')
# while len(word) >= 1:
#     print(word)
#     word = word[1:-1]

"""
Задача 4. Программа, которая считывает два натуральных числа (a, b), 
при этом а всегда меньше b. После чего для всех чисел от a до b включительно выводят физ: 
Если число делится на 3, буз - если делится на 5, физбуз - если и на 3 и на 5. 
Если никакие из условий не выполняются, то вывести число как оно есть
"""
# a = int(input())
# b = int(input())
#
# for i in range(a, b+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

"""
Задача 5. Нужно посчитать процент содержания в строке значений Г и Ц вместе
"""
# string = 'acggtgttat'
# count = 0
# for i in string:
#     if i.lower() in 'gc':
#         count += 1
# print(str(count/len(string) * 100) + ' %')
# print(f'{count/len(string)*100:.0f} %')

"""
Задача 6. 
"""









