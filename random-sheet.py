# shoa = float(input('shoa: '))
# pi = float(3.14)
# masahat = pi * (shoa ** 2)
# print(masahat.__float__())
#
#
# addad = float(input('addad ra vared konid: '))
# tavan2 = addad ** 2
# tavan3 = addad ** 3
# print(f'addad: {addad}')
# print(f'tavan2: {tavan2}')
# print(f'tavan3: {tavan3}')
#
#
# addad1 = float(input('addad paye:'))
# addad2 = float(input('addad2 tavan:'))
# javab = addad1 ** addad2
# print(javab)
#
#
# addad1 = float(input('addad1 ra vared konid: '))
# addad2 = float(input('addad2 ra vared konid: '))
# addad3 = float(input('addad3 ra vared konid: '))
# javab = (addad1 + addad2 + addad3) / 3
# print(javab)
#
# x = 5
# y = 7.26656544
# print('x is {1}\ny is {0:<50}\nz is {2}'.format(x,y,5+7))
#
#
#
# import datetime
# today = datetime.datetime.now()
#
# print(f'{today:%Y/%m/%d \n%I:%M:%S %p}')
# print(today)
#
#
#
#
# s = input('enter: ')
# s = s.rstrip()
# i = s.rfind(' ')
# print(s[i+1:])
#
#
# s1 = input('j1: ')
# s2 = str(s1.find('0'))
# s3 = s1.replace(s2,"+98")
# print(s3)
#
#
# x = input('inter sentence: ')
# y = input('inter char: ')
# x=x.count(y)
# print(x)
#
#
# x = input('inter sentence: ')
# x = x.rstrip()
# y = x.rfind(' ')
# print(x[y+1:])
#
#
#
#
# x = input('inter sentence: ')
# y = input('inter sentence2: ')
# print(y in x)
#
#
#
# x = input('inter sentence: ')
# y = input('inter sentence2: ')
# z = x.find(y)
# if z == int(z) and z != -1:
#     print('true')
# elif z == -1:
#     print('false')
# else:
#     print('false')
# print(z)
#
#
# x = input('inter sentence: ')
# x = x.replace(' ', '').replace('\n', '').replace('\t','')
# print(x)
#
#
# x = input('inter char: ')
# print(ord(x))
#
#
#
# x = input('inter phone number: ')
# print(x.isnumeric())
#
#
# x = input('inter sentence: ')
# kalame = x.count(' ')+1
# jomle = x.count('.') + x.count('?') + x.count('!')
# charac = x.count('.')+x.count('!') +x.count('?')+x.count(';')
# tedad = len(x)
# tedadh = len(x) - (x.count(' ')+x.count('.')+x.count('?')+x.count('!')+x.count(';'))
# print(f'kalame = {kalame} \n'
#       f'jomle = {jomle} \n'
#       f'character = {charac} \n'
#       f'tedad kol caracter = {tedad} \n'
#       f'tedad horoof = {tedadh} \n')
#
#
# number = list('1456565655')
# print('6' in number)
#
#
#
# o = []
# y = o.append(input('inter l: '))
# print(o, '\n' ,type(o))
# nomarat = []
# name = input("What is your name? ")
# nomarat.append(name)
# riazi = float(input('riazi: '))
# nomarat.append(riazi)
# fizik = float(input('fizik: '))
# nomarat.append(fizik)
# shimi = float(input('shimi: '))
# nomarat.append(shimi)
# moadel = (nomarat[1] +nomarat[2] + nomarat[3]) / (len(nomarat) - 1)
# print(f'hello {name} here is your moadel: ',moadel)
# print(nomarat)


# li = []
# name = input("Enter your name: ")
# li.append(name)
# shimi = float(input("shimi: "))
# li.append(shimi)
# fizik = float(input("fizik: "))
# li.append(fizik)
# riazi = float(input("riazi: "))
# li.append(riazi)
# moadel = (li[1]+li[2]+li[3])/3
# li.append(moadel)
# print(moadel)
# print(li)




# phone = str(input('phone: '))
# li = list(phone)
# for i in phone:
#     print(i)




# x = input("Enter a number: ")
# l1 = list(x)
# o = len(l1)
# r = input("Enter a number: ")
# l1.extend(r)
# for i in l1:
#     print(i)
# print(l1)
# print(len(l1))


# a = {}
# key = input("Enter a kalame: ")
# mani = input("Enter a mani: ")
# mani2 = input("Enter a mani2: ")
# if mani2 == '0':
#     a[key] = mani
# else:
#     a[key] = mani , mani2
#
# print(a)


# x = int(input("Enter a number: "))
# if x % 2 == 0 and x % 5 == 0:
#     print("yeah!!!!!")
# else:
#     print("nope")



# x = int(input("Enter zel rast: "))
# y = int(input("Enter zel chap: "))
# z = int(input("Enter ghaede: "))
#
# if x ==z == y :
#     print("motesavi azla")
#
# elif x == y :
#     print("motesavi saghein")
#
# else:
#     print("mokhtalefol azla")




# print(ord('Z'))


# x = input('enter chr: ')
#
# x = ord(x)
# if 57 >= x >= 48:
#     print('its a number!')
# elif 90 >= x >= 65:
#     print('its a capital letter!')
# elif 122 >= x >= 97:
#     print('its a small letter!')
# else:
#     print('its a special character!')




# y =int(input("Enter a number: "))
# while y <=95 :
#     y += 1
#     print('*'*y)
# y = int(input("Enter a number: "))
# while y >=1:
#
#     y -= 1
#     print('*'* y)
#
#
#
# s = 'hello'
# y = s[0]
# s[0] = 'H'
# print(s)
#
#
# x = 0
#
# s = (1 , 2, 3 , 4, 8)
# print(sum(s))
#
#
# print(min([],default=None))
#
#
#
#
# o = [1,2,23,556,11,222,555]
# l = [1,23,565,65656,5]
# for i in o:
#     if i not in l:
#         print(i)
#
# a = int(input('enter a number: '))
# b = int(input('enter a number: '))
# for i in range(a, b+1):
#     print(i)




# a = int(input('enter a number: '))
# b = int(input('enter a number: '))
# for i in range(1 , a+1):
#     if a % i == 0 and b % i == 0:
#         print(list(i))


# while True:
#     print('choose your option:\n\t1)encrypt\n\t2)decrypt\n\t3)quit')
#     on = input('enter your choice: ')
#     if on == '1':
#         x = ''
#         o = input('enter your text: ')
#         for c in o:
#             l = ord(c) * 2 + 5
#             x += chr(l)
#         print(x)
#         break
#     elif on == '2':
#         i = ''
#         o = input('enter your text: ')
#         for c in o:
#             p = (ord(c) - 5) // 2
#             i += chr(p)
#         print(i)
#         break
#     elif on == '3':
#         print('good luck!!!!')
#         break
#     else:
#         print('invalid input')


# def cobs(x):
#     return 2 * x + 88
#
#
# print(cobs(65))
# print(cobs(45445488))


# def counter():
#     sentence = input('enter a sentence: ')
#     word = input('enter a word: ')
#     return print(str(sentence).count(str(word)))
#
#
# counter()

# from sys import set_int_max_str_digits
# set_int_max_str_digits(1500000)
# def fact():
#     h = input('enter a number: ')
#     f = 1
#     for i in range(1, int(h) + 1):
#         f *= i
#     return print(f)
#
#
# def jam():
#     g = 0
#     for i in range(1, int(h) + 1):
#         g += fact()
#     return print(g)
#
# jam()

# def gam():
#     t = input('enter a number: ')
#     f = 0
#     for i in range(1, int(t) + 1):
#         f +=i
#     return print(f)
#
# gam()

# def maxomin():
#     l=[]
#     first = int(input('enter a number: '))
#     second = int(input('enter a number2: '))
#     third = int(input('enter a number3: '))
#     return print(f'max = {max(first, second, third)}') , print(f'min = {min(first, second, third )}')
#
# maxomin()




# def max3(a, b):
#     return max(a, b)
#
# x = input("Enter the first number: ")
# y = input("Enter the second number: ")
# z = input("Enter the third number: ")
# print(max3(x, y))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# s = 'robot'
# a,b,c,d,e = s
# b = d = '*'
# s = (a,b,c,d,e)
# print(s)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# for i in (1,2,3,4,5):
#     print(i)



# def outer(func):
#     def inner():
#         print('hello')
#         func()
#         print('bye')
#     return inner

# @outer
# def name ():
#     print('mahdi')

# name()

#----------------------------------------------------


# import time
# help(time.perf_counter)



# x = [1,2,3,4,5,6,7,8,9]
# l = []
# for i in x:
#     if i % 2 == 0:
#         l.append(i)

# def mul(args):
#     res = 1
#     for i in args:
#         res *= i
#     return res
    
# h = mul(l)
# print(h)
# p = 1
# print(map(lambda x:p*x , ))
#------------------------------------------------
# from random import randint
# y = int(input('enter a number: '))
# z = 0
# while True:
#     x = randint(1,100)
#     while x != y :
#         z += 1
#     if x == y :
# #         print('thats it')
# #         break

# # print(z+'times')
# #========================================================
# from random import randint

# y = int(input('Enter a number: '))  
# z = 0  
# while True:
#     m = {0}
#     x = randint(1, 10000000)
#     m.add(x)  
#     z += 1  
#     if  y in m:
#         break  

# print(f'Tried {z} times') 

# -------------------------------------------------
# import sys
# sys.setrecursionlimit(1500)
# def say_hi(x=0):
#     if x == 1400:
#         return 'bye'
#     print("salam!")
#     return say_hi(x + 1)

# result = say_hi()
# print(result)

# -------------------------------------------------
# import webbrowser
# url = 'https://www.google.com/maps'
# webbrowser.open_new_tab(url)
# -------------------------------------------------
# import time
# print(time.ctime())
# print(time.asctime())
# print(time.get_clock_info('time'))
# print(time.gmtime())
# print(time.mktime(''))


def name():
    x = input('name: ')
    return (f'welcome {x} !\nhere is your code!')


def km():
    x = input('KM: ')
    y = int(x) * 1000
    return ('*****' + f'{y} m' + '*****')

def miangin():
    x = []
    dars_ha = ['riazi', 'farsi', 'oloom', 'fizik']
    
    for dars in dars_ha:
        while True:
            try:
                score = int(input(f'{dars} (0-20): '))
                if 0 <= score <= 20:
                    x.append(score)
                    break
                else:
                    print('⚠️ Lotfan adadi bein 0 ta 20 vared konid.')
            except ValueError:
                print('⚠️ Lotfan faghat adad sahih vared konid.')
    
    average = sum(x) / len(x)
    return average



def mahdi():
    return 'mahdi '

print(mahdi() * 2)