# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Searching


# Simple Hash Function for Strings
# cat => 99 97 116 : ordinal values
# multiply each value by the positon(ordinal values with weighting)
# c is 1, a is 2, and t is 3
# 99*1 + 97*2 + 116*3
# Add them all and mod by the table size
# 641 % 11 = 3. Hash value is 3
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])*(pos+1)

    return sum%tablesize


astring = 'cat'
tablesize = 11
print(hash(astring, tablesize))
