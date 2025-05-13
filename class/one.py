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