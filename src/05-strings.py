# Strings: orders, immutable, text representation
# mystring = 'Hello Word'
# char = mystring[2]

# substring = mystring[::-1]


# greeting = 'Hello'
# name = 'Tom'
# setence = greeting + ' ' + name
# for i in greeting:
#     print(i)

# if 'ell' in greeting:
#     print('yes')
# else:
#     print('no')

# mystring = 'Hello Word'
# mystring = mystring.strip()
# mystring = mystring.upper()
# mystring = mystring.lower()
# mystring = mystring.startswith('Hello')
# mystring = mystring.endswith('World')
# mystring = mystring.find('lo')
# mystring = mystring.count('o')
# mystring = mystring.replace('World', 'Universe')

# mystring = 'how,are,you,doing'
# mylist = mystring.split(',')
# new_string = ' '.join(mylist)

# from timeit import default_timer as timer
# mylist = ['a']*1000000


# # Bad
# start = timer()
# mystring = ''
# for i in mylist:
#     mystring += i
# stop = timer()
# print(stop-start)

# # Good
# start = timer()
# mystring = ''.join(mylist)
# stop = timer()
# print(stop-start)

# %, .format, f-String
var = "Tom"
var2 = 6
# my_string = 'the variable is %s' % var
# my_string = 'the variables is {:.2f}and {}'.format(var, var2)
my_string = f'the variable is {var} and {var2}'
print(my_string)
