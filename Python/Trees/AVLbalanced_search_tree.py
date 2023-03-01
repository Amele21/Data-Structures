# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Trees

# AVL Balanced Binary Search Tree
# insertion and search O(logn) operation
import sys

class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

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
                    currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                    self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                    self._put(key,val,currentNode.rightChild)
            else:
                    currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                    self.updateBalance(currentNode.rightChild)


    # recursive helper method 
    def updateBalance(self,node):
        # 1st checks to see if the current node is out of balance enough to require rebalancing
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            # rebalancing is done and no further updating to parents is required
            self.rebalance(node)
            return
        
        # the balance factor of the parent is adjusted
        if node.parent != None:
            if node.isLeftChild():
                    node.parent.balanceFactor += 1

            elif node.isRightChild():
                    node.parent.balanceFactor -= 1

            # algorithm continues to work its way up the tree toward the 
            # root by recursively calling updateBalance on the parent
            if node.parent.balanceFactor != 0:
                    self.updateBalance(node.parent)

    # 
    def rotateLeft(self,rotRoot):
        # create a temp variable to keep track of the new root of the subtree
        # newroot the right child of the previous root
        newRoot = rotRoot.rightChild

        # replace the right child of the old root with the left child of the new root
        rotRoot.rightChild = newRoot.leftChild

        # new parent of the left child becomes the old root
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot

        # set to the parent of the old root
        newRoot.parent = rotRoot.parent

        # old root was the root of the entire tree, set new root
        if rotRoot.isRoot():
            self.root = newRoot

        else:
            # old root is a left child, point to new root
            if rotRoot.isLeftChild():
                    rotRoot.parent.leftChild = newRoot
            # old root is rith child, point to new root
            else:
                rotRoot.parent.rightChild = newRoot

        # set the parent of the old root to be the new root
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot

        # update the balance factors of the old and the new root
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)



    def rotateRight(self,rotRoot):
        # create a temp variable to keep track of the new root of the subtree
        # newroot the left child of the previous root
        newRoot = rotRoot.leftChild

        # replace the left child of the old root with the right child of the new root
        rotRoot.leftChild = newRoot.rightChild

        # new parent of the right child becomes the old root
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot

        # set to the parent of the old root
        newRoot.parent = rotRoot.parent


        if rotRoot.isRoot():
            self.root = newRoot

        else:
            if rotRoot.isRightChild():
                    rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild = newRoot

        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot

        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)


    def rebalance(self,node):
        if node.balanceFactor < 0:
                if node.rightChild.balanceFactor > 0:
                    self.rotateRight(node.rightChild)
                    self.rotateLeft(node)
                else:
                    self.rotateLeft(node)
        elif node.balanceFactor > 0:
                if node.leftChild.balanceFactor < 0:
                    self.rotateLeft(node.leftChild)
                    self.rotateRight(node)
                else:
                    self.rotateRight(node)

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
                 
    
    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.payload)
            self.printHelper(currPtr.leftChild, indent, False)
            self.printHelper(currPtr.rightChild, indent, True)



mytree = BinarySearchTree()

mytree[1]="A"
mytree[2]="B"
mytree[3]="C"



mytree.printHelper(mytree.root, "", True)
print("len: ", mytree.length())  # 3

print("root: ", mytree.root.payload)
print("leftChild: ", mytree.root.leftChild.payload)
print("rightChild: ", mytree.root.rightChild.payload)




total = 0
print('\niterations:')
i = iter(mytree.root)
print(next(i))
print(next(i))
print(next(i))
