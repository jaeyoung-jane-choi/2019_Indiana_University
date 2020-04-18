
#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 13", Jane Choi(Jaeyoung Choi) ,janechoi


############game


import random
from math import sqrt
import tkinter
from  tkinter  import messagebox

from  pa13Player  import Player

# ----------- global variables: -------------
gRunnerPosX = 320
gRunnerPosY = 240
gChaserPosX = 20
gChaserPosY = 60


    #added global variables:

gChaserFirst = False #bool
#when runner player first makes move to get close -> False
#when Chaser is first -> changes to True

gTicks =0 #simple integer counter, incremented by 1 every time refreshed 

gWinner = '' #simple string of winner's player name 


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

    
    global gChaserPosX
    global gChaserPosY
    global gChaserFirst
    
    if gChaserPosX>0 :
        
        gChaserPosX = gChaserPosX - 10
    
        gChaserFirst = True
    
        #since Chaser moves, gChaserFirst is changed to True 
    

def right_key(pEvent):
    """moves the x point one space to the right 

    tkinter.Event -> None """
    # print("debug: right-arrow key pressed")
    global gChaserPosX
    global gChaserPosY
    global gChaserFirst
    


    if gChaserPosX < 640:
        
        gChaserPosX = gChaserPosX + 10

        gChaserFirst = True

        #since Chaser moves, gChaserFirst is changed to True


     

def up_key(pEvent):
    """moves the y point one space up  

    tkinter.Event -> None """
    
    global gChaserPosX
    global gChaserPosY
    global gChaserFirst
    
    if gChaserPosY > 0 :
        
        gChaserPosY = gChaserPosY - 10

    
        gChaserFirst = True
  
        #since Chaser moves, gChaserFirst is changed to True




def down_key(pEvent):
    """moves the y point one space down 

    tkinter.Event-> None """
    #print("debug: down-arrow key pressed")
    global gChaserPosX
    global gChaserPosY
    global gChaserFirst
    
    
    if gChaserPosY<480:
        
        gChaserPosY = gChaserPosY +10

    
    
        gChaserFirst = True
        #print(gChaserFirst)
 
        #since Chaser moves, gChaserFirst is changed to True
   

# one "periodic handler" function, to update
#    state variables and redraw the canvas:



def refresh():
    """update the variables(chaser,runner) and redraw the canvas 

    None-> None"""

    
    # compute new position for "runner" player:
    delta_x = random.randint(-5, 5)
    delta_y = random.randint(-5, 5)
    
    global gChaserPosX
    global gChaserPosY
    global gRunnerPosY
    global gRunnerPosX
    global gChaserFirst
    global gRunnerPlayer
    global gChaserPlayer
    global gTicks
    global gWinner



    #before changing the location, first calculate the distance
            

    if gRunnerPlayer.distance_to(gChaserPlayer) <=20 and gChaserFirst == False:
        #runner hits the chaser
        gChaserPlayer.got_hit()
        
        print('Runner "hit" the Chaser!' )
        
    if gRunnerPlayer.distance_to(gChaserPlayer) <=20 and gChaserFirst == True:
        #chaser hits the runner
        gRunnerPlayer.got_hit()
        
        print('Chaser "hit" the Runner!')
    
    #change location
    
    newgRunnerPosX = gRunnerPosX + delta_x
    newgRunnerPosY = gRunnerPosY + delta_y

    if newgRunnerPosX > 0 and newgRunnerPosX <640:
        gRunnerPosX = newgRunnerPosX
        
    if newgRunnerPosY >0 and newgRunnerPosY< 480:
        gRunnerPosY = newgRunnerPosY
        
    # redraw players, by giving them their current coordinates:

    #print("debug:position setted for chaser")
    gChaserPlayer.set_position(gChaserPosX, gChaserPosY)
    print('gChaserFirst is currently ' + str(gChaserFirst))
    

    #print("debug: position setted for runner ")
    gRunnerPlayer.set_position(gRunnerPosX, gRunnerPosY)
    gChaserFirst = False #Runner position changed
    print('gChaserFirst is currently ' + str(gChaserFirst))
   
    
    

    if gRunnerPlayer.get_health() >0 and gChaserPlayer.get_health() >0:

    # schedule next call to refresh(),
    #    to happen after gMilliSeconds time
    #    e.g. 50 milliseconds = refresh 20 times/second
        gCanvas.after(gMilliSeconds, refresh)

            #ticks incremented too 
        gTicks = gTicks+1


    else:
    
        if gRunnerPlayer.get_health() <=0:
            gWinner = 'Chaser'
            print('Runner lost!'+ gWinner+ ' won in ' + str(gTicks) + ' ticks')
            
        else :
            gWinner = 'Runner'
            print('Chaser lost!'+ gWinner + ' won in ' + str(gTicks) + ' ticks')
            
        

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
gWindow.title("PA13 - runner and chaser")
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




    


#############high scores 2.0
    
choice = None
scores =[]

while choice != "0"  :
    try :
      #  print('try')
        file = open('scores.txt', 'r+')
        newscores = file.readlines()
        #print(newscores)
        scores =[]
        #for the lines in the newscores they are all string
            #by using eval, make them tuples 
        for line in newscores:
            #print(line)
            #strip out the \n
            line.strip('\n')
            line = eval(line) #tuple 
         #   print(line)
         #   print(type(line))
        
            scores.append(line) #append to new scores list 
         
          #  print(scores)
        
       # print(scores)
        
    except:
      #  print('except')
        file = open('scores.txt', 'w')
        
    

   
        
    print(
    """
    High Scores 2.0
    
    0 - Quit 
    1 - List Scores
    2 - Add the previous Score
    """
    )

    choice = input("Choice: ")

    if choice == "0":
        print("Good-bye.")

    # display high-score table
    elif choice == "1":
        print("High Scores\n")
        print("SCORE\tNAME")

        for lines in scores:
            
            print(lines)
        

# add a score
    elif choice == "2":
        
        name = gWinner
        score = int(gTicks)
        
        entry = (score, name)
        print(entry)
      #  print(scores)
 
        scores.append(entry) #append new name to scores list 

                
        #print(scores)
        scores.sort() #sort the lower scores 
       # print(scores)

        
        scores = scores[:5]
             # keep only top 5 scores
       # print(scores)
        
        file.seek(0) #make the location 0 
        
        file = open('scores.txt', 'w+')
        for lines in scores:
           #open the file to append new lines 
            file = open('scores.txt', 'a+')
            #print(lines)
            #print(file.tell())
            file.write((str(lines) +'\n'))
           # print('writing')
           # print(file.tell())
            
            read = file.read()
            #print(read)

            #close the file 
            file.close()
             
        

    
# some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")
        print("list of high scores", scores)

    
    
print()
# exit

    
