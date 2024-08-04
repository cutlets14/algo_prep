import array

arr = array.array('f', (1.0, 1.1, 1.2, 1.3))
# cprint(arr[1])

# TypeError: must be real number, not str
# arr[0] = 'a string'

# IndexError: array assignment index out of range
# arr[4] = 1.4

###

some_list = [1, 2, 4, 5, 6]

for a, b in enumerate(some_list):
    print(a)
    print(b)

