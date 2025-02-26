def cor():
    print('hi')
    while True :
        name = yield
        print(f'my name is {name}')
        print('bye')

x = cor()
next(x)
x.send('kalak')
next(x)
