#
#   turtle graphics
#

# WARNING: don't name this file 
#

# Python can use external libraries
#    that are not part of the Python language,
#    but can typically provide useful
#    additional functionalities.
# NumPy is a library for numerical applications
# SciPy is another library useful for
#       scientific computation,

# turtle graphics is a simple library
#   providing "line graphics" functionalities

import turtle
# from now on in this script,
#   we can use functionality from
#   the turtle graphics library


# we need to open a 'canvas-like' window
#   into which we're going to draw ...
turtle.Screen()

# the above line uses 'dot notation' i.e.
# i.e. the function Screen() is available
#      as part of the turtle library.

# to draw something on the screen in turtle graphics,
#      we need to create (i.e. define) a
#      turtle-type variable:
lightning = turtle.Turtle()

# now that we have a turtle,
#    we can ask it to do stuff for us...

lightning.forward(100)
# the above line asks the turtle named lightning
#    to move forward by 100 points on the screen.

# we're going to draw a square
#    by combining several commands to the
#    'lightning' turtle variable:
lightning.right(90)
lightning.forward(100)
lightning.right(90)
lightning.forward(100)
lightning.right(90)
lightning.forward(100)



