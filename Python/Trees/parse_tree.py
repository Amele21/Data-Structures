# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Trees

# Building a Parse Tree

import operator
from stack import Stack
from nodes_and_references import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree


# Function evaluates parseTree
def evaluate(parseTree):
    # use dictionary to have symbol as key, and its function operation as value
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    
    # base case when there is no leftC or rightC
    else:
        return parseTree.getRootVal()



#           *
#       3       +
#           10     5

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
et = evaluate(pt)
print("evaluated value: ", et)
# 15 * 3 
print(pt.getRootVal())                                  # *
print(pt.getRightChild().getRootVal())                  # 3

# 10 + 5 
print(pt.getLeftChild().getRootVal())                   # +
print(pt.getLeftChild().getLeftChild().getRootVal())    # 10
print(pt.getLeftChild().getRightChild().getRootVal())   # 5
#pt.postorder()  #defined and explained in the next section
