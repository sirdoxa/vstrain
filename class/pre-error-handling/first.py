# try:
#     x = int(input('enter the first num: '))
#     y = int(input('enter the second num: '))
#     print('x / y is', x / y)
# except ZeroDivisionError:
#     print('cannot divide by zero!!')
#     y = int(input('enter the second num carefully: '))
#     print('x / y is', x / y)
# except ValueError:
#     print('enter the right format!(number)')

# finally:
#     print('end!')


# # ====================or====================

# try:
#     if (x := int(input('enter the first num: '))) and (y := int(input('enter the second num: '))):
#         print('x / y is', x / y)
# except ZeroDivisionError:
#     print('cannot divide by zero!!')
#     if (y := int(input('enter the second num carefully: '))):
#         print('x / y is', x / y)
# except ValueError:
#     print('enter the right format!(number)')

# finally:
#     print('end!')

# ====================or====================


try:
    x = int(input('enter the first num: '))
    y = int(input('enter the second num: '))
    print('x / y is', x / y)
    if x == 7:
        raise NameError("hahaha cannot devide penaldo!!")
except (ZeroDivisionError,ValueError):
    x = int(input('enter the first num: '))
    y = int(input('enter the second num: '))
    print('x / y is', x / y)

else:
    print('without any exception!')
finally:
    print('*!'*20)