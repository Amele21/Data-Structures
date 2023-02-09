# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
from deque_class import Deque

# Palindrome-Checker function. String that reads the same forward and backwards.
def palchecker(aString):
    chardeque = Deque()

    # add items through rear
    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    # remove items from rear and front. Check if they are equal. 
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))