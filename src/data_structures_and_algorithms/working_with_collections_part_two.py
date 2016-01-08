# Problem
# You want to eliminate the duplicate values in a sequence,
# but preserve the order of the remaining items.

a = [1, 5, 2, 3, 1, 4, 3, 5, 6, 7, 8, 9]


# Only works for hashable items (dicts are not)
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a_unique_same_order = list(dedupe(a))


# Include dict support
def dedupe_dict(items, key=None):
    seen = set()
    for item in items:
        val = item if key in None else key(item)
        if val not in seen:
            yield val
            seen.add(val)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
list(dedupe_dict(a, key=lambda d: (d['x'], d['y'])))
