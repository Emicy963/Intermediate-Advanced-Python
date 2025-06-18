# Sets: unordered, mutable, no duplicate
# myset = {1,2,3}
# print(myset)

# myset = set('Hello')
# print(myset)

# myset = set()

# myset.add(1)
# myset.add(2)
# myset.add(3)

# myset.remove(4)
# myset.discard(2)
# myset.pop()

# for x in myset:
#     print(x)

# if 1 in myset:
#     print('yes')
# else:
#     print('no')

# odds = {1,3,5,7,9}
# evens = {0,2,4,6,8}
# primes = {2,3,5,7}

# u = odds.union(evens)
# print(u)

# i = odds.intersection(primes)
# print(i)

# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12}

# diff = setA.difference(setB)
# print(diff)
# diff = setB.difference(setA)
# print(diff)
# diff = setB.symmetric_difference(setA)
# print(diff)

# setA.update(setB)

# setA.intersection_update(setB)

# setA.difference_update(setB)

# setA.symmetric_difference_update(setB)
# print(setA)

# setA = {1,2,3,4,5,6}
# setB = {1,2,3}
# setC = {7,8}

# print(setA.issubset(setB)) - Return false
# print(setB.issubset(setA)) - Return true
# print(setB.issuperset(setA)) - Returns false
# print(setA.issuperset(setB)) - Return true
# print(setA.isdisjoint()) - Return false
# print(setA.isdisjoint(setC)) - Return true

# setB = setA.copy()
# setB = set(setA)

# print(setB)
# setB.add(7)
# print(setB)
# print(setA)

# a = frozenset([1,2,3,4])
# # Frozenset type is immutabble
# print(a)
