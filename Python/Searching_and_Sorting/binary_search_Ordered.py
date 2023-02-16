# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Searching

# Binary Search
# start by examining the middle item. 
# If that item is the one we are searching for, 
# we are done. If it is not the correct item, we can use the 
# ordered nature of the list to eliminate half of the remaining items. 
# If the item we are searching for is greater than the middle item, 
# we know that the entire lower half of the list as well as the middle item 
# can be eliminated from further consideration.

# Binary Search of an Ordered List
# O(logn)
def binarySearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = False
	while first <= last and not found:
		midpoint = (first + last) // 2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	
	return found
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))