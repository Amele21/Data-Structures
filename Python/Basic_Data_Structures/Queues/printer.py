# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
from queue_class import Queue
import random



# Track whether the printer has a current task
# if it does then it is busy
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    # Decrements the internal timer and sets the printer to idle when task is completed
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None  # idled

    # Returns whether printer is busy
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    # Start the next task
    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate



# Represents single printing task. 
# When the task is created, a random number generator 
# will provide a length from 1 to 20 pages
# Each task has a timestamp for computing waiting times
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


# main simulation
def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
      # call helper function
      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append( nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))


# Helper function decides whether a new printing task has been created. 
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


# 3600 sec == 60 min
# 5 is page per min
for i in range(10):
    simulation(3600,5)
