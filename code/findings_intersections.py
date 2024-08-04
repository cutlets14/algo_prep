## Given an array of non-negative integers, return an array consisting of all the even elements of the array first followed by all the odd elements of the array.

def even_first_then_odd(an_iterable) -> list:
    evens = []
    odds = []

    for item in an_iterable:
        if item % 2 == 0:
            evens.append(item)
        elif item % 2 != 0:
            odds.append(item)
    
    return evens + odds

print(even_first_then_odd([400, 12, 1, 12, 13, 57, 6, 95, 11, 20, 10]))