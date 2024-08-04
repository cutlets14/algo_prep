# Implementing a stack using a built-in list
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]
    
# Implementing a stack using a LinkedList
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def pop(self):
        if self.head is None:
            raise IndexError("Attempted to pop from an empty stack")
        else:
            popped_item = self.head
            self.head = self.head.next
            return popped_item

# Reversing a string using a stack
def reverse_a_string(a_string):
    stack = []
    rev_string = ""

    for c in a_string:
        stack.append(c)

    for c in a_string:
        rev_string += stack.pop()

    return rev_string

revved = reverse_a_string("satvik")
print(revved)

# Min stack
# Data structure that pops and pushes and keeps track of smallest element
class MinStack():
    def __init__(self):
        self.main = []
        self.min = []

    def pop(self):
        self.min.pop()
        return self.main.pop()
    
    def push(self, data):
        if len(self.main) == 0:
            self.min.push(data)
        elif data <= self.min[-1]:
            self.min.append(data)
        else:
            self.min.append(self.min[-1])
        self.main.append(data)

    def get_min(self):
        return self.min[-1]
    
# Stacked parentheses
# Given a string, use a stack to check whether it has balanced parentheses, meaning every time there is an open parenthesis, 
# there is a subsequently closed parenthesis.
# (str(1)) - balanced
# print(Hi!)) - imbalanced

def check_parentheses(a_string):
    stack = []

    for c in a_string:
        if c in ['(']:
            stack.append(c)
        if c == [')']:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

invalid_1 = 'lee(t(c)o)de)'
invalid_2 = '))(this is valid)'
invalid_3 = "{}{{invalid}"
valid_1 = '(str(1))'
valid_2 = "{valid}"
print(check_parentheses(invalid_3))
print(check_parentheses(valid_2))

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

print(return_valid_string(invalid_2))

class MaxStack():

    def __init__(self):
        self.main = []
        self.max = []

    def push(self, num):
        self.main.append(num)

        if len(self.main) == 0:
            self.max.append(num)
        elif num >= self.max[-1]:
            self.max.append(num)
        else:
            self.max.append(self.max[-1])

    def pop(self):
        self.max.pop()
        return self.main.pop()

    def get_max(self):
        return self.max[-1]