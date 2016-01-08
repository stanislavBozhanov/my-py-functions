# Problem
# Your program has become an unreadable mess of hardcoded slice indices
# and you want to clean it up.

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
