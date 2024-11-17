# # Задание 4
# # Создайте класс «Дробь». Необходимо хранить в полях
# # класса: числитель и знаменатель. Реализуйте методы класса
# # для ввода данных, вывода данных, реализуйте доступ к
# # отдельным полям через методы класса. Также создайте
# # методы класса для выполнения арифметических операций
# # (сложение, вычитание, умножение, деление, и т.д.).
#
# from __future__ import annotations
#
#
# class Fraction:
#     def __init__(self, numerator: int, denominator: int, int_part: int = 0):
#         self.__num: int = numerator + int_part * denominator
#         self.__den: int = denominator
#
#     # @property
#     # def num(self) -> int:
#     # 	return self.__num
#     #
#     # @num.setter
#     # def num(self, value):
#     # 	if type(value) == int:
#     # 		self.__num = value
#
#     def add(self, fraction: Fraction) -> Fraction:
#         num = self.__num * fraction.__den + fraction.__num * self.__den
#         den = self.__den * fraction.__den
#         return Fraction(num, den)
#
#     def multiply(self, fraction: Fraction) -> Fraction:
#         num = self.__num * fraction.__num
#         den = self.__den * fraction.__den
#         return Fraction(num, den)
#
#     def subtraction(self, fraction: Fraction) -> Fraction:
#         num = self.__num * fraction.__den - fraction.__num * self.__den
#         den = self.__den * fraction.__den
#         return Fraction(num, den)
#
#     def __str__(self) -> str:
#         num = self.__num
#
#         if self.__num > self.__den:
#             int_part = int(self.__num / self.__den)
#             num -= int_part * self.__den
#             return f'{int_part} ({num}/{self.__den})'
#         elif self.__num == self.__den:
#             return str(int(self.__num / self.__den))
#
#         return f'{self.__num}/{self.__den}'
#
#     def __float__(self):
#         return self.__num / self.__den
#
#
# # f1 = Fraction(2, 3, int_part=3)
# f2 = Fraction(523, 213)
# #
# # f3: Fraction = f1.add(f2)
# # f4: Fraction = f3.add(f1)
#
# print(f2)
# # print(f.get_num())
import math

# Задание 1
# Создайте класс Число (или используйте уже ранее
# созданный вами). Класс число хранит внутри одно
# значение. Используя перегрузку операторов реализуйте
# для него арифметические операции для работы с числом
# (операции +, -, *, /).

# from __future__ import annotations
#
#
# class Number:
#     def __init__(self, value: int | float):
#         self.__value: int | float = value
#
#     def __str__(self) -> str:
#         return str(self.__value)
#
#     def __add__(self, other: Number) -> Number:
#         return Number(self.__value + other.__value)
#
#     def __sub__(self, other: Number) -> Number:
#         return Number(self.__value - other.__value)
#
#     def __mul__(self, other: Number) -> Number:
#         return Number(self.__value * other.__value)
#
#     def __truediv__(self, other: Number) -> Number:
#         return Number(self.__value / other.__value)
#
#
# a = Number(5)
# b = Number(2)
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# from __future__ import annotations
# from abc import abstractmethod, ABC
#
#
# class pet:
#     def __init__(self, name: str, age: int, breed: str):
#         self._name: str = name
#         self._age: int = age
#         self._animal_type: str = breed
#
#     @abstractmethod
#     def sound(self):
#         raise NotImplementedError('Метод sound должен быть определен')
#
#     @abstractmethod
#     def about(self):
#         raise NotImplementedError('Метод about должен быть определен')
#
#     @abstractmethod
#     def breed(self):
#         raise NotImplementedError('Метод breed должен быть определен')
#
#
# class dog(pet, ABC):
#     def sound(self):
#         print('gav')
#
#     def about(self):
#         print(f'My name is {self._name}')
#
#     def breed(self):
#         print(f'My name is {self._name}')
#
#
# class cat:
#     pass
#
#
# class hamster:
#     pass
#
#
# class parrot:
#     pass

# class Book:
#     def __init__(self, title: str, author: str, year: str):
#         self.title: str = title
#         self.author: str = author
#         self.year: str = year
#
#     def get_info(self):
#         print(self)
#
#     def edit_year(self):
#         self.year = int(input("Enter year: "))
#         return self.year
#
#     def __str__(self):
#         return f'{self.title}, {self.author}, {self.year}'
#
#
# book1 = Book('Python', '<NAME>', '1999')
# book1.get_info()
# book1.edit_year()
# print(book1)

# class Person:
#     def __init__(self, name: str, age: int):
#         self.name: str = name
#         self.age: int = age
#
#
# class Student(Person):
#     def __init__(self, name: str, age: int, institute: str, score: float):
#         super().__init__(name, age)
#         self.institute: str = institute
#         self.score: float = score
#
#     def __str__(self):
#         return f'{self.name}, {self.age}, {self.institute}, {self.score}'
#
#
# f = Student('slava', 20, 'Computer Science', 80)
# print(f)

from abc import abstractmethod, ABC

#
#
# class Figure:
#     @abstractmethod
#     def get_area(self) -> float:
#         raise NotImplementedError('Method get_area is not implemented')
#
#
# class Rectangle(Figure):
#     def __init__(self, width: int, height: int):
#         self.width: int = width
#         self.height: int = height
#
#
# class Circle(Figure):
#     def __init__(self, radius: float):
#         self.radius: float = radius
#
#     def get_area(self) -> float:
#         return math.pi * (self.radius * self.radius)
#
#
# f1 = Rectangle(5, 5)
# f2 = Circle(5)
#
#
# print(f2.get_area())


# def divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         return "Division by zero"
#
#
# print(divide(5, 0))


# def error_input():
#     while True:
#         try:
#             return int(input())
#         except ValueError:
#             print("Please enter a number")
#
# error_input()


# f = lambda value, value1: value + value1
# print(f(1, 2))

# a = int(input("Enter a number: "))
# b = print('+') if a > 0 else print('-')

# a = int(input("Enter a number: "))
# b = 'Четное' if a % 2 == 0 else 'Нечетное'
#
# print(b)


# arr = ('sfa', 'fasges', 'fasgsgsd')
# b = [len(i) for i in arr]
#
# print(b)

a = [c**2 for c in range(11) if c % 2 == 0]
print(a)

