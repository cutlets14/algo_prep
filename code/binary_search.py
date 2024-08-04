from bisect import bisect_left

sorted_fruits = ['apple', 'banana', 'cherry', 'durian']
bisect_left(sorted_fruits, 'banana')
# returns 1

# binary_left works in interesting ways:
# It returns the leftmost index of the element you are looking for provided it exists in the iterable.
# It may return an out-of-bounds index if the element you are looking for does exist in the iterable but it will tell you where the item should go in the iterable.
# Therefore, using bisect_left to perform binary search requires two additional checks:
# That the returned index is not out-of-bounds and the item at the returned index is equivalent to the target item

def binary_search_binary(an_iterable, item):
    index = bisect_left(an_iterable, item)

    if index <= len(an_iterable) and an_iterable[index] == item:
        return True
    return False

# Binary search written by hand
def binary_search(an_iterable, target):
    first = 0
    last = len(an_iterable) - 1

    while last >= first:
        mid = (first + last)//2

        if an_iterable[mid] == target:
            return True
        else:
            if an_iterable[mid] > target:
                last = mid - 1
            else:
                first = mid + 1
    return False

print(binary_search([1,2,3,4,5], 2))

# Binary search for characters encoded in ASCII
def binary_search_char(an_iterable, character):
    first = 0
    last = len(an_iterable) - 1

    while last >= first:
        mid = (first + last)//2

        if ord(an_iterable[mid]) == ord(character):
            return True
        elif ord(an_iterable[mid]) > ord(character):
            last = mid - 1
        elif ord(an_iterable[mid]) < ord(character):
            first = mid + 1
    return False

lst = ['a', 'z', 'q', 'm', 'r']
lst.sort()
binary_search_char(lst, 'q')