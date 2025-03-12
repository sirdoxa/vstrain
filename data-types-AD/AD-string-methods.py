print(dir(str))
x = 'Straße'
print(x.casefold())
print(x.lower())

print(x.center(20,'*'))
print(repr(x.center(20)))
p = 'mahdi\tnabavi'
print(p)
print(p.expandtabs(15))  #(space)
d = {'a':'mahdi','b':'nabavi'}
print('my name is {a} {b}'.format_map(d))
m = 'mahdi nabavi'
print(m.find('na'))
print(m.index('i'))
o = 'Mahdi nabavi'
p = 'mahdi'
print(o.isalpha())  #is alphabet
print(p.isalpha())
p = 'mahdi'
r = 'مهدی'
print(p.isascii())
print(r.isascii())
x = '799556'
print(x.isnumeric())
print(x.isdecimal())    
print(x.isdigit())  # the diffrence between this three meyhods-->https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth
s = 'c_66'
print(s.isidentifier()) #for example the name of the variable
s = 'c_ 66'
print(s.isidentifier()) 
s = 'jiiejfifepf'
print(s.islower())
s = 'JFJJFJF;pkookk,jjJjjJJjJ'
# print(s.islower().lower())
x = 'mahdi\tnabavi'
print(x.isprintable())  #\t,\n,... -->false

x = '   '
print(x.isspace())
x = '  \n\n\n\t\t\n '
print(x.isspace())
x = 'Mahdi Nabavi 1385 D:'
print(x.title())
print(x.istitle())
x = 'IJFEIFIEJIJ'
print(x.isupper())
numbers = ["1", "2", "3", "4"]
result = ", ".join(numbers)
print(result)  # خروجی: 1, 2, 3, 4

x = ['mahdi','nabavi']
print(' '.join(x))
# -------------------------------------------------
x = 'mahdi'
print(repr(x.ljust(15,'*')))
print(repr(x.rjust(15,'*')))


x = 'barsam'

tab = str.maketrans('b','ß','a')
print(tab)
print(x.translate(tab))
# or
d = {'a':'@','b':'ß','m':None}
m = str.maketrans(d)
print(m)
x = 'barsam'
print(x.translate(m))


s = 'mahdi 1385 nabavi'
print(s.partition('i'))
print(s.rpartition('i'))
print(s.partition('1385'))

x = '----mahdi----'
print(x.removeprefix('-'))
print(x.removesuffix('-')) # only remove one of ()
print(x.lstrip('-')) # remove all of ()
x = 'yxzyxjkjpplplpp'
print(x.removeprefix('xyz'))
print(x.lstrip('xyz'))


x = 'dana kalak'
print(x.rindex('l'))


x = 'mahdi nabavi python'
print(x.split(' '))
print(x.split(' ',1))
print(x.rsplit(' ',1))

x = 'mahdi\nnabavi\nxd'
print(x.splitlines())
print(x.splitlines(True))


x = 'MAhdi nabavi OG'
print(x.swapcase())

x = '1'
print(x.zfill(10))

h = '1'
m = '3'
print(h.zfill(2),':',m.zfill(2))
