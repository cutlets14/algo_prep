import sys

def merge(left_array, right_array):

    # Check if either array is empty
    if len(left_array) == 0:
        return right_array
    
    if len(right_array) == 0:
        return left_array
    
    # By now, we know that neither array is empty
    result = []
    left_index = right_index = 0

    while len(result) < len(left_array) + len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            result.append(left_array[left_index])
            left_index += 1
        else:
            result.append(right_array[right_index])
            right_index += 1
    
        # Check if we are at the end of each array
        if left_index == len(left_array):
            result += right_array[right_index:]
            break
        
        if right_index == len(right_array):
            result += left_array[left_index:]
            break

    return result

def merge_sort(input):
    # Check for base case
    if len(input) < 2:
        return input
    
    # Split array into two
    midpoint = len(input) // 2

    left_array = input[:midpoint]
    right_array = input[midpoint:]

    return merge(merge_sort(left_array), merge_sort(right_array))

def main():
    output = merge_sort([5, 4, 7, 99, 0, 404, 69])
    print(output)

if __name__ == "__main__":
    main()