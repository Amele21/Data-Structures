# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Trees

# nodes and references

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print("root object: ", r)
print("root value: ", r.getRootVal())
print("left child: ", r.getLeftChild())
print("right child: ", r.getRightChild())
print('\n')

r.insertLeft('b')
print("left child(object): ", r.getLeftChild())
print("left child value: ", r.getLeftChild().getRootVal())
print('\n')

r.insertRight('c')
print("right child(object): ", r.getRightChild())
print("right child value: ", r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print("right child new value set: ", r.getRightChild().getRootVal())