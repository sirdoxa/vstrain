# def cor():
#     print('hi')
#     while True :
#         name = yield
#         print(f'my name is {name}')
#         print('bye')

# x = cor()
# next(x)
# x.send('kalak')
# next(x)



# -------------------------------------------
# def gc():
#     print('start')
#     for i in range(11):
#         x = yield i
#         print(f'my name is {x}')

# x = gc()
# print(next(x))

# x.send('mahdi')
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# --------------------------------------------------------


def fosh(words):
    print('start')
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = '*' * 5

f = fosh(['koon' , 'sag' , 'olagh' ,  'khar'])
next(f)

print(f.send('khar'))
print(f.send('mahdi'))
print(f.send('sag'))
print(f.send('taha'))
print(f.send('j'))

def cor():
    print('hi')
    while True :
        name = yield
        print(f'my name is {name}')
        print('bye')

x = cor()
next(x)
x.send('kalak')
next(x)
