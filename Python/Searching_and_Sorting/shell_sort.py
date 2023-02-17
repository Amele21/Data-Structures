# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Sorting


# This shellsort performs at O(n^2)
# typically, shellsort performs between O(n) and O(n^2)
# sublist starts at every 4, then every 2, and then every 1
# each sublist gets sorted 
def shellSort(alist):
    sublistcount = len(alist) // 2

    # sublist goes from 4, 2, 1. Ends at 0
    while sublistcount > 0:
      # go through each start position. So for first round sublist 4. index 0 - 3
      # second round sublist 2: index 0-1 , third round sublist 1: index 0
      for startposition in range(sublistcount):
        gapInsertionSort(alist, startposition, sublistcount)

      print("After increments of size", sublistcount, "The list is", alist)
      sublistcount = sublistcount // 2

# sort the values based on start position and gap
def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
