#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 12 part II", Jane Choi(Jaeyoung Choi) ,janechoi

import random
import tkinter
from  tkinter  import messagebox

from  pa12Player  import Player

# ----------- global variables: -------------
gRunnerPosX = 320
gRunnerPosY = 240
gChaserPosX = 20
gChaserPosY = 60

# screen refresh rate, e.g.
#    50 milliseconds means: refresh canvas 20 times/second
gMilliSeconds = 50

# player variables for the game are declared here, and instantiated below:
gRunnerPlayer = None
gChaserPlayer = None

# TKinter-related variables are 
#    also declared here, and instantiated below:
gWindow = None
gCanvas = None



# ----------- useful functions: -------------
#
# TKinter binding and events are described here:
#   https://docs.python.org/3/library/tkinter.html#bindings-and-events

# four "event handler" functions, to handle key-press events:
def left_key(pEvent):
    """moves the x point one space to the left 

    tkinter.Event ->None"""
    
    #print("debug: left-arrow key pressed")
    #print("debug: pEvent" + str(pEvent))
    #print("debug: pEvent.widget" + str(pEvent.widget))
    print("debug: pEvent.widget.winfo_width()" + str(pEvent.widget.winfo_width()))
    print("debug: pEvent.widget.winfo_height()" + str(pEvent.widget.winfo_height()))

    global gChaserPosX

    if gChaserPosX>0 :
        gChaserPosX = gChaserPosX - 1
    #print("debug left-arrow key pressed.")

    

def right_key(pEvent):
    """moves the x point one space to the right 

    tkinter.Event -> None """
    # print("debug: right-arrow key pressed")
    global gChaserPosX

    if gChaserPosX < 640:
        gChaserPosX = gChaserPosX + 1

def up_key(pEvent):
    """moves the y point one space up  

    tkinter.Event -> None """
    
    # print("debug: up-arrow key pressed")
    global gChaserPosY
    if gChaserPosY > 0 : 
        gChaserPosY = gChaserPosY - 1

def down_key(pEvent):
    """moves the y point one space down 

    tkinter.Event-> None """
    # print("debug: down-arrow key pressed")
    global gChaserPosY
    if gChaserPosY<480: 
        gChaserPosY = gChaserPosY + 1

# one "periodic handler" function, to update
#    state variables and redraw the canvas:
def refresh():
    """update the variables(chaser,runner) and redraw the canvas 

    None-> None"""
    # compute new position for "runner" player:
    delta_x = random.randint(-5, 5)
    delta_y = random.randint(-5, 5)
    global gRunnerPosX
    global gRunnerPosY
    
    newgRunnerPosX = gRunnerPosX + delta_x
    newgRunnerPosY = gRunnerPosY + delta_y

    if newgRunnerPosX > 0 and newgRunnerPosX <640:
        gRunnerPosX = newgRunnerPosX
       
    if newgRunnerPosY >0 and newgRunnerPosY< 480:
         gRunnerPosY = newgRunnerPosY


    # redraw players, by giving them their current coordinates:
    gRunnerPlayer.set_position(gRunnerPosX, gRunnerPosY)
    gChaserPlayer.set_position(gChaserPosX, gChaserPosY)

    

    # schedule next call to refresh(),
    #    to happen after gMilliSeconds time
    #    e.g. 50 milliseconds = refresh 20 times/second
    gCanvas.after(gMilliSeconds, refresh)


# one "event handler" to properly dispose of Tk resources
#    when the "close button" is selected in the game window:
def closeProgram():
    """closes down the program

    None -> None """
    global gWindow
    if tkinter.messagebox.askokcancel("Quit Game", \
         "Quit the Game?"):
        gWindow.destroy()





# ----------- main program begins here: -------------

# create top-level User Interface element for Tk, i.e. a GUI window:
gWindow = tkinter.Tk()
# give a title to the window:
gWindow.title("PA12 part II - runner and chaser")
# for this game, make the window not resizable by user
#   (the window will assume the size of its content, defined below)
gWindow.resizable(False,False)

# create a graphics Canvas object (where we'll draw the game's Players)
#    define the Canvas as content to gWindow object,
#    and set the Canvas's size to 640 x 480 pixels:
gCanvas = tkinter.Canvas(gWindow, width = 640, height = 480)
# ask the Canvas to display itself, resizing its window necessary:
#    https://docs.python.org/3/library/tkinter.html#the-packer
gCanvas.pack()

# connect "event handler" functions to keyboard keys that
#    we'll use to control the "Chaser" player on canvas:
gWindow.bind('<Left>', left_key)
gWindow.bind('<Right>', right_key)
gWindow.bind('<Up>', up_key)
gWindow.bind('<Down>', down_key)

# connect "event handler" function to quit the game
#    when the "close button" is selected in the game window:
gWindow.protocol("WM_DELETE_WINDOW", closeProgram)


# create two players:
gRunnerPlayer = Player(gCanvas, "red", gRunnerPosX, gRunnerPosY)
gChaserPlayer = Player(gCanvas, "green", gChaserPosX, gChaserPosY)


# manually place a first call to the refresh function:
refresh()

# start an infinite loop, while events get processed:
gWindow.mainloop()

