print('normal: ')
l = []
for i in range(10):
    l.append(i**2)

print(l)
# -------------------------------------------------
print('with comprehension: ')
x = [i**2 for i in range(10)]
print(x)
# -------------------------------------------------
print('with map:')
m = list(map(lambda i : i ** 2 ,range(10)))
print(m)
# -------------------------------------------------
print('with comprehension(even):')
x = [i**2 for i in range(10) if i % 2 == 0]
print(x)
# -------------------------------------------------
s1 = [1,2,3]
s2 = [4,2,3]
t = [(i , j) for i in s1 for j in s2 if i != j ]
print(t)
# -------------------------------------------------
from math import pi

p = [str(round(pi,i))  for i in range(10) ]
print(p)
# -------------------------------------------------
matrix =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
t = [[row[i]for row in matrix]for i in range(4)]
for j in t:
    print(j)

# -------------------------------------------------

x1 = [1,2,3]
x2 = [4,5,6]
x3 = [7,8,9]
print(list(zip(x1,x2,x3)))
# -------------------------------------------------
'''اگه ما بجای [] ,()بزاریم بجای list comprehension , generator expression داریم'''

c = (x for x in (1,2,3))        # generator expression
# print(list(c))
print(next(c))
print(next(c))
print(next(c))

# -------------------------------------------------
x = 'kfkfkhfkhdodkd'        
t = {i for i in x}          # set 
print(t)
# -------------------------------------------------
d = {'mahdi':18,'taha':16,'hamid':43}
s = {key:value for key,value in d.items()}
print(s)
# -------------------------------------------------
d1 = ['a','b','c']
d2 = [12,20,40]         # dictionary
d = {key:value for key , value in zip(d1,d2)}
print(d)
# -------------------------------------------------
# [expression_if_true if condition else expression_if_false for variable in iterable]

x = [ 1,2,3,4,56,7,8,9]
t=[i if i % 2 != 0 else 'zoj' for i in x  ]
t=[i if i % 2 != 0 else 0 for i in x  ]
print(t)

# -------------------------------------------------
def func(x):
    if x % 2 != 0 :
        return x
    else:
        return 0
x = [ 1,2,3,4,56,7,8,9]
t=[func(i) for i in x  ]
print(t)

# -------------------------------------------------
from random import randrange
def ran():
    return randrange(50,150)
t = [x for _ in range (10) if  (x:=ran()) >= 100 ] # walrus OP--> :=
print(t)
# -------------------------------------------------
names = ['mahdi','taha','hamid','saber']
t = {name:[i for i in range(5)] for name in names}
print(t)