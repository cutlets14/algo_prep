# Manual bubble sort

def bubble_sort(an_iterable):
    iter_length = len(an_iterable) - 1

    for i in range(iter_length):
        print("#############")
        print(f"This is the {i}th iteration.")
        print("#############")
        for j in range(iter_length):
            print(f"This is index j: {j}.")
            print(f"Element at index j: {an_iterable[j]}")
            print(f"Element at index j+1: {an_iterable[j+1]}")
            if an_iterable[j] > an_iterable[j+1]:
                an_iterable[j], an_iterable[j+1] = an_iterable[j+1], an_iterable[j]
                print(f"Inner loop - Element at index j: {an_iterable[j]}")
                print(f"Inner loop - Element at index j + 1: {an_iterable[j + 1]}")
    return an_iterable

print(bubble_sort([22,4,56,1,345,7]))