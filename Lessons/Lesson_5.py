class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        # self.__age = age
        self._age = age

    def hello(self):
        return f'Hello, my name is {self.name} {self.surname}'

    def walk(self):
        return 'I can walk!'

    def set_name(self, new_name):
        self.name = new_name


person_1 = Person('Sabina', 'Daneika', 29)
# print(person_1.name)
# print(person_1.surname)
# print(person_1.age)
# print(person_1._age)
# print(person_1._Person__age)
# print(f'Attributes: {person_1.__dict__}')
# person_1.name = 'Sabi'
# print(person_1.hello())
# print(person_1.walk())
person_1.set_name('Sasha')
print(person_1.hello())

person_2 = Person('Amelia', 'Daneika', 3)
# print(person_2.name)
# print(person_2.surname)
# print(person_2.hello())
# print(person_2.walk())

class Tester(Person):

    def __init__(self, name, surname, age, framework):
        super().__init__(name, surname, age)
        self.framework = framework

    def test(self):
        return 'I love testing'

tester_1 = Tester('Max', 'Popov', 34, 'pytest')
# print(tester_1.name)
# print(tester_1.surname)
# print(tester_1.framework)
# print(tester_1.hello())

class ManualTester(Tester):

    def __init__(self):
        super().__init__()

