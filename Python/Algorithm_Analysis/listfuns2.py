# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
import timeit

popzero = timeit.Timer("x.pop(0)","from __main__ import x")
popend = timeit.Timer("x.pop()","from __main__ import x")

x = list(range(2000000))
print(popzero.timeit(number=1000))


x = list(range(2000000))
print(popend.timeit(number=1000))
