# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Trees

# Binary Search Tree
# insertion and search O(N) unbalanced tree 


class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    # makes the  BinarySearchTree().root iterable 
    def __iter__(self): 
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild


    # Goes directly to the node we want to splice out and makes the right changes
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


    # finds the successor
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                   if self.isLeftChild():
                       succ = self.parent
                   else:
                       self.parent.rightChild = None
                       succ = self.parent.findSuccessor()
                       self.parent.rightChild = self
        return succ

    # finds the minimum key in a subtree
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current


    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self



class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    # Checks to see if the tree already has a root. 
    # if no, creates a new TreeNode and install it as the root of the tree
    # if yes, calls _put
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1


    # Private, recursive helper when root node is already in place
    # Goes left if new key is less than current node, right otherwise. 
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   # if key already exists, just change payload
                   if currentNode.key == key:
                       currentNode.payload = val
                       self.size -= 1
                   else: 
                       currentNode.leftChild = TreeNode(key,val,parent=currentNode)

        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   # if key already exists, just change payload
                   if currentNode.key == key:
                       currentNode.payload = val
                       self.size -= 1
                       
                   else: 
                       currentNode.rightChild = TreeNode(key,val,parent=currentNode)


    # overload the [] operator
    def __setitem__(self,k,v):
       self.put(k,v)


    # simply searches the tree recursively until it gets to a nonmatching
    # lead node or finds a matching key
    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    # Private, recursive helper when root node is already in place
    # Goes left if new key is less than current node, right otherwise. 
    # Returns a TreeNode to get
    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)


    # Calls get, allows us to write a Python statement that 
    # looks like we are accessing a dictionary ie. z = myZipTree['Fargo']
    def __getitem__(self,key):
       return self.get(key)


    # overloads the in operator and allows for the following
    # if 'Fargo' in myZipTree
    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False


    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    # allows to use del self[key] to delete
    def __delitem__(self,key):
       self.delete(key)


    # deletes a key
    def remove(self,currentNode):
         # leaf (no children)
         if currentNode.isLeaf(): 
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
        # interior (both children)
         elif currentNode.hasBothChildren(): 
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         # this node has one child
         else: 
           if currentNode.hasLeftChild():
             # update left child reference of the parent to point to the left children of current node
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             # update right child reference of the parent to point to the right childern of current node
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             # No parent, current node is the root, so just replace data
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
                 
           else:
             # update left child reference of the parent to point to the left children of current node
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             # update right child reference of the parent to point to the right childern of current node
             elif currentNode.isRightChild():  
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             # No parent, current node is the root, so just replace data
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)




mytree = BinarySearchTree()

mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"
mytree[2]="pk"
print("mytree node: ", mytree.root.isRoot()) # True





print(mytree.length())  # 4
print(len(mytree))      # 4

print(3 in mytree)      # True
print(8 in mytree)      # False
print(mytree.get(4))    # blue
print(mytree[4])        # blue

del mytree[4]
print(mytree[4])        # None
print(len(mytree))      # 3

print(mytree[2])    # pk
print(mytree[6])    # yellow


total = 0
print('\niterations:')
i = iter(mytree.root)
print(next(i))
print(next(i))

"""
i = iter(mytree)
j = 0
print("\niteration start:")
while  j < len(mytree):
    value = next(i)
    print(value)
    
    if value != None:
        j += 1

mytree[7]="green"
mytree[8]="purple"
print("\nStarts were left off")
print(next(i))
print(next(i))
"""





