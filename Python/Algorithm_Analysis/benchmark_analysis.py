# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

#Example of Benchmark analysis
# NOTE Dependent on machine, program, time of day, compiler, and programming language.
 
import time

def sumOfN(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()

   return theSum,end-start

#time to finish run increases as n increases
for i in range(5):
       print("N: Sum is %d required %10.7f seconds"%sumOfN(10000))

for i in range(5):
    print("N: Sum is %d required %10.7f seconds"%sumOfN(100000))

for i in range(5):
    print("N: Sum is %d required %10.7f seconds"%sumOfN(1000000))



def sumOfN2(n):
    start = time.time()
    sum = (n*(n+1))/2
    end = time.time()

    return sum, end-start

#time to finish run DOES not change as much as sumofN
for i in range(5):
       print("N2: Sum is %d required %10.7f seconds"%sumOfN2(10000))

for i in range(5):
    print("N2: Sum is %d required %10.7f seconds"%sumOfN2(100000))

for i in range(5):
    print("N2: Sum is %d required %10.7f seconds"%sumOfN2(1000000))