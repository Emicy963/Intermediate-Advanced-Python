# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {'name': 'Anderson', 'age':21,'email':'anderson@test.com'}
print(mydict)

mydict2 = dict(name='Mary', age=27, city='Boston')
# print(mydict2)

# value = mydict['name']
# print('Value:',value)

# mydict['email'] = 'anderson@test.com'
# print(mydict)

# del mydict['name']
# print(mydict)

# mydict.pop('age')
# print(mydict)

# mydict.popitem()
# print(mydict) Remove the last item

# if 'name' in mydict:
#     print(mydict['name'])

# try:
#     print(mydict['name'])
# except:
#     print('Erro')

# for key in mydict.keys():
#     print(key)

# for value in mydict.values():
#     print(value)

# for key, value in mydict.items():
#     print(key, value)

# mydict_cpy = dict(mydict)
# mydict_cpy = mydict.copy()
# print(mydict_cpy)

# mydict_cpy['email'] = 'anderson@test.com'
# print(mydict)
# print(mydict_cpy)

# mydict.update(mydict2)
# print(mydict)

mydict3 = {3: 9, 6: 36, 9: 81}

# value = mydict3[9]
# print(value)

mytuple = (8, 7)
mydict = {mytuple: 15}

print(mydict)
