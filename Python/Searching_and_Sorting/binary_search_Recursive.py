# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Searching

# Recursive Binary Search Version
# Slice operator in Python is O(k) so 
# binary search using slice will not perform in strict logarithmic time
def binarySearch(alist, item):
	# base case
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist) // 2
		# item found
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return binarySearch(alist[:midpoint], item)
			else:
				return binarySearch(alist[midpoint+1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))