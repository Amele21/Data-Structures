# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Sorting

# O(n^2)
def insertionSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index

     while position > 0 and alist[position - 1] > currentvalue:
         alist[position] = alist[position - 1]    # shift right
         position = position - 1                  # go left

     alist[position] = currentvalue               # position found for current value

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
