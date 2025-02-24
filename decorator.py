def exmp(func):
    def inner ():
        print(15 * '*')
        func()

        print(15 * '*') 
    return inner


def func():
    print ('dana haroom')

s = exmp(func)
s()
print('***************\ntaha\nnabavi\n***************')