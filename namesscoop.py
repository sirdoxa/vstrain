def a():
    x = 12 
    print('a->',x)
    def a2():
        x = 5
        print('a2->',x)
    a2()
a()    
#a2() #not defined because we didn't call a()
