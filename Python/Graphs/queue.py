# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

# Queue
# Note: The rear and front can be flipped either end. 
#
#  rear  [                ] front
#               items


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):                # O(n)
        self.items.insert(0,item)

    def dequeue(self):                      # O(1)
        return self.items.pop()

    def size(self):
        return len(self.items)