# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Trees

# Tree Traversals

from binaryTree_nodes_and_references import BinaryTree

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())



tree = BinaryTree('book')
tree.insertLeft('Chapter1')
tree.getLeftChild().insertLeft('Section 1.1')
tree.getLeftChild().insertRight('Section 1.2')
tree.getLeftChild().getRightChild().insertLeft('Section 1.2.1')
tree.getLeftChild().getRightChild().insertRight('Section 1.2.2')

tree.insertRight('Chapter2')
tree.getRightChild().insertLeft('Section 2.1')
tree.getRightChild().insertRight('Section 2.2')
tree.getRightChild().getRightChild().insertLeft('Section 2.2.1')
tree.getRightChild().getRightChild().insertRight('Section 2.2.2')


print("------------------preorder------------------------")
preorder(tree)
print("------------------postorder------------------------")
postorder(tree)
print("------------------inorder------------------------")
inorder(tree)