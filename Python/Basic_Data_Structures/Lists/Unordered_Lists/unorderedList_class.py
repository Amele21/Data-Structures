# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# https://gist.github.com/cyyeh/f292faf1060b92bb9d4556e26aeae478 
# Meant for pratice and note taking

# Node contains the item itself aka data field
# and each node holds a reference to the next node
class Node:
    # constructor
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    # get value from node
    def getData(self):
        return self.data

    # get next node reference
    def getNext(self):
        return self.next

    # set value to node
    def setData(self,newdata):
        self.data = newdata

    # set next node reference
    def setNext(self,newnext):
        self.next = newnext




class UnorderedList:
    # constructor
    def __init__(self):
        self.head = None
    

    # prints all the values of the linked list
    def getAll(self):
        current = self.head
       
        while current != None:
            print(current.data, end=' ')
            current = current.getNext()
        print()
            

    # check if the list is empty
    def isEmpty(self):
        return self.head == None


    # insert item at the start(head)
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp


    # size of the list
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count


    # find item in the list
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


    # remove item from the list
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    # insert item at the end of the list
    def append(self, item):
        current = self.head
        temp = Node(item)
        previous = None

        while current != None:
            previous = current
            current = current.getNext()
        
        previous.setNext(temp)
    

    # insert item in the pos positon of the list
    def insert(self, pos, item):
        current = self.head
        previous = None
        index = 0
        temp = Node(item)
    
        while current != None and index < pos:
            previous = current
            current = current.getNext()
            index += 1
    
        if pos == 0:
            temp.setNext(self.head)
            self.head = temp      
        else:
            if current == None:
                previous.setNext(temp)
            else:
                temp.setNext(current)
                previous.setNext(temp)


    # Get the index of the item in the list
    def index(self, item):
        current = self.head
        found = False
        index = 0
    
        while current != None and not found:
            if current.getData() != item:
                index +=1
                current = current.getNext()
            else:
                found = True
        
        if found:
            return index
        else:
            return "Not Found"


    # remove last item of the list
    def pop(self):
        current = self.head
        previous = None
    
        if current == None:
            return "No item in list"
    
        while current.getNext() != None:
            previous = current
            current = current.getNext()
    
        previous.setNext(None)
        return current.getData()


    # remove item from the pos position of the list
    def delete(self, pos):
        current = self.head
        previous = None
        index = 0
    
        if current == None:
            return "No item in list"
    
        while index < pos and current != None:
            previous = current
            current = current.getNext()
            index += 1
      
        if current == None:
            return "No item in list"
        else:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

        return current.getData()




mylist = UnorderedList()

# add method
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
# [54, 26, 93, 17, 77, 31]

# search and size methods
print(mylist.size())        # 6
print(mylist.search(93))    # True
print(mylist.search(100))   # False

mylist.add(100)
print(mylist.search(100))   # True
print(mylist.size())        # 7
# [100, 54, 26, 93, 17, 77, 31]

# remove method
mylist.remove(54)           
print(mylist.size())        # 6
mylist.remove(93)
print(mylist.size())        # 5
print(mylist.search(93))    # False
# [100, 26, 17, 77, 31]

# pop method
print(mylist.search(31))    # True
print(mylist.pop())         # 31
print(mylist.search(31))    # False
# [100, 26, 17, 77]

# append method
mylist.append(43)
# [100, 26, 17, 77, 43]

# index method
print(mylist.index(43))     # 4
mylist.getAll()

# insert method
mylist.insert(2, 99)
mylist.getAll()
# [100, 26, 99, 17, 77, 43]

# delete method
mylist.delete(1)
mylist.getAll()
# [100, 99, 17, 77, 43]
