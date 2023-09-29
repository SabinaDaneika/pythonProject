"""
Списки - хранят набор или последовательность элементов, могут хранить разные типы данных,
изменяемая структура данных
"""
# lst = [10, 'Hello', False, None, True, 25, True, 26.5]
# print(lst.count(True))
# lst = [10, 'Hello', False, None, True, 25, True, 26.5]
# print(lst.count(True))
# print(lst.index(True))
# lst2 = [x for x in lst if isinstance(x, int)]
# print(lst2)
# print(len(lst2))
# print(lst)
# print(lst[4])
# print(lst[-2])
"""
Получить длину списка
"""
# print(len(lst))
# print(id(lst))
"""
Добавить элемент к списку
"""
# text = 'Bye'
# lst.append(text)
# print(lst)
"""
Замена элемента
"""
# lst[-2] = 100
# print(lst)
# print(id(lst))
"""
Развернём список
"""
# lst.reverse()
# print(lst)
"""
Чтобы применить методы sum, min, max должны бать элементы в списке одного типа данных
"""
# lst2 = []
# for i in lst:
#     if isinstance(i, int):
#         lst2.append(i)
# print(lst2)
# print(sum(lst2))
# print(min(lst2))
# print(max(lst2))
"""
Генерация списков
"""
# lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3, 4, 5, 6]
# lst2 = []
# for number in lst:
#     if number % 2 == 0:
#         lst2.append(number **2)
# print(lst2)
#
# lst3 = [num * num for num in lst if num % 2 == 0]
# print(lst3)

# lst4 = list(range(10, 50))
# print(lst4)

""" 
Срезы списков - в [] указываем с какого элемента:по какой (НЕ в ключительно):шаг
"""
# lst5 = [3, 7, 'a', None, True, 56.9, 'Hello']
# print(lst5[2:6:2])
# print(lst5[2:7:2])

""" 
Генерация вложенных списков - enumerate
"""
# s1 = 'My name is Sab\nina'
# s1 = 'My name is Sabina'
# lst6 = list(s1.split())
# lst6 = list(s1.split(' '))
# lst6 = list(word for word in s1.split())
# lst6 = [[char for char in word] for word in s1.split()]

# lst6 = [[char for i, char in enumerate(word)] for word in s1.split()]
# lst6 = [[i for i, char in enumerate(word)] for word in s1.split()]
# lst6 = [[i for i, char in enumerate(word)] for word in s1.split()]
# print(lst6)
"""
Вложенные списки
"""
# lst = [5, ['a', 'b', 'c'], 5]
# print(lst[1][1])
"""
Кортежи (Tuples) - неизменяемая структура данных
"""
# my_tuple = 1, 2, 3
# print(type(my_tuple))
# print(my_tuple)

# my_tuple2 = ('lemon', 'mango', 'banana', 'apple', 'cherry')
# print(type(my_tuple2))

# my_tuple2[0] = 'orange'
# lst = list(my_tuple2)
# lst[0] = 'orange'
# my_tuple2 = tuple(lst)
# print(my_tuple2)
# my_tuple3 = ('lemon')
# print(type(my_tuple3))

# def sum_it(*args):
#     return sum(args)
#
# print(sum_it(2, 5, 8, 25))
# print(sum_it(2, 5, 8, 25, 2, 5, 8, 25))

"""
Функции листа
"""
# .append(): adds only one element in a list fruits.append('Grapes')
# .pop() function removes (last) element from a list

# .extend(): adds multiple element in a list fruits.extend(['Grapes', 'kiwi', 'pears'])
# .insert(): adds an element at a particular position using an index fruits.insert(0, 'banana')
# .index(element)

# s1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
# lst = list(s1)
# lst = [word for word in s1.split()][::-1]
# print(lst)

# for i in range(len(lst)):
#     print(lst.pop())
#     print(f'lst - {lst}')

# lst = lst + lst
# print(lst)

# lst.insert(2, 2222)
# print(lst)

# print(lst.index('sit'))
"""
Отсортировать лист
"""
# lst.reverse()
# print(lst)
"""
метод sorted генерирует новый список
"""
# lst1 = sorted(lst)

# print(lst1)

"""
метод sort меняет существующий список in place, не генерируя новый, поэтому возвращает None
"""
# lst3 = lst.sort()
# print(lst3)

# lst = ['lemon', 'mango', 'banana', 'apple', 'cherry']
# lst.sort()
# print(lst)

"""
Словарь
"""
# my_dict2 = {
#     'name': 'Alex',
#     'last_name': 'Smith',
#     'age': 25,
#     'dep': 'DEV'
# }
# my_dict2.setdefault('salary', 5000)
# my_dict2['salary'] = 1000
# x = my_dict2.setdefault('salary', 10000)

# print(my_dict2)
# my_dict2 = {
#     'name': 'Alex',
#     'last_name': 'Smith',
#     'age': 25,
#     'dep': 'DEV'
# }
# my_dict2.setdefault('salary', 5000)
# my_dict2['salary'] = 1000
# x = my_dict2.setdefault('salary', 10000)

# print(my_dict2)
# my_dict2['salary'] = 5000
# print(my_dict2)
# print(my_dict2.pop('salary'))
# print(my_dict2)
# print(my_dict2.get('salary', 'Not found'))
# print(my_dict2['name'])
# print(my_dict2['last_name'])
# my_dict2['dep'] = 'IT'
# print(my_dict2.keys())
# print(my_dict2.values())
# print(my_dict2.items())
# print(len(my_dict2))

# def keywords(**kwargs):
#     return kwargs
#
# print(keywords(name='Alice', last_name='Petrova'))

# def positional(*args):
#     return args
# print(positional('Sabina', 'Daneika'))

"""
Множества (Sets)
"""
# my_list = [1, 2, 5, 8, 10, 12, 10, 12, 'Hello', 'Hello', '', '']
# print(my_list)
# my_unique_list = list(set(my_list))
# print(my_unique_list)

# set1 = {1, 2, 3, 'one', 'ten'}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}
#
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))
# print(set1)
# print(set1.remove(1))
# print(set1)
# print(set1.add(8))
# print(set1)

# fs = frozenset({1, 2, 3})
# print(fs)
# fs.remove(1)
# print(fs)







