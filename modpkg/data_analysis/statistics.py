def stat(list):
    '''list'''
    list = sorted(list)
    total = sum(list)
    x = total / len(list)
    return x

def miane(list):
    '''list'''
    list = sorted (list)
    if (len(list) % 2) == 0:
        mid1 = len(list) // 2 
        mid2 = (len(list) // 2) + 1
        return mid1,mid2

    else:
        x = len(list) // 2
        return list[x]        


