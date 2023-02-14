# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Recursions

import turtle


# Draws a filled triangle using the begin_fill and end_fill turtle methods
# Each degree of the Sierpinski triangle is drawn in a different color
def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()


# Takes as arguments two endpoints and returns the point halfway between them
def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)


# Three way recursive algorithm
# Degree serves as the base case when less than zero.
# Each Degree is a different color
# Order: lower left, top, lower right
# Starts at 'first' and goes all the way in until degree is zero. (LOWER LEFT)
    ## Then it works its way back calling 'first', 'second', and 'third'
    ## Goes back another degree and go through 'first', 'second', and 'third'
    ## Repeat above until back at degree three
# Now starts at 'second' and goes all the way in until degree is zero. (TOP)
    ## same as sub-steps above
# Then starts at 'third' and goes all the way in until degree is zero. (LOWER RIGHT)
    ## same as sub-steps above
def sierpinski(points, degree, myTurtle):
    colormap = ['blue','red','green','white','yellow','violet','orange']

    drawTriangle(points, colormap[degree], myTurtle)

    if degree > 0:
        # first    
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])],
                    degree-1, 
                    myTurtle)
        # second
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])],
                   degree-1, 
                   myTurtle)
        # third
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])],
                   degree-1,
                   myTurtle)




def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints, 3, myTurtle) # points, degree, myTurtle
   myWin.exitonclick()

main()
