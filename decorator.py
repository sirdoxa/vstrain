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

def dec(ka):
    def mo():
        print('=' * 20)
        ka()
        print('=' * 20)
    mo()
    return mo



def ka():
    return 'mahdi'

s = dec(ka)
s()