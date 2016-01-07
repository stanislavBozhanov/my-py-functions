# Problem
# You have an N-element tuple or sequence that you would like to unpack into a collection
# of N variables.

p = (4, 5)
a, b = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

# You can unpack any object that is iterable
s = 'Hello'
a, b, c, d, e = s

# Unpacking and discarding some varibales
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data

# Unpacking elements from iterables of arbitrary length
# Problem
# You run a course and decide at the end of the semester that
# you’re going to drop the first and last homework grades, and
# only average the rest of them.


def avg(grades):
    return sum(grades) / len(grades)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('Dave', 'dave@abv.bg', '565-5646-6456', '54-5345-5345-354')
name, email, *phone_numbers = record
# phone_numbers = ['565-5646-6456', '54-5345-5345-354']

daily_income = [11, 12, 34, 435, 45, 23, 234]
*previous_days, today = daily_income
avg_past_incomes = sum(previous_days) / len(previous_days)


# Star expression in string unpacking
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')


sequence = [1, 2, 3, 4, 5, 6]
head, *tail = sequence


# Recursion isn't a strong python feathure
# Avoid using it
def sum_seq(items):
    head, *tail = items
    return head + sum_seq(tail) if tail else head
