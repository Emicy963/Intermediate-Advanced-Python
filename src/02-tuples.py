# Tuple: ordered, immutable, allows duplicate elements
# mytuple = 'Max', 3, 'Ana'
# mytuple = ('Max')^

# mytuple = tuple(['Max', 28, 'Boston'])
# print(mytuple)

# item = mytuple[1]
# print(item)

# # mytuple[0] = 'Lucas' - Its return TypeError because tuples be immutable

# for i in mytuple:
    # print(i)

# if 'Max' in mytuple:
#     print('yes')
# else:
#     print('no')

# mytuple = ('a', 'b', 'c', 'd', 'i', 'i')
# print(len(mytuple))
# print(mytuple.count('i'))
# print(mytuple.index('a'))

# mylist = list(mytuple)
# print(mylist)

# mytuple2 = tuple(mylist)
# print(mytuple2)~

# mytuple = (1,32,3,4,5,7,6,9,87,0)
# a = mytuple[2:5]
# print(a)

# mytuple = 'Max', 21, 'Luanda'

# name, age, city = mytuple
# print(name)
# print(age)
# print(city)

# mytuple = (0,1,2,3,4)
# i1, *i2, i3 = mytuple

# print(i1)
# print(i3)
# print(i2)

import sys
import timeit
mylist = [0,1,2,'hello', True]
mytuple = (0,1,2,'hello', True)
print(sys.getsizeof(mylist), 'bytes')
print(sys.getsizeof(mytuple), 'bytes')

print(timeit.timeit(stmt='[0,1,2,3,4,5]',number=1000000))
print(timeit.timeit(stmt='(0,1,2,3,4,5)',number=1000000))
