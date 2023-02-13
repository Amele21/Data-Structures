# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Recursions

import sys
 
# adding Stack folder to the system path
sys.path.insert(1, 'C:\\Users\\adria\\Data_Structures\\Python\\Basic_Data_Structures\\Stacks')
from stack_class import Stack

rStack = Stack()

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n % base])
        toStr(n // base, base)
    
    
        


toStr(1453,16)  # push the values onto the Stack

# pop the values from the Stack
res = ""
while not rStack.isEmpty():
    res = res + str(rStack.pop())
print(res)