# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

from stack_class import Stack

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF" # for remainder beyond base 10, two digit remainders use A-F

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))  # binary
print(baseConverter(25,16)) # hexadecimal