# odd or even

# l = input('enter the list:(seperated by space!)--> ').split(' ')
# l = list(map(lambda x :int(x),l))
# odd = list(filter(lambda x : x % 2 != 0, l))
# even = list(filter(lambda y : y % 2 == 0, l))
# print(f'list is {l}\nodd = {odd} and even = {even}')

#----------------------------------------------------

# l = [('ali',55),('mohsen',25),('mahdi',22),('kamran',5)]
# print(sorted(l,key=lambda x:x[1]))

#-----------------------!!!!!!!!!------------------------

l = [{'wheight': 100, 'color': 'red'}, {'wheight': 150, 'color': 'yellow'}, {'wheight': 1500, '': 'green'}]
k = list(sorted(l,key=lambda x : l[l]))
print(k)


#----------------------------------------------------
# m = input('enter your numbers: ').split(' ')
# k = []
# l = list(map(lambda x : int(x),m))
# k.append(l)
# odd = list(filter (lambda x: x% 2 == 0,l))
# even = list(filter (lambda y: y% 2 != 0,l))
# print(f'list is {l}\nodd is {odd}\neven is {even}')

#-----------------------------------------------------

# m = input('enter your numbers: ').split(' ')
# l = set(map(lambda x : int(x),m))
# moraba = set(map(lambda x : x**2,l))
# mokab = set(map(lambda x : x ** 3, l))
# print(f'list is{l}\nmokab is {mokab}\nmoraba is {moraba}')

#------------------------------------------------------
# m = input('enter an string: ')
# ch = input('enter a chr: ')
# k = map(lambda x : m.startswith(ch),m)
# print(k())

#-------------------------------------------------------
# m = input('enter an string: ')
# k = lambda x: x.replace('.','',1).isdigit()
# print(k(m))