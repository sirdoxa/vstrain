def exm(x):
    print(x **2)


exm.creator = 'mahdi'
exm.title = 'func-attributes'
print(exm.creator)

setattr(exm,'language','python')
# print(dir(exm))
print(exm.language)

print(getattr(exm,'title'))
if hasattr(exm,'creator'):
    print('exists')
else:
    print('not exist')

print(exm.__dict__)

delattr(exm,'language')
print(exm.__dict__)

del exm.creator
print(exm.__dict__)

