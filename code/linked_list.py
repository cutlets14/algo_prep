class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def __str__(self):
        node = self.head
        output = []
        while node is not None:
            output.append(node.data)
            node = node.next
        return str(output)
    
    def search(self, target):
        current = self.head

        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False
    
    def remove(self, target):
        if self.head == target:
            self.head = self.head.next
            return
        
        current = self.head
        previous = None

        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while True:
            try:
                slow = slow.next
                fast = fast.next.next

                if slow is fast:
                    return True
            except:
                return False



a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")
a_list.append("Monday")
# print(a_list)
# a_list.remove("Wednesday")
# print(a_list)

# from collections import deque
# d = deque()
# d.append('Harry')
# d.append('Potter')

# for item in d:
#     print(item)

# import random
# a_list = LinkedList()

# for i in range(1, 101):
#     a_list.append(i)

# print(a_list)

# out = a_list.search(13)
# print(out)