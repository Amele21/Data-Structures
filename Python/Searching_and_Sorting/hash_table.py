# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Searching

# Complete Hash Table Example
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))

          while self.slots[nextslot] != None and self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    # Simple remainder method 
    def hashfunction(self,key,size):
         return key%size

    # plus 1 rehash function
    def rehash(self,oldhash,size):
        return (oldhash+1)%size


    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot

      while not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True

      return data
    

    def remove(self, key):
      startslot = self.hashfunction(key, len(self.slots))

      stop = False
      found = False
      position = startslot

      while self.slots[position] != None and not found and not stop:
         if self.slots[position] == key:
           found = True
           # Remove the data from slots and data
           self.slots[position] = None
           self.data[position] = None

         else:
           position=self.rehash(position, len(self.slots))
           if position == startslot:
               stop = True

      return


    # Allows function to call HashTable class method without having to put the method
    # ex. H[54]="cat" rather than H.put(54, "cat")
    def __getitem__(self,key):
        return self.get(key)


    # Allows function to call HashTable class method without having to put the method
    # ex. H[54]="cat" rather than H.get(54, "cat")
    def __setitem__(self,key,data):
        self.put(key,data)
    

    def __delitem__(self, key):
       self.remove(key)

    

    


H=HashTable()

H[54]="cat"       # __setitem__() magic method
#H.put(54,"cat")  # same as above

H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

del H[55]       # __delitem__() magic method
#H.remove(55)   # same as above

print(H.slots)
print(H.data)


print(H[20])      # __getitem__() magic method
#print(H.get(20)) # same as above

print(H[17])
H[20]='duck'
print(H[20])
print(H[99])
