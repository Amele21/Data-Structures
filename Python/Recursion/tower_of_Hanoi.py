# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Recursions
# Tower of Hanoi

#                                  __
#        _____                     ___
#       fromPole(A)            toPole(B)           withPole(C)
#        initial                final              intermediate


# On the first recursion call, we move all but the bottom disk on the 
# initial tower to an intermediate pole. 
# On the second, we move the tower from the intermediate 
# pole to the top of the largest disk
def moveTower(height, fromPole, toPole, withPole):
    # Base case: height is 0
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole) # first
        moveDisk(fromPole,toPole)
        moveTower(height-1, withPole, toPole, fromPole) # second

# 
def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")