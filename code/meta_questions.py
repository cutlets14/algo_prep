# Toeplitz Matrix
# Given an m x n matrix, determine if the given matrix is a Toeplitz matrix.
# A Toeplitz matrix is one in which every diagonal from top-left to bottom-right has the same elements.

def isToeplitzMatrix(matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
        
    return True

print(isToeplitzMatrix([[1, 2, 3], [4, 1, 2], [5, 4, 1]]))  # true
print(isToeplitzMatrix([[1, 2], [3, 4]]))  # false
print(isToeplitzMatrix([[7, 7, 7], [7, 7, 7], [7, 7, 7]]))  # true
    
# Remove all adjacent duplicates in string
def remove_adjacent_duplicates(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

print(remove_adjacent_duplicates("abccba")) # empty
print(remove_adjacent_duplicates("foobar")) # fbar
print(remove_adjacent_duplicates("abcd")) # abcd

# Valid palindrome
# To determine if a given string s can be made into a palindrome by deleting at most one character, 
# we can use a two-pointer technique to check for palindromic properties.
def valid_palindrome(s):
    def is_palindrome_range(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            # Skip either the left character or the right character
            return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)
        left += 1
        right -= 1

    return True

# Example usage
s = "abca"
print(valid_palindrome(s))  # Output: True

# Minimum remove to make valid parentheses
# Variation where a valid string is returned
def return_valid_string(a_string):
    stack = []
    to_remove = set()

    for i, char in enumerate(a_string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                print(stack)
                stack.pop()
                print(stack)
            else:
                to_remove.add(i)
                print(to_remove)
    to_remove = to_remove.union(set(stack))

    result = ''.join(char for i, char in enumerate(a_string) if i not in to_remove)

    return result

## Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Base case: if root is None, or root is one of p or q, return root
    if root is None or root == p or root == q:
        return root
    
    # Recurse on the left and right subtrees
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    # If both left and right are not None, root is the LCA
    if left is not None and right is not None:
        return root
    
    # Otherwise, return the non-None child (either left or right)
    return left if left is not None else right
