# from Lesson2 import power

# number = 10
# print(number)
# print(id(number))
# print(type(number))
#
# number1 = 10
# print(id(number1))
#
# name = 'Bob'
# name1 = name
# print(name1)
# print(name)
# print(type(name))
# print(id(name))
#
# lesson_1 = 'python'
# print(lesson_1)
#
# Name = 'Alice'
# print(name)
#
# for_1 = 10
# print(for_1)
# print(id(for_1))

# pi = 3.14
# print(type(pi))
#
# boolean = True
# print(type(boolean))

# num1 = 5
# num2 = '6'
# print(num2)
# print(id(num2))
# num2 = 6
# print(id(num2))
# num3 = int(num2)
# print(num1+num2)
# print(num1+int(num2))
# print(type(num2))

# name = input('Как вас зовут? ')
# print('Привет, ' + name)
# print(f'Привет, {name}')

# var = None
# print(type(var))

# number = 10
# print(number)
# print(type(number))
#
# num1 = 1.9
# print(num1)
# print(type(num1))

# num2 = int(num1)
# print(num2)

# sum1 = 0.1 + 0.2
# print(sum1)

# a = 6
# b = 7
# print(a == b)
# print(a < b)

# a = 1
# b = 1.8
# c = 'Hello!'
# d = True
# e = [1, 2.6, 'flow']
# f = {1: "str", "err": [1, 2, 3]}
# g = (1, 2 [2, "45"])
# i = {1, 2, 3, '4', 5, [3, "hello"]}

# print(1 + 2)
# print(1 - 2)
# print(1 * 2)
# print(1 / 2)
# print(1 // 2)
# print(2 ** 3)
# print(10 % 3)

# print(abs(-7))
# a = [1, 3, 5, 7, 9]
# print(min(a))
# print(max(a))

# b = pow(2, 3)
# print(b)
#
# a = round(3.49999999)
# print(a)

# a = 3
# a += 1
# a *= 2
# print(a)

# str1 = 'hello'
# str2 = "hello"
#
# a1 = [1, 2, 3, 4]
# b1 = len(a1)
# b2 = sum(a1)
# c1 = b2 / b1
# print(c1)
#
# a2 = "hello   "
# print(len(a2))

# a1 = "Hello"
# a2 = "world"
# a3 = str(10)
# print(f"{a1} {a2}")
# print(a1 + " " + a3)

a1 = "hello"
# print(a1 * 5)
# print('e' in a1)
# print('e' not in a1)
#
# print(a1[0])
# print(a1[1])
# print(a1[0:3])
# print(a1[-1])
# print(a1[0:5:2])
print(a1[::-1])

# s = 'hello,world,asd'
# s1 = 'hello-world-asd'
# # print(s.replace('e', 'a'))
# print(s.split())
# print(s.split(','))
# print(s1.split('-'))

"""
На ввод масса в граммах, выводить только килограммы без остатка
"""
# weight = int(input('Enter weight: '))
# weight //= 1000
# print(weight)

"""
Какое-то кол-во школьников делят какое-то кол-во яблок, 
вывести сколько яблок достанется каждому ребёнку?
"""
# children_num = int(input('Enter number of children: '))
# apple_num = int(input('Enter number of apples: '))
# num_for_one = apple_num // children_num
# print(num_for_one)

"""
К нам поступает какое-то число и нам нужно вывести его последнюю цифру
"""
# number = input('Enter number: ')
# print(number[-1])

# number = int(input('Enter number: '))
# number = number%10
# print(number)

"""
Есть целое число, и нам нужно получить следующее за ним целое число
"""
# number = int(input())
# num_1 = number//2
# num_2 = num_1 * 2 + 2
# print(num_2)

"""
Нам дано время в секундах, нам нужно вывести время в часах, минутах, секундах
Например 2 сек, нам нужно вывести 00:00:02
"""
# sec = int(input())
# hour = sec // 3600 % 24
# minute = sec // 60 % 60
# sec_1 = sec % 60
# print(f'{hour:0>2}:{minute:0>2}:{sec_1:0>2}')

# print(power(3))












