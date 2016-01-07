# Problem
# You want to keep a limited history of the last
# few items seen during iteration or during
# some other kind of processing.

from collections import deque, defaultdict, OrderedDict
import heapq
import json


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


# Problem
# You want to make a list of the largest
# or smallest N items in a collection.

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

heapq.nlargest(3, portfolio, key=lambda x: x['price'])

# Problem
# You want to implement a queue that sorts
# items by a given priority and always returns
# the item with the highest priority on each pop operation.


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)  # !r calls the repr() on the arg first

q = PriorityQueue()
q.push(Item('programming'), 3)
q.push(Item('eat food'), 1)
q.push(Item('drink_water'), 2)
q.push(Item('sleep'), 2)

q.pop()  # Item('programming')
q.pop()  # Item('drink_water')
q.pop()  # Item('sleep')
q.pop()  # Item('eat food')
# If you use queue for threads you need to add
# appropriate locking  and signaling

# Problem
# You want to make a dictionary that maps keys
# to more than one value (a so-called “multidict”).

# In dict each key maps to a single value
# If you want mulitple you can use collections

# Preserve insertion order
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

# Eliminating duplicates
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(3)

# If you want to set behaviour manually

d = {}
d.setdefault('a', []).append(1)
d.setdefault('b', set()).add(2)

# Long way
d = {}
pairs = [('a', 1), ('b', 2), ('c', 3)]
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
# d = {'b': [2], 'a': [1], 'c': [3]}

# Better way
d = defaultdict(list)
pairs = [('a', 1), ('b', 2), ('c', 3)]
for key, value in pairs:
    d[key].append(value)

# Problem
# You want to create a dictionary, and you also want to
# control the order of items when iterating or serializing.

# Size of OrderedDict is almost twise as large as normal dict
d = OrderedDict()
d['stenly'] = 24
d['viki'] = 21
d['Anna'] = 20

for key in d:
    print(key, d[key])
# prints in the order added
# easy for serializing
j = json.dumps(d)

# Problem
# You want to perform various calculations
# (e.g., minimum value, maximum value, sort‐ing, etc.)
# on a dictionary of data.

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Zip creates an iterator that can be used only once
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
print(max(prices_and_names))  # ValueError: max() arg is an empty sequence


# Problem
# You have two dictionaries and want to find out
# what they might have in common (samekeys, same values, etc.).

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Using set operations
a.keys() & b.keys()  # { 'x', 'y'}

# Make a dictionary from some keys
c = {key: a[key] for key in a.keys() - {'z', 'w'}}

# item() and keys() support set operations values() doesn't
# because unlike keys() values() can contain duplicates
