# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Searching

# Sequential Search of a List of Integers
#       [1, 2, 32, 8, 17, 19, 42, 13, 0]
# Start  -> -> -> -> -> -> -> -> -> -> 
# Starting at the first item in the list, 
# we simply move from item to item, following the 
# underlying sequential ordering until we either find 
# what we are looking for or run out of items.

# O(n) unordered list
def sequentialSearch(alist, item):
    pos = 0
    found = False
	
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
          pos = pos+1
    
    return found
	

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))    # False
print(sequentialSearch(testlist, 13))   # True