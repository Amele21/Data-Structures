# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

#  rear  [                ] front
# Queue example using the game hot potato. The queue acts like a circle.
from queue_class import Queue


def hotPotato(namelist, num):
    simqueue = Queue()

    # Names in namelist added to Queue
    for name in namelist:
        simqueue.enqueue(name)

    # Loop continues until only one player left
    while simqueue.size() > 1:
        # iterate through players removing/adding. Completely remove a player who is on num 
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))