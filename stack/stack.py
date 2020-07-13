"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # return len(self.storage)
        curr = self.storage.head
        count = 0
        if curr == None:
            return 0
        while curr:
            if curr:
                count += 1
            curr = curr.get_next()
        return count


    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_tail()
         
 
 
s = Stack()
s.push(10)
s.push(8)
s.push(7)
print(s.pop())

print(s.__len__())

# s.__len__()
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         length = len(self.storage)
#         return length

#     def push(self, value):
#         return self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             value = self.storage.pop()
            # return value
