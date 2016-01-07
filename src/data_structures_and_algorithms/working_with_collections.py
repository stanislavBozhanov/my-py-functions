# Problem
# You want to keep a limited history of the last
# few items seen during iteration or during
# some other kind of processing.

from collections import deque
import heapq


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
