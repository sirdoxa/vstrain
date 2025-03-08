print(dir(dict))  # dict --> {}          # set --> {0} or set()

c = {'a': 1, 'b': 2}
c.clear()
print(c)
# -----------------------------------------
c = {'a': 1, 'b': 2}

g = c.copy()
g['c'] = 3
print(g)
# -----------------------------------------
c = {'a': 1, 'b': 2}
print(dict.fromkeys(['a', 'b'], 7))
# -----------------------------------------
c = {'a': 1, 'b': 2}
print(c.get('a'))
print(c['a'])
print(c.get('c'))  # None
print(c.get('c', 4))  # None
# print(c['c']) #key error

# -----------------------------------------

c = {'a': 1, 'b': 2}
print(c.pop('a'))
print(c)

print(c.pop('c', 0))
# print(c.pop('c'))         # error

# -----------------------------------------
c = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(c.popitem())          # the last one!!
print(c.popitem())
print(c)
#-----------------------------------------

c = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
c.setdefault('p')
print(c)
c.setdefault('x',6)
print(c)

#-----------------------------------------

c = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(c.items())
print(c.keys())
print(c.values())

#-----------------------------------------
c = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(c.setdefault('d'))
print(c)
print(c.setdefault('p',0))
print(c)
#-----------------------------------------
c = {'a': 1, 'b': 2, 'c': 3, 'd': 4,'a': 0}             # if exists , update the value
c.update({'s':15 , 'f':14 , 'l' : 17})
print(c)

c.update([['q',25] , ['h',24] , ['m' , 27]])
print(c)
c.update(t=40,o=98,u=87)
print(c)


f = {'k' : 15000,'r' : 1000000}
print(f | c) # اگه تکراری یاشه اپدیت میکنه
z = f | c
print(z)

#-----------------------------------------
f = {'k' : 15000,'r' : 1000000}

f['diff'] = f.pop('k')

print(f)



