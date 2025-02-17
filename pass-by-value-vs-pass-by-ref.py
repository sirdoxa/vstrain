# pass by value

def a(x):
    x += [10,11]
    print(x)
    

x = [11,15,16,17,7,8]
a(x)
print(x)
# ----------------------------------

# pass by refrence

def b(x):
    x += (10,11)
    print(x)


x = (1,2,3,4,5)
b(x)
print(x)