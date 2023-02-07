# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

# top is right, base is left
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s=Stack()

print(s.isEmpty()) # True
s.push(4)
s.push('dog')
#['4', 'dog']
print(s.peek())     # dog
s.push(True)
print(s.size())     # 3
print(s.isEmpty())  # False
s.push(8.4)
print(s.pop())      # 8.4
print(s.pop())      # True
print(s.size())     # 2


