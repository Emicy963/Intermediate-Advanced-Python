# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
# from collections import Counter

## Counter
# a = 'aaabbbccc'
# mycounter = Counter(a)
# print(mycounter.items())
# print(mycounter.values())

# print(mycounter.most_common(1))
# print(list(mycounter.elements()))

# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(1,-4)
# print(pt)
# print(pt.x,pt.y)

# from collections import OrderedDict

# ordered_dict = OrderedDict()
# ordered_dict['a'] = 1
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4

# print(ordered_dict)

# from collections import defaultdict
# b = defaultdict(int)
# b['a'] = 1
# b['b'] = 2
# print(b['a'])

from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

# d.pop()
# d.popleft()
# d.clear()

# d.extend([4,5,6])
# d.extendleft([4,5,6])

# d.rotate(-1)
# print(d)
