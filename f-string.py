x = 5
y = 4.266564
print(f'x is {x}\ny is {y:010.3f}\nx ** 2 is {x**2}') # in string for single quotation use !r after variable

# -------------------------------------------
def up(x):
    return x.upper()

x = 'mahdi'
print(f'upper is {up(x)}')
print(f'upper is {x.replace('a','A')}')

# -------------------------------------------
# '{'[field name] ['!' conversation] [':' format spec]'}' , !a , !r , !s

print(f'x is {'mahdi'!r}')
x = 4.25645

# [[fill]align][sign][#][0][width][grouping_option][.precision][type]

print(f'x --> {1.5:.3%}')               #[.precision][type]
print(f'x --> {1546466458:,.3f}')
print(f'x --> {1546466458:25,.3f}')
print(f'x --> {1546466458:025,.3f}')    # [0][width][grouping_option][.precision][type]
print(f'x --> {1546466458:#b}')         #[type] --> d = int     b = binary  o = 8   x = 16
print(f'x --> {452:+}')                 # [sign] if space  + --> space   - --> -
print(f'x --> {452:>20}','*',sep='')        # [[fill]align]
print(f'x --> {452:+<20}','*',sep='')       # [[fill]align]
print(f'x --> {452:^20}','*',sep='')        # [[fill]align]
print(f'x --> {452:^+20}','*',sep='')        # [[fill]align][sign]


import datetime
today = datetime.datetime.today()

print(f'{today:%Y/******%b}')


