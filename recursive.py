# # def fib(x):
# #     if x == 0 or x == 1:
# #         return x
   
# #     return fib(x-1) + fib(x-2)

# # print(fib(5))

# # -------------------------------------------------


# # from time import sleep

# # def rec(x):
# #     if x == 0:
# #         return 0
# #     sleep(1)
# #     print(x)
# #     x -= 1
# #     rec(x)

# # rec(15)


# # -----------------------------------

# # def mul(x):
# #     if x == 0:
# #         return 1
# #     elif x % 10 < 5:
# #         return mul(x // 10)
# #     else:
# #         return (x % 10) * mul(x // 10)  

# # print(mul(12346789))

# # ------------recursive decorator-------------------

# # from functools import wraps
# # from time import sleep
# # def star(func):
# #     @wraps(func)
# #     def inner(*args,**kw):
# #         print('*' * 20)
# #         func(*args, **kw)
# #         print('-' * 20)
# #     return inner
        

# # @star
# # def rec(x):
# #     if x == 0:
# #         return 0
# #     sleep(1)
# #     print(x)
# #     x -= 1
# #     rec(x)

# # rec(15)

# #------------------recursive generator---------------------


# # from time import sleep

# # def g_rec(x):
# #     if x == 0:
# #         return
# #     sleep(0.3)
# #     print(x)
# #     yield x    #^^^^^^^^^^^^^^^^^^^^^^^^^^^
# #     for i in g_rec(x-1):
# #         yield i


# # o = g_rec(10)
# # print(list(o))




# #-------------------------memoization------------------------------

# from functools import wraps

# # def fn(func):
# #     memo = {}
# #     @wraps(func)
# #     def inner(n):
# #         if n not in memo:
# #             memo[n] = func(n)
# #         return memo[n]
# #     return inner


# # @fn
# # def fib(x):
# #     if x == 0 or x == 1:
# #         return x
   
# #     return fib(x-1) + fib(x-2)

# # print(fib(40))

