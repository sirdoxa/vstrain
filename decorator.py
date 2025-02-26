# Decorator 
# توابع تو در تو
# ارسال تابع به عنوان ارگومان

# -------------------------------------------------

# def exmp(func):
#     def inner ():
#         print(15 * '*')
#         func()

#         print(15 * '*') 
#     return inner


# def func():
#     print ('dana haroom')

# s = exmp(func)()

# print('***************\ntaha\nnabavi\n***************')

# ------------------------------------------------------

# def mo(m):
#     def inner(h, j):
#         if j == 0:
#             return'warning!!!!!'
#         return m(h, j)
#     return inner

# @mo   # @ + the name of decorator function can run python decorator function on our new function
# def m(h, j):
#     return h/j

# print(m(10, 0))



# =======================================

# def dec(ka):
#     def mo():
#         print('=' * 20)
#         ka()
#         print('=' * 20)
#     mo()
#     return mo


# def ka():
#     return 'mahdi'

# s = dec(ka)
# s()

# --------------------------------------
# import functools

# def decorator_name(func):
#     @functools.wraps(func)  # این خط اطلاعات تابع اصلی را حفظ می‌کند
#     def wrapper(*args, **kwargs):
#         # ✅ کد قبل از اجرای تابع اصلی (Pre-processing)
#         result = func(*args, **kwargs)  # اجرای تابع اصلی
#         # ✅ کد بعد از اجرای تابع اصلی (Post-processing)
#         return result
#     return wrapper



#--------------------------------------------------------------------
# import functools

# def decorator_name(o):
#     def actual_decorator(func):  # حالا این تابع، `func` را می‌گیرد
#         @functools.wraps(func)  # حفظ اطلاعات تابع اصلی
#         def wrapper(*args, **kwargs):
#             print('*' * o)  # ✅ کد قبل از اجرای تابع اصلی
#             result = func(*args, **kwargs)  # اجرای تابع اصلی
#             return result  # ✅ بازگرداندن مقدار تابع اصلی
#         return wrapper
#     return actual_decorator  # دکوراتور اصلی را برمی‌گردانیم

# @decorator_name(25)  # دکوراتور حالا یک عدد می‌گیرد
# def func():
#     return 'mahdi'

# print(func())

#---------------------------------------------------
from time import perf_counter
def debug(f):
    def debuger(*args,**kw):
        start = perf_counter()
        f(*args,**kw)
        end = perf_counter()
        g = end - start
        print(f'time : {g:.10f}')
    return debuger


@debug
def pow(x):
   return x ** 2 * 8

h = pow(8)
print(h)