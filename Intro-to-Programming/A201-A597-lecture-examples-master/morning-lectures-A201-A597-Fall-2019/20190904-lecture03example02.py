#
# turtlegraphics
#

# turtle graphics is an 'external library'
# and therefore needs to be  imported:
import turtle
#
# we need to open a 'canvas' window
# for drawing in it ...
# ... we're going to assign that new
#     window to a variable, if we need
#     to refer to it later:

# we call turtle's Screen() function,
# and we store its result into  window:
window = turtle.Screen()

# the above line uses the 'dot notation'
# i.e. it refers to a function Screen()
#      that belongs to the library turtle


# let's be optimistic, and call our
# first turtle with the name  lightning:
lightning = turtle.Turtle()
# in the above line,
# we asked the library turtle
# to execute the function Turtle()
# and we store the result into
#   the variable lightning

# the forward() function is one of the
#   functions that the turtle can execute
#   and it requires one argument:
#   i.e. how many pixels to move
lightning.forward(100)

# let's try and have the turtle change
#   direction:
lightning.right(90)


# by combining several commands,
#   we can have the turtle draw e.g.
#   a square, for simplicity
lightning.forward(100)
lightning.right(90)
lightning.forward(100)
lightning.right(90)
lightning.forward(100)
lightning.right(90)



