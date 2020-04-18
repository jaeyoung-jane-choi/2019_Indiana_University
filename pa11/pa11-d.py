
#"A201 / Fall 2019", "Programming Assignment 11", Jane Choi, janechoi

from math import sqrt



class Dot(object):
    """represents a dot

    attributes: x(int: the x-coordinate) , y(int: the y-coordinate), color(str)"""

    def __init__(self, px,py,pcolor):
        """constructor for the dot which has the x coordinate,y coordinate,color 

        Dot , int, int , str-> None"""
        self.x = px
        self.y = py
        self.color = pcolor


    def __str__(self):
        """outputs a human readable string in the form "x: x coord,y: y coord,color: color"

        Dot -> str"""

        lString =   'x:' +str(self.x)+'\ny: '+str(self.y)+'\ncolor:'+ str(self.color) 

        #when used print() , this is outputed 
        return lString 
        
    

    def move_up(self, pint):
        """move the y point with the amount of pint 

        Dot, int -> None """
        #only move the y value 
        self.y = self.y + pint 

    def move_right(self,pint):
        """move the x point with the amount of pint 

        Dot, int -> None """
        #only move the x value 
        self.x = self.x + pint

    def distance_to(self,other):
        """returns the calculation of two dots

        Dot, Dot -> float"""
        #return the manhattan distance 
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def draw(self):
        """draws the dot with the coordinates and color 

        Dot -> turtle """
        #import  turtle 
        import turtle
        
        Window = turtle.Screen()
        turtle = turtle.Turtle()

        #lift the pen for not drawing the coordinates
        turtle.up()
        #move turtle to the coordinates 
        turtle.goto(self.x, self.y)
        #put the pen down to draw the dot 
        turtle.down()
        #color the dot with it's color
        turtle.dot(5,self.color)
        
        



############# MAIN PROGRAM #################

###E
    
print("Creating a blue Dot called dot1 with coordinates (10,20)...")
d1 =Dot(10,20,'blue')
print(d1)

print("Creating a green Dot called dot1 with coordinates (30,75)...")
d2 =Dot(30,75,'green')
print(d2)


print('Moving d1 , 15 places up')
d1.move_up(15)
print("d1 is now: " + str(d1))



print('Moving d2 , 15 places to the left ')
d2.move_right(-15)
print("d2 is now: " + str(d2))

print('Changing d1 color to red')
d1.color = 'red'
print("d1 is now: " + str(d1))



print('The distance between the two dots d1, d2 is...')
print(d1.distance_to(d2))

print('We will now draw the dots...')
d1.draw()
d2.draw()










