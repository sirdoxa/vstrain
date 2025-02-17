# def len1():
#     st = input('enter an str: ')
#     k = 0
#     for i in st:
#         k += 1
#     print(k)


# len1()

# -------------------------

# def max1():
#     st = input('enter some numbers: ').split(' ')
#     print(st)
#     x = len(st) - 1
#     print(st[x])        

# max1()

# ----!!!!!!!!!!!!!!!!!!!!!!!!!!---

# def min1():
#     st = sorted(list(map(int,input('x:').split(' '))))
        
#     print(st[0])
# min1()

#----------------------------------

# def sum1():
#     st =sorted(list(map(int,input('x:').split(' '))))
#     x = 0
#     for i in st:
#         x = x + i
#     print(x)
# sum1()

#-------------------------------

# def moraba():
#     x = int(input('enter your number: '))
#     for i in range(0, x):
#         if i ** 2 == x:
#             print('yes')
#             break
#     else: #اگه تابع بریک بخوره کلا از همه حلقه ها میره بیرون
#         print('no')
# moraba()

#--------------------------------------

# def price():
#     x = int(input("enter the price: "))
#     y = int(input("enter the discount: "))
#     y = y /100
#     return print(f'the final price is {x - (x * y)} dollars')
# price()

#--------------------------------

# def find():
#     x = input("enter chr: ")    
#     y = int(ord(x))
#     if 57>=y>=48:
#         print('its a number!!!')
#     elif 90>=y>=65 :
#         print('its a capital word!!!')
#     elif 122>=y>=97 :
#         print('its a small word!!!')
#     else:
#         print('others signs!!!')


# find()
