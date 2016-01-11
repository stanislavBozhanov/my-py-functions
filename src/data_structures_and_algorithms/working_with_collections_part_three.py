# Problem
# Your program has become an unreadable mess of hardcoded slice indices
# and you want to clean it up.

from collections import Counter
from operator import itemgetter, attrgetter


# 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100.......513.25..........'

cost = int(record[20:23])*float(record[30:36])

SHARES = slice(20, 23)
PRICE = slice(30, 36)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

# To avoid Index out of range you can bind it to a sequence
s = slice(1, 50, 2)
a = 'HelloWorld'
for i in range(*s.indices(len(a))):
    print(a[i])

# Problem
# You have a sequence of items, and you’d like to determine
# the most frequently occurring items in the sequence.

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)

sentence = 'I went in the park for the run'
letters_counts = Counter(sentence.lower())

# Under the cover Counter is a dict that maps values to counts
letters_counts['i']

more_words = [
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts_two = Counter(more_words)
# Combining counters
total_words_counts = word_counts + word_counts_two


# Problem
# You have a list of dictionaries and you would like to sort
# the entries according to one or more of the dictionary values.

# Database data for our users
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

# or

rows_by_fname_lambda = sorted(rows, key=lambda r: r['fname'])

# But itemgetter is faster

# print(rows_by_fname)
# print(rows_by_uid)

# itemgetter can accept multiple keys

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))

min_uid = min(rows, key=itemgetter('uid'))

# Problem
# You want to sort objects of the same class, but they don’t natively
# support comparison operations.


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
users_by_id = sorted(users, key=attrgetter('user_id'))


# Problem
# You have a sequence of dictionaries or instances and you want to iterate
# over the data in groups based on the value of a particular field, such as date.

rows = [
    {'address': '5122 N CLARK', 'date': '07/03/2012'},
    {'address': '5123 N BLUS', 'date': '07/02/2012'},
    {'address': '5124 N CKSD', 'date': '07/01/2012'},
    {'address': '5125 N PESD', 'date': '07/03/2012'},
    {'address': '5126 N ADGSS', 'date': '07/03/2012'},
    {'address': '5126 N EDDS', 'date': '07/01/2012'},
    {'address': '5127 N KOLL', 'date': '07/04/2012'},
    {'address': '5120 N PELS', 'date': '07/04/2012'},
]
