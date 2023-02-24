# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Stack

# top is right, base is left
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)    # O(1)

     def pop(self):
         return self.items.pop()    # O(1)

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
