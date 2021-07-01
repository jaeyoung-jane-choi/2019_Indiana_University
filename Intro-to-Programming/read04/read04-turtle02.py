#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Reading Assignment 04","Jane Choi", 'janechoi'

##############################################
import turtle


##############################################
# set up Turtle Graphics and drawing parameters:
 
# create new "drawing canvas" window, to draw in it:
myWindow = turtle.Screen()   
 
# create an object "myTurtle" that can draw:
myTurtle = turtle.Turtle()   
 

myTurtle.speed(5)
 
# set how small should details be by default:
#
smallestDetail = 200
 

 
##############################################
#   recursive Koch fractal curve function    #
##############################################
  
def koch(length): 
    if length < smallestDetail:
        myTurtle.forward(length)
    else:
        koch(length/3)
        myTurtle.left(60)
        koch(length/3)
        myTurtle.right(120)
        koch(length/3)
        myTurtle.left(60)
        koch(length/3)
 
##############################################
#           main program begins here         #
##############################################
 
print("I'm going to draw a Koch fractal curve.")
print("What's the size of the smallest detail you'd like to see?")
smallestDetail = int(input("e.g. 200 no details, smaller more details: "))
 
koch(100)
myTurtle.right(120)
koch(100)
myTurtle.right(120)
koch(100)
myTurtle.right(120)
