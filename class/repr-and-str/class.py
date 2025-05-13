class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
    def __str__(self):
        return f'{self.__class__.__name__}({self.firstname}, {self.lastname}, {self.age})'
    

person1 = Person('Mahdi','Nabavi',18)
print(person1.lastname)
print(str(person1))
print(repr(person1))
print(id(person1))
print(person1.__str__())

person2 = Person('Mahdi','Nabavi',18)
print(person2.firstname)
print(str(person2))
print(repr(person2))
print(id(person2))
print(person2.__str__())
