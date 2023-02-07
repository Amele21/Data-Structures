# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

# top is left,  base is right
class Stack:
    def __init__(self):
        self.items = []
	
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)       # O(n)
	
    def pop(self):
        return self.items.pop(0)        # O(n)
	
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
	
s = Stack()
s.push('hello')
s.push('true')
# ["true", "hello"]
print(s.pop())  # true
 