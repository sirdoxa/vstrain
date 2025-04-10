def f (x,y):
    print(max(x,y))

def upper(x):
    print(x.upper())

# f(5,81)
# upper('mahdi')
#
# def po(x):
#     print(x ** 2)
from  functools import wraps
def dec(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(10 * '*')
        result = f(*args, **kwargs)
        print(result)
        print(10 * '*')
    return wrapper

@dec
def dec_name():
    p = input()
    return p
