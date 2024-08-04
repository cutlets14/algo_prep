def move_zeros_to_back(a_list):
    zero_index = 0

    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return(a_list)

a_list = [8, 0, 3, 0, 12]
move_zeros_to_back(a_list)

print(a_list)


another_list = [8, 0, 3, 0, 12]
print(enumerate(another_list))
def move_zeros_to_front(a_list):
    last_index = len(a_list) - 1

    for index, n in reversed(list(enumerate(a_list))):
        if n == 0:
            a_list[last_index] = n
            if last_index != index:
                a_list[index] = 0
            last_index -= 1
    return a_list

move_zeros_to_front(another_list)

print(another_list)