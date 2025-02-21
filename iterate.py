# iterate -> تکرار کردن
# iteration -> تکرار: for , while
# iterable -> قابل تکرار ،تکرار پذیر
# iteraator -> تکرار کننده ، تکرارگر


# i = [1, 2, 3]
# i = iter(i)
# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break
# -----------------------------
# m = input('enter some numbers (separated by space) --> ').split(' ') 
# i = iter(m)  

# while True:
#     try:
#         print(next(i))   
#     except StopIteration:
#         break
#------------------------------------
# from itertools import count
# counter = count(10)

# for i in counter:
#     print(next(counter))
#     if i == 500000:
#         break

#-------------------------------------

from itertools import count
counter = count() #=>lazy
print('__next__'in dir(counter))
print(next(counter))