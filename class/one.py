# 1 - همه چیز در پایتون یک شی است
# 2 - هر شی حداقل باید نمونه ای از یک کلاس باشد
# 3 - یک متغیر ، یک ارجاع به شی است
# 4 - هر کلاس خود یک شی از کلاس "type" است و همه کلاس ها از کلاسی با نام  object ارث بری میکنند.
# 5 - در ساختار جدید پایتون ، مفهوم کلاس برابر با مفهوم type  در نظر گرفته شده است .




# mypy ---------> for type hints !!!!

# x = 4
# print(id(x))
# y = 4
# print(id(y))
# print(dir(y))
# print(x.__pow__(y))
# print(x.__mul__(y))
# print(x.__add__(y))

# # <object>.<attributes> = <value>

# class point():
#     def reset(self):
#         self.x = 0
#         self.y = 0

# o = point()
# k = point()

# o.x = 656
# o.y = 188.5
# print(7 * '*' , ' o ', 7 * '*')
# print(o.y)
# print(o.x)

# o.reset()

# print(7 * '*' , ' o ', 7 * '*')
# print(o.y)
# print(o.x)


# =========================================
from math import hypot
import inspect
import doctest

class point:


    """
    >>> p1 = point()
    >>> p2 = point(3,4)
    >>> p1.distance(p2)
    5
    """
    
    # method
    # attribute --> default/Non default

    def __init__(self, x:float = 0, y:float = 0) -> None:
        self.move(x, y)
    
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def distance(self, other:'point') -> float: 
        return hypot(self.x - other.x, self.y - other.y)
    
doctest.testmod()
    
print(inspect.getsource(point))
print(point.__bases__)
p1 = point()
p2 = point()


p1.move(1,7)
p2.move(8,9)

print(p1.x)
print(p1.y)
print(p1.distance(p2))

# =====================================
# __new__ ==> create
# ___init__ ==> initialize

p3 = point()
print(p3.x)
print(p3.y)
#==================================
# class Car:
#     def __init__(self,model, year):
#         self.model = model
#         self.year = year
#
#     def describe(self):
#         print(f'model: {self.model}, year: {self.year}')
#
#
# car=Car('Ford','1990')
# car.describe()
import argparse
# from curses.ascii import isdigit
from idlelib.autocomplete import completion_kwds
from operator import index
from symtable import Class


# class Book:
#     def __init__(self,title):
#         self.title = title
#
#     def show_title(self):
#         print(self.title)
#
#     def change_title(self,new_title):
#         self.title = new_title
#
# book1 = Book('48 laws of power')
# book2 = Book('doom')
# book1.show_title()
# book1.change_title('new title')
# book1.show_title()
# book2.show_title()



# class Student:
#     school = 'high school'
#     def __init__(self,name):
#         self.name=name
#
#     def school_name(self):
#         print(f'{self.name} {Student.school}')
#
#
# student1 = Student('Mahdi')
# student2 = Student('taha')
#
# student2.school_name()
# Student.school = 'navab'
#
# student1.school_name()



# class Book:
#     language = 'english'
#     def __init__(self, title):
#         self.title = title
#
#     def show(self):
#         print(f'lang = {self.language} , title = {self.title}')
#
#
#
# x1 = Book('taha')
# x1 = Book('mahdi')
# x1.show()
# Book.language = 'persian'
# x1.show()



# class Counter:
#     count = 0
#
#     def __init__(self):
#         Counter.increment_count()
#
#     @classmethod
#     def increment_count(cls):
#         cls.count += 1
#     @staticmethod
#     def show_count ():
#         print(f'count: {Counter.count}')
#
#
# cr1 = Counter()
# Counter.show_count()
# cr2 = Counter()
# cr2.show_count()



# class Student:
#     counter = 0
#     def __init__(self):
#         Student.up()
#
#     @classmethod
#     def up(cls):
#         cls.counter += 1
#
#     def show(self):
#         print(f'students: {self.counter}')
#
#     @staticmethod
#     def stat():
#         print('students are great')
#
#
# x1 = Student()
# x1.show()
# x2= Student()
# x2.show()
# x1.stat()





# class Calculator:
#
#     @staticmethod
#     def plus(a,b):
#         print(a+b)
#
#     @staticmethod
#     def minus(a,b):
#         print(a-b)
#
#     @staticmethod
#     def multiply(a,b):
#         print(a*b)
#
#     @staticmethod
#     def divide(a,b):
#         print(a/b)


# Calculator.plus(2,8)
# Calculator.minus(2,8)
# Calculator.multiply(2,8)
# Calculator.divide(2,8)






# class Employee:
#
#     company_name = 'doxa group'
#
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(f'{self.name} {Employee.company_name}')
#
#     @classmethod
#     def change_company(cls, new_name):
#         cls.company_name = new_name
#
#
# x = Employee('mahdi')
# x.show()
# x.change_company('nabavi')
# x.show()


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):
#         print("Hello " + self.name)
#
#
# class Student(Person):
#     def study(self):
#         print(f"{self.name} is studying")
#
#
# op = Person("Mahdi")
# op.introduce()
# st = Student("taha")
# st.study()
# st.introduce()




# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):
#         print("Hello " + self.name)
#
#
# class Teacher(Person):
#     def introduce(self):
#         print(f'im {self.name}')
#
# tt = Teacher('John')
# tt.introduce()
#
# pp = Person('John')
# pp.introduce()


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):
#         print(f"My name is {self.name}")
#
#
# class Teacher(Person):
#     def introduce(self):
#         super().introduce()
#         print("I'm a teacher.")
#
#
# t = Teacher("Mahdi")
# t.introduce()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#
# st = Student("John", 24, 22)
# print(st.name)
# print(st.age)
# print(st.student_id)



# class Person:
#     def __init__(self, name, age):
#         print('person called')
#         self.name = name
#         self.age = age
#
#
# class Student(Person):
#     def __init__(self, name, age, score):
#         super().__init__(name, age)
#         self.score = score
#
#
# st = Student('John', 24, 80)
# print(st.name)
# print(st.age)
# print(st.score)


# x = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
# y = ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ک', 'گ', 'ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'ئ', 'و']




# class Animal:
#     def __init__(self, species ):
#         self.species = species
#         print('animal created')
#
# class Pet(Animal):
#     def __init__(self, name, species ):
#         super().__init__(species)
#         self.name = name
#         print('pet created')
# class Dog(Pet):
#     def __init__(self, name, species,breed ):
#         super().__init__(name, species)
#         self.breed = breed
#         print('dog created')
#
# d = Dog("jacki",'d','GERMAN')
#
#
# print(d.name)
# print(d.breed)
# print(d.species)



# class Speaker:
#     @staticmethod
#     def speak():
#         print('i can speak')
#
# class Walker:
#     @staticmethod
#     def walk():
#         print('i can walk')
#
#
# class Human(Speaker, Walker):
#     pass
#
# st = Human()
# st.walk()
# st.speak()
#
# class x:
#     def test(self):
#         pass
# class y:
#     def test(self):
#         pass
# class z:
#     def test(self):
#         pass
# class child(x,y,z):
#     def test(self):
#         pass
#
# print(child.mro())



# class A:
#     def action(self):
#         print("A")
#
# class B(A):
#     def action(self):
#         print("B")
#         super().action()
#
# class C(A):
#     def action(self):
#         print("C")
#         super().action()
#
# class D(B, C):
#     def action(self):
#         print("D")
#         super().action()
#
# obj = D()
# obj.action()


# class A:
#     def __init__(self):
#         print('a')
#         super().__init__()
#
# class B(A):
#     def __init__(self):
#         print('b')
#         super().__init__()
#
# class C(A):
#     def __init__(self):
#         print('c')
#         super().__init__()
#
# class D(B,C):
#     def __init__(self):
#         print('d')
#         super().__init__()
#
#
#
# g = D()
# print(g)


# class BankAccount:
#     def __init__(self):
#        self.__balance = 0
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def withdraw(self, amount):
#         self.__balance -= amount
#
#     def show(self):
#         print("your balance is:", self.__balance)
#
#
#
# b = BankAccount()
# b.deposit(100)
# b.withdraw(70)
# b.show()


# class Student:
#     def __init__(self,score):
#         self.__score = score
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self,num):
#         if 0 <= num <= 20:
#             self.__score = num
#         else:
#             print("score must be between 0 and 20")
#
#
# x1 = Student(10)
# x2 = Student(1)
#
# print(x1.score)
#
#
# x1.score = 15
# print(x1.score)


# class Car:
#     @staticmethod
#     def drive():
#         print("Driving car")
#
#
# class Motor:
#     @staticmethod
#     def drive():
#         print("Driving motor")
#
# class bike:
#     @staticmethod
#     def drive():
#         print("Driving bike")
#
#
#
# def ma(x):
#     x.drive()
#
# ma(Motor)
# ma(Car)
# ma(bike)



# class Animal:
#     def sound(self):
#         print("Some animal sound")
#
# class Bird(Animal):
#     def sound(self):
#         print("Bird sound")
# class Fish(Animal):
#     def sound(self):
#         print("Fish sound")
# def make_sound(animal):
#     animal.sound()
#
# make_sound(Bird())
# make_sound(Fish())





# class Animal:
#     def sound(self):
#         print('animal sound')
#
# class Dog(Animal):
#     def sound(self):
#         print('woof')
#
# class Cat(Animal):
#     def sound(self):
#         print('meow')
#
# class cow(Animal):
#     def sound(self):
#         print('moo')
#
# def animal_sound(x):
#     x.sound()
#
# animal_sound(cow())
# animal_sound(Dog())
# animal_sound(Cat())

# from  abc import ABC, abstractmethod
#
# class Vehicle (ABC):
#     @abstractmethod
#     def move(self):
#         print("Vehicle moved")
#
# class Car (Vehicle):
#     def move(self):
#         print("Car moved")
#
# class Bicycle(Vehicle):
#     def move(self):
#         print("Bicycle moved")
#
#
# d = Bicycle()
#
# d.move()


# try:
#     x = int(input('enter first num: '))
#     y = int(input('enter second num: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('cant divide by zero')
# except ValueError:
#     print('value is not an integer')
# finally:
#     print('all done')

# try:
#     while True:
#         f = int(input('enter a number of temperature:(Fahrenheit) '))
#         if -100 <= f <= 300:
#             c = (f-32)/1.8
#             print(f'temperature in Celsius: {c}')
#             break
#         else:
#             print('enter a number between -100 and 300')
# except ValueError:
#     print('enter a valid number')




# class NegativeAgeError(Exception):
#     pass
#
# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise NegativeAgeError("Age can't be negative")
#     print(f"You are {age} years old.")
# except NegativeAgeError:
#     print("You entered a negative age!")
# except ValueError:
#     print("Please enter a valid integer.")


# class WeakPasswordError (Exception):
#     pass
#
#
# try:
#     password = input("Password: ")
#     if len(password) < 8 or password.isdigit() == True:
#         raise WeakPasswordError("Password must be at least 8 characters long and contain at least one letter")
#     print("Password:", password)
# except ValueError:
#     raise "Password must be at least 8 characters long and contain at least one letter"
#
# except WeakPasswordError as e:
#     print(e)


import time


# def dec(func):
#     def wrapper():
#         func()
#         print(time.process_time())
#
#     return wrapper
#
#
# @dec
# def func():
#     print("hello")
#
# func()



def dec(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper



@dec
def say():
    print('mahdi')

say()
