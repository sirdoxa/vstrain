def exmp(func):
    def inner ():
        print(15 * '*')
        func()
        
        print(15 * '*')
    return inner


def func():
    print ('reza')

s = exmp(func)
s()