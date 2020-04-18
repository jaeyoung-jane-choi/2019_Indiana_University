#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 12 part II", Jane Choi(Jaeyoung Choi) ,janechoi

import random
from math import sqrt
import tkinter

class Player(object):
    """a player in the game 

    Attributes: x(int: the x-coordinate), y(int: the y-coordinate), color(str), radius(float), health(int), canvas(tkinter.Canvas) """

    def __init__(self, pCanvas, pColor="white", pX=0.0, pY=0.0, pSize=10, pHealth=10):
        """contructor accepting a cavas, color, starting coordinates, size, health

        Player, tkinter.Canvas , str, int, int, int, int ->  None """

        # See Programming Assignment 12 part II instructions for details.
        self.x = pX
        self.y = pY
        self.__color = pColor
        self.__radius = pSize / 2

        self.__health = pHealth
        self.__canvas = pCanvas
        x1 = self.x - self.__radius
        y1 = self.y - self.__radius
        x2 = self.x + self.__radius
        y2 = self.y + self.__radius
        self.ID = self.__canvas.create_oval(x1, y1, x2, y2, fill=self.__color)

        
    def set_position(self, pX=0.0, pY=0.0):
        """sets the position of the player 

        Player, int, int -> None """

        self.x = pX
        self.y = pY
        x1 = self.x - self.__radius
        y1 = self.y - self.__radius
        x2 = self.x + self.__radius
        y2 = self.y + self.__radius
        self.__canvas.coords(self.ID, x1, y1, x2, y2)
        


    def distance_to(self, otherPlayer):
        """calculates the distance of the two players

        Player, Player -> float """

        distance = sqrt((self.x - otherPlayer.x)^2 + (self.y -otherPlayer.y)^2)

        return distance
