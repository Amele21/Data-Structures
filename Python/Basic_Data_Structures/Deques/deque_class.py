# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

# Deque
# Note: The rear and front can be flipped either end. 
#
#  rear  [                ] front
#               items

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):           # O(1)
        self.items.append(item)

    def addRear(self, item):            # O(n)
        self.items.insert(0,item)

    def removeFront(self):              # O(1)
        return self.items.pop()

    def removeRear(self):               # O(n)
        return self.items.pop(0)

    def size(self):
        return len(self.items)



if __name__ == "__main__": 
    d=Deque()
    print(d.isEmpty())  # True
    d.addRear(4)
    d.addRear('dog')
    d.addFront('cat')
    d.addFront(True)
    print(d.size())     # 4
    print(d.isEmpty())  # False
    d.addRear(8.4)
    # rear [8.4, 'dog', '4', 'cat', True] front

    print(d.removeRear())   # 8.4
    print(d.removeFront())  # True