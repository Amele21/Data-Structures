# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Trees

# Binary Heap
# represented by single list
# creates a new, empty, binary heap
class BinaryHeap:
    def __init__(self):
        self.heapList = [0]  
        self.currentSize = 0 


    # percolates a new iem as far up in the tree 
    # as it needs to go to maintain the heap property
    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2


    # adds a new item to the heap
    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)


    # largest child is moved down the tree
    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc


    # return smallest child 
    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1


    # Returns the item with the minimum key value, 
    # removing the item from the heap
    # in our case the value at index 1 is the lowest value
    # last value now in the front. Perculate it down the heap
    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize] 
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)  # reorganize the heap
      return retval


    #builds a new heap from a list of keys
    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1




bh = BinaryHeap()
bh.buildHeap([9, 6, 5, 2, 3]) # built as [0,2,3,5,6,9]

# Delete each min value of the Binary Heap
print(bh.delMin())

# insert new value at the end and percup if needed
print(bh.insert(4))

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

