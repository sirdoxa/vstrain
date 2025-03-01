# from time import perf_counter
# start1 = perf_counter()
# def square_gen():
#     for i in range(0, 1000000000, 2):
#         yield i ** 2

# end1 = perf_counter()
# square_gen()
# print(f'time:{end1 - start1}')

# #--------------------------------------------------
# start = perf_counter()

# def square_gen1():
#     l = []
#     for i in range(0, 1000000000, 2):
#         l.append(i ** 2) 
#     return l
    
# end = perf_counter()
# square_gen1()
# print(f'time:{end - start}')

#--------------------------------------------------------

# def enu_gen():
#     s = input('enter an string: ')
#     for i in range(len(s)):
#         yield i,s[i]
# x = enu_gen()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# def fib(list):
#     for i in range(len(list)):
#         yield list[i] + list[i+1]
# n = [0,1,2,3,4,5,6,7,12,40]
# f = fib(n)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
#-----------------------------------------------------

def shw(x):
    result = []  # لیستی برای نگه‌داشتن مقادیر قبلی
    for i in range(1, len(x)):  # از ایندکس 1 شروع می‌کنیم
        result.append(x[i])  # مقدار جدید را اضافه می‌کنیم
        yield result[:]  # لیست را کپی کرده و برمی‌گردانیم

m = [15, 14, 2, 3, 1, 4, 5, 28, 8]
v = shw(m)

print(next(v))  # [14]
print(next(v))  # [14, 2]
print(next(v))  # [14, 2, 3]
print(next(v))  # [14, 2, 3, 1]
print(next(v))  # [14, 2, 3, 1, 4]
print(next(v))  # [14, 2, 3, 1, 4, 5]
print(next(v))  # [14, 2, 3, 1, 4, 5, 28]
print(next(v))  # [14, 2, 3, 1, 4, 5, 28, 8]

# -----------------------------------------
# def rev(x):
#     o = len(x)-1
#     while o>=0:
#          yield x[o]
#          o -= 1
# n = ('mahdi')
# f = rev(n)
# print(next(f))
# print(next(f))
# print(next(f))


# ---------------------------------------------------


# x = input('zoj or fard: ')
# def ada(x):
#     addadz = 0
#     addadf = 1
#     while True:
#         if x == 'zoj':
#             yield addadz 
#             addadz += 2
#         elif x == 'fard':
#             yield addadf
#             addadf += 2

# g = ada(x)
# for i in range (150):
#     print(next(g))

# ---------------------------------------------------

# def gen1():
#     x = 0
#     while True:
#         yield str(x) * x 
#         x += 1


# p = gen1()
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# -------------------------------------------------
def y (f):
    def inner ():
            p = f()
            yield p ** 2
    return inner

@y
def x ():
    import random
    x = random.randint(1,100)
    print(x)
    return x

o = x()
print(next(o))