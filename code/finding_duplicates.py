## Finding duplicates using for loops
## O(n^2)

def find_duplicates(an_iterable):
    dups = []

    for i in range(len(an_iterable)):
        for j in range(i + 1, len(an_iterable)):
            if an_iterable[i] == an_iterable[j] and an_iterable[i] not in dups:
                dups.append(an_iterable[i])
    
    return dups


an_iterable = [12, 1, 15, 16, 12, 15, 20, 21, 16]
dups = find_duplicates(an_iterable)
print(dups)

## Finding dups using a set
## O(n)

def find_dups(an_iterable):
    dup_set = set()
    dups = []

    for item in an_iterable:
        l1 = len(dup_set)
        dup_set.add(item)
        l2 = len(dup_set)

        if l1 == l2:
            dups.append(item)

    return dups

an_iterable = [12, 1, 15, 16, 12, 15, 20, 21, 16]
dups = find_dups(an_iterable)
print(dups)

## Finding duplicates using Collections
## Collections are specialized container datatypes providing alternatives to Python's general purpose built-in containers
## A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
from collections import Counter
an_iterable = [20, 30, 25, 20]

dups = [item for item, value in Counter(an_iterable).items() if value > 1]
print(dups)





