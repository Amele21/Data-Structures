# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

# Greatest Common Disisor Function
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    # Constructor method
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

    # Standard method redefined
     def __str__(self):
         return str(self.num)+"/"+str(self.den)

    # User-defined method redefined
     def show(self):
         print(self.num,"/",self.den)

    #Standard method redefined
     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)  # To get lowest terms ie 3/6 -> 1/2

    #Standard method redefined
     def __sub__(self,otherfraction):
         newnum = self.num*otherfraction.den - self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)  # To get lowest terms ie 3/6 -> 1/2

     #Standard method redefined
     def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    #Standard method redefined
     def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    #Standard method redefined
     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum # True or False
    
      #Standard method redefined
     def __lt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum < secondnum # True or False

    #Standard method redefined
     def __gt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum > secondnum # True or False
    



x = Fraction(1,2) # We want 1/2
y = Fraction(2,3) # We want 2/3
x.show() # 1 / 2
y.show() # 2 / 3

# __str__
print(x) # 1/2 because of __str__ otherwise it would have be an object containing reference of variable (address)
print(type(x)) # Type is still object <class '__main__.Fraction'>
print(str(x)) # 1/2 string instead of object because of __str__
print(x.__str__()) #1/2 same as above

# __add__
print(x+y) # 7/6

# __sub__
print(y-x) # 2/3 - 1/2  ->   4/6 - 3/6 = 1/6

# __mul__
print(x*y) # 1/3

# __truediv__   # 1/2 / 2/3   ==   1/2 * 3/2  -> 3/4
print(x/y)

# __eq__
print(x == y) #equality changed from same reference(Shalllow Equality) to the same value (Deep Equality)

#__lt__
print(x < y) # 1/2 < 2/3  = True

#__gt__
print(x > y) # 1/2 > 2/3  = False

print(x.__gt__(y))

