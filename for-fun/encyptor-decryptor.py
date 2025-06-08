while True:
    print('choose your option:\n\t1)encrypt\n\t2)decrypt\n\t3)quit')
    on = input('enter your choice: ')
    key = int(input('enter your key(number): '))

    if on == '1':
        x = ''
        o = input('enter your text: ')
        for c in o:
            l = ord(c) * key 
            x += chr(l)
        print(x)
        break
    elif on == '2':
        i = ''
        o = input('enter your text: ')
        for c in o:
            p = ord(c) // key
            i += chr(p)
        print(i)
        break
    elif on == '3':
        print('good luck!!!!')
        break
    else:
        print('invalid input')
