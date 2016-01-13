import math
from itertools import compress

# Problem
# You have data inside of a sequence, and need to extract values or
# reduce the sequence using some criteria.

my_list = [-1, 2, 4, 5, -4, -5, 20, 3]
negative = [n for n in my_list if n < 0]
positive = [n for n in my_list if n > 0]\

# problem is if my_list is large and you can use
# a generator to produce values one by one afterwards

pos = (n for n in my_list if n > 0)
# for x in pos:
#     print(x)

# if having multiple types
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ival = list(filter(is_int, values))  # filter creates an iterator
# print(ival)
# Outputs ['1', '2', '-3', '4', '5']

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
sqrts = [math.sqrt(x) for x in mylist if x > 0]
clip_neg = [x if x > 0 else 0 for x in mylist]

# get addresses with counts larger than 5

addresses = [
    '5412 N Somedude',
    '5148 N dfsjfkd',
    '5800 N dfsdf',
    '2122 E dfhsdkjfs',
    '5645 E fdsklfjs',
    '1060 W fdksfjs',
    '4801 W fjsklfjs',
    '1039 E dfdfa'
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
# [False, False, True, False, False, True, True, False]
adrsmore5 = list(compress(addresses, more5))  # compress return an iterator

# Problem
# You want to make a dictionary that is a subset of another dictionary.

prices = {
    'ACME': 45.23,
    'AAPL': 12.33,
    'IBM': 234.00,
    'HPQ': 111.32,
    'FB': 234.11
}

# Make a dictionary for all the prices above 200
p1 = {key: value for key, value in prices.items() if value > 200}
# {'FB': 234.11, 'IBM': 234.0}
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
