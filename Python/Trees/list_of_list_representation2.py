# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Trees

# List of Lists Representation example 2


def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
print("start:", r)

insertLeft(r,4)
print("insert left: ", r)
insertLeft(r,5)
print("insert left: ", r)

insertRight(r,6)
print("insert right: ", r)
insertRight(r,7)
print("insert right: ", r)
print("complete: ", r)

lc = getLeftChild(r)
print("left child of root: ", lc)

rc = getRightChild(r)
print("right child of root: ", rc)

setRootVal(lc,9)
print("new lc root inserted:", r)

insertLeft(lc,11)
print("insert left: ", r)
print("right child of the right child of root:", getRightChild(getRightChild(r)))
