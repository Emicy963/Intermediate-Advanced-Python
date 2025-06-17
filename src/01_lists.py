# Lists: Ordered, mutable, allows duplicate elements
mylist = ['banana', 'cherry', 'apple']
print(mylist)

mylist2 = list() # How create a blanck list or mylist2 = []

## Acess individual elements in a list
item = mylist[1] # Index indique who elements a wanna see in list, start on 0
print(item)
item2 = mylist[-1] # For acess last elements
print(item)

## Interable in list
for x in mylist:
    print(x)

### Using coditionals
if 'banana' in mylist:
    print('Yes')
else:
    print('No')

## Checks, append, insert, remove, clear, reverse, sort
print(len(mylist)) # Returns the len of the list

### Add itens
mylist.append('lemon') # This add a new element, how last element
print(mylist)

mylist.insert(1, 'blueberry') # This you can specify the index so you show the position for item to add
print(mylist)

### Remove itens
item = mylist.pop() # Remove the last item in list
print(f'Remove item: {item}')
print(mylist)

item = mylist.remove('cherry') # It remove specifique item in list using name. If item is not in list return ValueError

mylist.clear() # Remove all itens in list

### Reverse order
numberlist = [5,3,6,-2,-1,10]
print(numberlist)
numberlist.reverse() # Reversing order of itens
print(f'Reverse order: {numberlist}')

numberlist.sort() # Ordering list
print(f'Normal order: {numberlist}')

new_list = sorted(numberlist) # If you wanna create a new list with the same elements ordering
print(new_list)

## Multiple lists
mylist3 = [0] * 5
print(mylist3)

mylist4 = [1,2,3,4,5]

new_list = mylist3 + mylist4
print(new_list)

## SLicing
mylist5 = [1,2,3,4,5,6,7,8,9]
a = mylist5[1:5] # Start index 1 but don't take the index 5 stop in 4
b = mylist5[:5] # If don't specify start index, start for first item
c = mylist5[1:] # Start for index 1 to the last element
d = mylist5[::1] # That takes the item step one
e = mylist5[::-1] # Trick for revers list
print(a)
print(b)
print(c)
print(d)
print(e)

## Copying List
list_org = ['banana', 'cherry', 'apple']

list_cpy = list_org # list_org.copy()

list_cpy.append('lemon') # If you chance the copy list you don't modify the original list
print(f'Original: {list_org}')
print(f'Copy: {list_cpy}')

## List Comprehension
a = [1,2,3,4,5,6]
b = [x*x for x in a]

print(a)
print(b)
