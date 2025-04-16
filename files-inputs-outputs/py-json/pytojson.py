import json
# loads ==> json string to python type ---> deserialize / pars

jn_str = '4'
py_type = json.loads(jn_str)
print(jn_str,type(jn_str))
print(py_type,type(py_type))

# load ==> json file to python type

with open('myfile.json','r') as jf:
    s = json.load(jf)

print(s,type(s))

# dumps ==> python type to json string ---> serialize

d = {'a':15,'b':20}
j = json.dumps(d)
print(d,type(d))


# dump ==> python type to json file

d = {
    'name':'mahdi',
    'last name':'nabavi',
    'age': '18',
    'marks':{'riazi':[15,16,17],'fizik':[15,9,13]},
    'lessons':['fizik','honar','riazi']
}

with open('test.json','w') as jf:
    json.dump(d,jf,indent=4,sort_keys=True)
