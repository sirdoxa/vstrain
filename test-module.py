
import module.mod1 
# module.mod1.f(15,18)

# module.mod1.dec_name()

import module.mod2
print(module.x)
from modulef import *
print(func1('2356'))
print(name)
# print(_age)

from modulef import _age,name,func1
print(func1('2356'))
print(name)
print(_age)

print(module.mod2.op)

module.mod2.op = 'no'

print(module.mod2.op)

import importlib ; importlib.reload(module.mod2)

print(module.mod2.op)
