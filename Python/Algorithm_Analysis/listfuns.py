# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
import timeit


# for loop and create the list by concatenation
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

# for loop and create the list by appending
def test2():
    l = []
    for i in range(1000):
        l.append(i)

# create the list using list comprehension
def test3():
    l = [i for i in range(1000)]

# range function wrapped by a call to the list constructor
def test4():
    l = list(range(1000))


# Capture the time it takes for each of the functions to execute

t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")

t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")



popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))
print(popzero.timeit(number=1000))


x = list(range(2000000))
print(popend.timeit(number=1000))
