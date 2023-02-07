# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

from stack_class import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

#helper function for symbol-matching
def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close) # index returns lowest index in opens and closers where open and close symbols are found


print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))