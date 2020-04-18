Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13Player.py 
>>> gRunnerPosX = 320
>>> gRunnerPosY = 240
>>> gRunnerPlayer = Player(gCanvas, "red", gRunnerPosX, gRunnerPosY,10,0)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    gRunnerPlayer = Player(gCanvas, "red", gRunnerPosX, gRunnerPosY,10,0)
NameError: name 'gCanvas' is not defined
>>> gCanvas = None

>>> gRunnerPlayer = Player(gCanvas, "red", gRunnerPosX, gRunnerPosY,10,0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    gRunnerPlayer = Player(gCanvas, "red", gRunnerPosX, gRunnerPosY,10,0)
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13Player.py", line 28, in __init__
    self.ID = self.__canvas.create_oval(x1, y1, x2, y2, fill=self.__color)
AttributeError: 'NoneType' object has no attribute 'create_oval'
>>> gCanvas = tkinter.Canvas(gWindow, width = 640, height = 480)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    gCanvas = tkinter.Canvas(gWindow, width = 640, height = 480)
NameError: name 'gWindow' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py", line 7, in <module>
    from  pa12Player  import Player
ModuleNotFoundError: No module named 'pa12Player'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py", line 7, in <module>
    from  pa12Player  import Player
ModuleNotFoundError: No module named 'pa12Player'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
>>> gChaserPlayer = Player(gCanvas, "green", gChaserPosX, gChaserPosY,10,0)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    gChaserPlayer = Player(gCanvas, "green", gChaserPosX, gChaserPosY,10,0)
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13Player.py", line 28, in __init__
    self.ID = self.__canvas.create_oval(x1, y1, x2, y2, fill=self.__color)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 2495, in create_oval
    return self._create('oval', args, kw)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 2480, in _create
    *(args + self._options(cnf, kw))))
_tkinter.TclError: invalid command name ".!canvas"
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 1705, in __call__
    return self.func(*args)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 749, in callit
    func(*args)
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py", line 169, in refresh
    if gRunnerPlayer.distance_to(gChaserPlayer) <20 & gChaserFirst == False:
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13Player.py", line 83, in distance_to
    distance = sqrt((self.x - otherPlayer.x)^2 + (self.y -otherPlayer.y)^2)
ValueError: math domain error
debug: pEvent.widget.winfo_width()646
debug: pEvent.widget.winfo_height()486
debug: pEvent.widget.winfo_width()646
debug: pEvent.widget.winfo_height()486
debug: pEvent.widget.winfo_width()646
debug: pEvent.widget.winfo_height()486
debug: pEvent.widget.winfo_width()646
debug: pEvent.widget.winfo_height()486

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 1705, in __call__
    return self.func(*args)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 749, in callit
    func(*args)
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py", line 168, in refresh
    if gRunnerPlayer.distance_to(gChaserPlayer) <20 & gChaserFirst == False:
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13Player.py", line 83, in distance_to
    distance = sqrt((self.x - otherPlayer.x)^2 + (self.y -otherPlayer.y)^2)
ValueError: math domain error

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 1705, in __call__
    return self.func(*args)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 749, in callit
    func(*args)
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py", line 169, in refresh
    if gRunnerPlayer.distance_to(gChaserPlayer) <20 & gChaserFirst == False:
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13Player.py", line 83, in distance_to
    distance = sqrt((self.x - otherPlayer.x)^2 + (self.y -otherPlayer.y)^2)
ValueError: math domain error
>>> gRunnerPlayer.distance_to(gChaserPlayer)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    gRunnerPlayer.distance_to(gChaserPlayer)
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13Player.py", line 83, in distance_to
    distance = sqrt((self.x - otherPlayer.x)^2 + (self.y -otherPlayer.y)^2)
ValueError: math domain error
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 1705, in __call__
    return self.func(*args)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 749, in callit
    func(*args)
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py", line 169, in refresh
    if gRunnerPlayer.distance_to(gChaserPlayer) <20 & gChaserFirst == False:
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13Player.py", line 83, in distance_to
    distance = sqrt((self.x - otherPlayer.x)^2 + (self.y -otherPlayer.y)^2)
ValueError: math domain error

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
change position
>>> gRunnerPlayer.distance_to(gChaserPlayer)
342.81190177705327
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
>>> gRunnerPlayer.distance_to(gChaserPlayer)
46.32493928760188
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
>>> gRunnerPlayer.distance_to(gChaserPlayer)
5.0
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py", line 245, in <module>
    refresh()
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py", line 151, in refresh
    while gRunnerPlayer.get_heatlh() >0 and gChaserPlayer.get_heatlh() >0:
AttributeError: 'Player' object has no attribute 'get_heatlh'
>>> 
Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
The player's health is at 0 or below
The player's health is at 0 or below
The player's health is at 0 or below
The player's health is at 0 or below
The player's health is at 0 or below
The player's health is at 0 or below
The player's health is at 0 or below
The player's health is at 0 or below
The player's health is at 0 or below
The player's health is at 0 or below
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
The player's health is at 0 or below
Runner has got hit
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 

=============================== RESTART: Shell ===============================
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
One of the player has reached health of 0
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Chaser lost! Runner won in 151 ticks
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Chaser lost! Runner won in 160 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Runner has got hit
Chaser lost! Runner won in 108 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
debug: left-arrow key pressed
debug: left-arrow key pressed
gChaserFirstFalse
debug: left-arrow key pressed
debug: left-arrow key pressed
gChaserFirstFalse
debug: left-arrow key pressed
debug: left-arrow key pressed
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstFalse
debug: left-arrow key pressed
debug: left-arrow key pressed
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
debug: left-arrow key pressed
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
Chaser lost! Runner won in 103 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
debug: left-arrow key pressed
gChaserFirstFalse
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
Runner has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
Chaser lost! Runner won in 85 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
Runner has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
Chaser lost! Runner won in 85 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
<class 'NoneType'>
gChaserFirstFalse
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
Chaser lost! Runner won in 94 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
Chaser lost! Runner won in 123 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstTrue
Runner has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
Chaser lost! Runner won in 159 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
Runner has got hit
Chaser lost! Runner won in 86 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser lost! Runner won in 73 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser lost! Runner won in 60 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner has got hit
gChaserFirstTrue
Chaser has got hit
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Chaser has got hit
gChaserFirstFalse
Chaser lost! Runner won in 202 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Chaser lost! Runner won in 70 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Chaser lost! Runner won in 102 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py", line 276, in <module>
    refresh()
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py", line 176, in refresh
    if originalY == gChaserPosY  and originalX == gChaserPosY :
NameError: name 'originalY' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser lost!Runner won in 78 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Runner "hit" the Chaser!
gChaserFirstFalse
Chaser lost!Runner won in 98 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser lost!Runner won in 65 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser lost!Runner won in 130 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser lost!Runner won in 60 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
gChaserFirstTrue
Chaser "hit" the Runner!
Chaser lost!Runner won in 69 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
9
gChaserFirstTrue
Chaser "hit" the Runner!
8
gChaserFirstTrue
Chaser "hit" the Runner!
7
gChaserFirstTrue
Chaser "hit" the Runner!
6
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
5
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
4
gChaserFirstTrue
Chaser "hit" the Runner!
3
gChaserFirstTrue
Chaser "hit" the Runner!
2
gChaserFirstTrue
Chaser "hit" the Runner!
1
gChaserFirstTrue
Chaser "hit" the Runner!
0
Chaser lost!Runner won in 61 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
9
gChaserFirstTrue
Chaser "hit" the Runner!
8
gChaserFirstTrue
Chaser "hit" the Runner!
7
gChaserFirstTrue
gChaserFirstTrue
Chaser "hit" the Runner!
6
gChaserFirstTrue
Chaser "hit" the Runner!
5
gChaserFirstTrue
Chaser "hit" the Runner!
4
gChaserFirstTrue
Chaser "hit" the Runner!
3
gChaserFirstTrue
Chaser "hit" the Runner!
2
gChaserFirstTrue
Chaser "hit" the Runner!
1
gChaserFirstTrue
Chaser "hit" the Runner!
0
Runner lost!Chaser won in 52 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
Chaser lost!Runner won in 83 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
Runner "hit" the Chaser!
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
gChaserFirstFalse
Runner "hit" the Chaser!
Chaser lost!Runner won in 69 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser lost!Runner won in 81 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
Runner "hit" the Chaser!
True
True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser lost!Runner won in 72 ticks
True
True
True
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser lost!Runner won in 59 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
True
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
debug:position setted for chaser
gChaserFirst is currently False
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
Runner "hit" the Chaser!
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
Runner "hit" the Chaser!
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
Runner "hit" the Chaser!
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
Runner "hit" the Chaser!
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
Runner "hit" the Chaser!
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
Runner "hit" the Chaser!
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
Runner "hit" the Chaser!
debug: down-arrow key pressed
True
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug: down-arrow key pressed
True
debug:position setted for chaser
gChaserFirst is currently True
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
debug:position setted for chaser
gChaserFirst is currently False
debug: position setted for runner 
gChaserFirst is currently False
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
debug: down-arrow key pressed
debug: down-arrow key pressed
debug: down-arrow key pressed
debug: down-arrow key pressed
debug: down-arrow key pressed
debug: down-arrow key pressed
debug: down-arrow key pressed
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Chaser lost!Runner won in 200 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser lost!Runner won in 70 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently True
Chaser "hit" the Runner!
gChaserFirst is currently True
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
Chaser "hit" the Runner!
gChaserFirst is currently True
Chaser "hit" the Runner!
gChaserFirst is currently True
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
Chaser "hit" the Runner!
gChaserFirst is currently True
Chaser "hit" the Runner!
gChaserFirst is currently True
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
Chaser "hit" the Runner!
Runner lost!Chaser won in 161 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser lost!Runner won in 125 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser lost!Runner won in 98 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser lost!Runner won in 85 ticks
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser lost!Runner won in 80 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
The player's health is at 0 or below
gChaserFirst is currently False
Runner lost!Chaser won in 107 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser lost!Runner won in 108 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
Chaser lost!Runner won in 55 ticks
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Chaser lost!Runner won in 245 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Chaser "hit" the Runner!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Chaser "hit" the Runner!
Runner "hit" the Chaser!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
Runner "hit" the Chaser!
The player's health is at 0 or below
Chaser lost!Runner won in 215 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
Runner "hit" the Chaser!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Chaser "hit" the Runner!
Runner "hit" the Chaser!
The player's health is at 0 or below
Chaser lost!Runner won in 347 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
Runner "hit" the Chaser!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
Runner "hit" the Chaser!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
Chaser "hit" the Runner!
The player's health is at 0 or below
Runner lost!Chaser won in 160 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Runner "hit" the Chaser!
Chaser lost!Runner won in 198 ticks
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently True
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
Runner "hit" the Chaser!
gChaserFirst is currently True
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
Runner "hit" the Chaser!
gChaserFirst is currently True
Runner "hit" the Chaser!
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently True
gChaserFirst is currently True
Runner "hit" the Chaser!
Chaser lost!Runner won in 106 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/part13-game.py 
gChaserFirstFalse
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
The player's health is at 0 or below
gChaserFirst is currently False
Runner lost!Chaser won in 93 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/high_scores2.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/high_scores2.py", line 18, in <module>
    choice = input("Choice: ")
KeyboardInterrupt
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0

Good-bye.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0

Good-bye.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 4

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0

Good-bye.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 3

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0

Good-bye.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 7
Sorry, but 7 isn't a valid choice.
list of high scores []

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 6
Sorry, but 6 isn't a valid choice.
list of high scores []

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 4
Sorry, but 4 isn't a valid choice.
list of high scores []

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: Jane
What score did the player get?: 100

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Jane 	 100
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: j
What score did the player get?: s
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 42, in <module>
    score = int(input("What score did the player get?: "))
ValueError: invalid literal for int() with base 10: 's'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: -
Sorry, but - isn't a valid choice.
list of high scores []

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 28, in <module>
    score = open('scores.txt', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'scores.txt'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 34, in <module>
    score = open('scores.txt', 'w+r')
ValueError: must have exactly one of create/read/write/append mode
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 27, in <module>
    choice = input("Choice: ")
KeyboardInterrupt
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 51, in <module>
    score.write(entry)
AttributeError: 'int' object has no attribute 'write'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 22
Sorry, but 22 isn't a valid choice.
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 59, in <module>
    print("list of high scores", scores)
NameError: name 'scores' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 51, in <module>
    file.write(entry[1]+ ':'+ entry[0])
TypeError: can only concatenate str (not "int") to str
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
['jane']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 20
['jane:10']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jull
What score did the player get?: 21
['jane:10jack:20']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 38, in <module>
    for entry in scores:
NameError: name 'scores' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['jane:20\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 38, in <module>
    print(file.readlines().strip('\n'))
AttributeError: 'list' object has no attribute 'strip'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
jane:20

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 14
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
jane	14

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
['jane\t14\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 4
['jane\t14\n', 'jack\t10\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: phil
What score did the player get?: 3
['jill\t4\n', 'jane\t14\n', 'jack\t10\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
['jill\t4\n', 'jane\t14\n', 'jack\t10\n']
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: yoon
What score did the player get?: 10
['yoon\t10\n', 'phil\t3\n', 'jill\t4\n', 'jack\t10\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
['phil\t3\n', 'jill\t4\n', 'jane\t10\n', 'jack\t10\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
jane	10
jack	10
jill	4
phil	3

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
jane	10
jack	10
jill	4
phil	3

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
no file

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
High Scores

NAME	SCORE
What is the player's name?: jane
What score did the player get?: 10
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
[]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
jane	10

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 3
High Scores

NAME	SCORE
['jane\t10\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: haily
What score did the player get?: 10
High Scores

NAME	SCORE
['jane\t10\n', 'jack\t3\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
jane	10
jack	3
haily	10

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: james
What score did the player get?: 1
High Scores

NAME	SCORE
['jane\t10\n', 'jack\t3\n', 'haily\t10\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
jane	10
jack	3
haily	10
james	1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 9
Sorry, but 9 isn't a valid choice.
list of high scores ['jane\t10\n', 'jack\t3\n', 'haily\t10\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: yoon
What score did the player get?: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: phil
Sorry, but phil isn't a valid choice.
list of high scores ['jane\t10\n', 'james\t1\n', 'jack\t3\n', 'haily\t10\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: phil
What score did the player get?: 4
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
jane	10
jack	3
haily	10
james	1
yoon	1
phil	4

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> socres
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    socres
NameError: name 'socres' is not defined
>>> scores
['yoon\t1\n', 'jane\t10\n', 'james\t1\n', 'jack\t3\n', 'haily\t10\n']
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 10
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 64, in <module>
    file.write(entry[0]+ '\t'+ str(entry[1])+'\n')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
Sorry, but  isn't a valid choice.
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 78, in <module>
    print("list of high scores", scores)
NameError: name 'scores' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
jane	10
jack	3
haily	10
james	1
yoon	1
phil	4

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 4
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
['yoon\t1\n', 'phil\t4\n', 'jane\t10\n', 'james\t1\n', 'jack\t3\n']
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: phil
What score did the player get?: 15
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: yoon
Sorry, but yoon isn't a valid choice.
list of high scores ['20\tjane\n', '10\tjack\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: yoon
What score did the player get?: 4
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: jina
Sorry, but jina isn't a valid choice.
list of high scores ['20\tjane\n', '15\tphil\n', '10\tjack\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jina
What score did the player get?: 25
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

s
>>> scores
['4\tyoon\n', '20\tjane\n', '15\tphil\n', '10\tjack\n']
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
2
What is the player's name?: 0
What score did the player get?: 0
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 11, in <module>
    file = open('scores.txt', 'r+')
FileNotFoundError: [Errno 2] No such file or directory: 'scores.txt'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
1

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 46, in <module>
    print('entry is'+ entry)
TypeError: can only concatenate str (not "tuple") to str
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
(10, 'jane')
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0'
Sorry, but 0' isn't a valid choice.
list of high scores []

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 48, in <module>
    print(entry.sort())
AttributeError: 'tuple' object has no attribute 'sort'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
None
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 20
None
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(20, 'jane'), (10, 'jack')]
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[(10, 'jane')]
None
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: jack
Sorry, but jack isn't a valid choice.
list of high scores []

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 14
[(10, 'jane'), (14, 'jack')]
None
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 26
[(10, 'jane'), (14, 'jack'), (26, 'jill')]
None
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: phil
What score did the player get?: 1
[(10, 'jane'), (14, 'jack'), (26, 'jill'), (1, 'phil')]
None
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 15
[(15, 'jane')]
[(15, 'jane')]
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 20
[(15, 'jane'), (20, 'jack')]
[(15, 'jane'), (20, 'jack')]
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: haily
What score did the player get?: 1
[(15, 'jane'), (20, 'jack'), (1, 'haily')]
[(1, 'haily'), (15, 'jane'), (20, 'jack')]
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: han
What score did the player get?: 4
[(1, 'haily'), (15, 'jane'), (20, 'jack'), (4, 'han')]
[(1, 'haily'), (4, 'han'), (15, 'jane'), (20, 'jack')]
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 57, in <module>
    file.write(scores)
TypeError: write() argument must be str, not list
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[(10, 'jane')]
[(10, 'jane')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 1
[(10, 'jane'), (1, 'jack')]
[(10, 'jane'), (1, 'jack')]
High Scores

NAME	SCORE
["[(10, 'jane')]"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: haily
What score did the player get?: 35
[(10, 'jane'), (1, 'jack'), (35, 'haily')]
[(35, 'haily'), (10, 'jane'), (1, 'jack')]
High Scores

NAME	SCORE
["[(10, 'jane')][(10, 'jane'), (1, 'jack')]"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['10\tjane']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 20
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['20\tjack']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 59, in <module>
    file.write(str(entry[0]),entry[1])
TypeError: write() takes exactly one argument (2 given)
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['10janek']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['10janek']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['10\tjane\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 20
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['20\tjack\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 13
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['13\tjane\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 13
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['13\tjane\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: aj
What score did the player get?: 20
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 13
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['13\tjane\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
10	jane

10	jane


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
10	jane

10	jane


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 14
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
14	jack

14	jack


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
14	jack


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
20	jane


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
High Scores

NAME	SCORE
['20\tjane\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 24
High Scores

NAME	SCORE
['20\tjane\n', '10\tjane\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
20	jane
10	jane
24	jack


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: haily
What score did the player get?: 14
High Scores

NAME	SCORE
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
14	haily


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
High Scores

NAME	SCORE
['14\thaily\n']
['14\thaily\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
14	haily
10	jane


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 1
High Scores

NAME	SCORE
['14\thaily\n', '10\tjane\n']
['10\tjane\n', '14\thaily\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
14	haily
10	jane
1	jack


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: phil
What score did the player get?: 20
High Scores

NAME	SCORE
['14\thaily\n', '10\tjane\n', '1\tjack\n']
['14\thaily\n', '10\tjane\n', '1\tjack\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
14	haily
10	jane
1	jack
20	phil


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: yoon
What score did the player get?: 5
High Scores

NAME	SCORE
['14\thaily\n', '10\tjane\n', '1\tjack\n', '20\tphil\n']
['20\tphil\n', '14\thaily\n', '10\tjane\n', '1\tjack\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
14	haily
10	jane
1	jack
20	phil
5	yoon


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 38, in <module>
    for line in listversion:
NameError: name 'listversion' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 38, in <module>
    for line in listversion:
NameError: name 'listversion' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jinna
What score did the player get?: 20
High Scores

NAME	SCORE
['14\thaily\n', '10\tjane\n', '1\tjack\n', '20\tphil\n', '5\tyoon\n']
['5\tyoon\n', '20\tphil\n', '14\thaily\n', '10\tjane\n', '1\tjack\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
['5\tyoon\n', '20\tphil\n', '14\thaily\n', '10\tjane\n', '1\tjack\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
['5\tyoon\n', '20\tphil\n', '14\thaily\n', '10\tjane\n', '1\tjack\n']
>>> listversion
['5\tyoon\n', '20\tphil\n', '14\thaily\n', '10\tjane\n', '1\tjack\n']
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jasmin
What score did the player get?: 2
High Scores

NAME	SCORE
['5\tyoon\n', '20\tphil\n', '20\tjinna\n', '14\thaily\n', '10\tjane\n', '1\tjack\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: sue
What score did the player get?: 10
High Scores

NAME	SCORE
['5\tyoon\n', '20\tphil\n', '20\tjinna\n', '2\tjasmin\n', '14\thaily\n', '10\tjane\n', '1\tjack\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 14
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: hans
What score did the player get?: 20
High Scores

NAME	SCORE
["(14, 'jane')\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jasmin
What score did the player get?: 2
High Scores

NAME	SCORE
["(20, 'hans')\n", "(14, 'jane')\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 40, in <module>
    for line in listversion:
NameError: name 'listversion' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jasmin
What score did the player get?: 15
High Scores

NAME	SCORE
["(20, 'jane')\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: hans
What score did the player get?: 3
High Scores

NAME	SCORE
["(20, 'jane')\n", "(15, 'jasmin')\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: mary
What score did the player get?: 30
High Scores

NAME	SCORE
["(3, 'hans')\n", "(20, 'jane')\n", "(15, 'jasmin')\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(3, 'hans')

(20, 'jane')

(15, 'jasmin')

["(3, 'hans')\n", "(20, 'jane')\n", "(15, 'jasmin')\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 56, in <module>
    score = int(input("What score did the player get?: "))
KeyboardInterrupt
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 39, in <module>
    for line in listversion:
NameError: name 'listversion' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: haily
What score did the player get?: 24
High Scores

NAME	SCORE
["(30, 'mary')\n", "(3, 'hans')\n", "(20, 'jane')\n", "(15, 'jasmin')\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(30, 'mary')

(3, 'hans')

(20, 'jane')

(15, 'jasmin')


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(30, 'mary')

(3, 'hans')

(20, 'jane')

(15, 'jasmin')


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[(10, 'jane')]
[(10, 'jane')]
High Scores

NAME	SCORE
["(30, 'mary')\n", "(3, 'hans')\n", "(24, 'haily')\n", "(20, 'jane')\n", "(15, 'jasmin')\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 1
[(10, 'jane'), (1, 'jack')]
[(10, 'jane'), (1, 'jack')]
High Scores

NAME	SCORE
["(30, 'mary')\n", "(3, 'hans')\n", "(24, 'haily')\n", "(20, 'jane')\n", "(15, 'jasmin')\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 20
[(10, 'jane'), (1, 'jack'), (20, 'jill')]
[(20, 'jill'), (10, 'jane'), (1, 'jack')]
High Scores

NAME	SCORE
["(30, 'mary')\n", "(3, 'hans')\n", "(24, 'haily')\n", "(20, 'jane')\n", "(15, 'jasmin')\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(30, 'mary')

(3, 'hans')

(24, 'haily')

(20, 'jane')

(15, 'jasmin')


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 39, in <module>
    for line in listversion:
NameError: name 'listversion' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]
High Scores

NAME	SCORE
["[(20, 'jane')]\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 20
[(20, 'jill')]
[(20, 'jill')]
High Scores

NAME	SCORE
["[(20, 'jane')]\n", "[(20, 'jane'), (10, 'jack')]\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: jack
Sorry, but jack isn't a valid choice.
list of high scores [(20, 'jane')]
1
    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 14
[(20, 'jane'), (14, 'jack')]
[(20, 'jane'), (14, 'jack')]
High Scores

NAME	SCORE
["[(20, 'jane')]"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
[(20, 'jane'), (14, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 30
[(20, 'jane'), (14, 'jack'), (30, 'jill')]
[(30, 'jill'), (20, 'jane'), (14, 'jack')]
High Scores

NAME	SCORE
["[(20, 'jane')][(20, 'jane'), (14, 'jack')]"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE
0
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 14
[(20, 'jane'), (14, 'jack')]
[(20, 'jane'), (14, 'jack')]
High Scores

NAME	SCORE
0
["[(20, 'jane')]\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: haily
What score did the player get?: 14
[(14, 'haily')]
[(14, 'haily')]
High Scores

NAME	SCORE
0
16
["(20, 'jane'), (14, 'jack')]\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(14, 'haily'), (20, 'jane')]
[(20, 'jane'), (14, 'haily')]
High Scores

NAME	SCORE
0
30
["(14, 'jack')]\n"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 14
[(20, 'jane'), (14, 'haily'), (14, 'jack')]
[(20, 'jane'), (14, 'jack'), (14, 'haily')]
High Scores

NAME	SCORE
0
44
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 25
[(20, 'jane'), (14, 'jack'), (14, 'haily'), (25, 'jill')]
[(25, 'jill'), (20, 'jane'), (14, 'jack'), (14, 'haily')]
High Scores

NAME	SCORE
0
58
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jasmin
What score did the player get?: 10
[(25, 'jill'), (20, 'jane'), (14, 'jack'), (14, 'haily'), (10, 'jasmin')]
[(25, 'jill'), (20, 'jane'), (14, 'jack'), (14, 'haily'), (10, 'jasmin')]
High Scores

NAME	SCORE
0
74
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: hans
What score did the player get?: 30
[(25, 'jill'), (20, 'jane'), (14, 'jack'), (14, 'haily'), (10, 'jasmin'), (30, 'hans')]
[(30, 'hans'), (25, 'jill'), (20, 'jane'), (14, 'jack'), (14, 'haily'), (10, 'jasmin')]
High Scores

NAME	SCORE
0
72
[']\n']

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
[(30, 'hans'), (25, 'jill'), (20, 'jane'), (14, 'jack'), (14, 'haily')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> listversion
[']\n']
>>> file.readlines()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    file.readlines()
ValueError: I/O operation on closed file.
>>> a= open('scores.txt','r')
>>> a.readlines()
["[(30, 'hans'), (25, 'jill'), (20, 'jane'), (14, 'jack'), (14, 'haily')]\n", ']\n']
>>> a.read()
''
>>> b=a.read()
>>> b
''
>>> a.readline()
''
>>> a
<_io.TextIOWrapper name='scores.txt' mode='r' encoding='UTF-8'>
>>> a.readlines()
[]
>>> a= open('scores.txt','r')
>>> lines = a.readlines()
>>> lines
["[(30, 'hans'), (25, 'jill'), (20, 'jane'), (14, 'jack'), (14, 'haily')]\n", ']\n']
>>> lines[0]
"[(30, 'hans'), (25, 'jill'), (20, 'jane'), (14, 'jack'), (14, 'haily')]\n"
>>> lines[0][0]
'['
>>> lines[0][1]
'('
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 40, in <module>
    for lines in scores:
NameError: name 'scores' is not defined
>>> score
["[(30, 'hans'), (25, 'jill'), (20, 'jane'), (14, 'jack'), (14, 'haily')]\n", ']\n']
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 15
[(20, 'jane'), (15, 'jack')]
[(20, 'jane'), (15, 'jack')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 30
[(20, 'jane'), (15, 'jack'), (30, 'jill')]
[(30, 'jill'), (20, 'jane'), (15, 'jack')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jasmin
What score did the player get?: 42
[(30, 'jill'), (20, 'jane'), (15, 'jack'), (42, 'jasmin')]
[(42, 'jasmin'), (30, 'jill'), (20, 'jane'), (15, 'jack')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jinna
What score did the player get?: 20
[(42, 'jasmin'), (30, 'jill'), (20, 'jane'), (15, 'jack'), (20, 'jinna')]
[(42, 'jasmin'), (30, 'jill'), (20, 'jinna'), (20, 'jane'), (15, 'jack')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: yoon
What score did the player get?: 10
[(42, 'jasmin'), (30, 'jill'), (20, 'jinna'), (20, 'jane'), (15, 'jack'), (10, 'yoon')]
[(42, 'jasmin'), (30, 'jill'), (20, 'jinna'), (20, 'jane'), (15, 'jack'), (10, 'yoon')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(42, 'jasmin')
(30, 'jill')
(20, 'jinna')
(20, 'jane')
(15, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> score
["[(20, 'jane')][(20, 'jane'), (15, 'jack')][(30, 'jill'), (20, 'jane'), (15, 'jack')][(42, 'jasmin'), (30, 'jill'), (20, 'jane'), (15, 'jack')][(42, 'jasmin'), (30, 'jill'), (20, 'jinna'), (20, 'jane'), (15, 'jack')][(42, 'jasmin'), (30, 'jill'), (20, 'jinna'), (20, 'jane'), (15, 'jack')]"]
>>> listversion
[]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jasmin30
What score did the player get?: 30
[(20, 'jane'), (30, 'jasmin30')]
[(30, 'jasmin30'), (20, 'jane')]
High Scores

NAME	SCORE
["[(20, 'jane')]"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 15
[(20, 'jane'), (15, 'jack')]
[(20, 'jane'), (15, 'jack')]
High Scores

NAME	SCORE
["[(20, 'jane')]"]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 63, in <module>
    del newlist[:]
NameError: name 'newlist' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 64, in <module>
    print(file.write(highscores))
TypeError: write() argument must be str, not list
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 65, in <module>
    file.write(lines+'\n')
TypeError: can only concatenate tuple (not "str") to tuple
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(20, 'jane')

(10, 'jack')


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1\
Sorry, but 1\ isn't a valid choice.
list of high scores []

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(20, 'jane')

(10, 'jack')


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jenny
What score did the player get?: 40
[(40, 'jenny')]
[(40, 'jenny')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(40, 'jenny')

10, 'jack')


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[(40, 'jenny'), (10, 'jane')]
[(40, 'jenny'), (10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(40, 'jenny')

(10, 'jane')


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 13
[(40, 'jenny'), (10, 'jane'), (13, 'jack')]
[(40, 'jenny'), (13, 'jack'), (10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(40, 'jenny')

(13, 'jack')

(10, 'jane')


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 41, in <module>
    for lines in highscores:
NameError: name 'highscores' is not defined
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 40
["(20, 'jane')\n", (40, 'jack')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 54, in <module>
    scores.sort(reverse = True)
TypeError: '<' not supported between instances of 'str' and 'tuple'
>>> scores
["(20, 'jane')\n", (40, 'jack')]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 30
[(30, 'jane')]
[(30, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
["(30, 'jane')", (10, 'jack')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 54, in <module>
    scores.sort(reverse = True)
TypeError: '<' not supported between instances of 'str' and 'tuple'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 65, in <module>
    file.write((lines))
TypeError: write() argument must be str, not tuple
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
["(20, 'jane')", (10, 'jack')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 55, in <module>
    scores.sort(reverse = True)
TypeError: '<' not supported between instances of 'str' and 'tuple'
>>> scores[0]
"(20, 'jane')"
>>> type(scores[0])
<class 'str'>
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
["(20, 'jane')", (10, 'jack')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 57, in <module>
    scores.sort(reverse = True)
TypeError: '<' not supported between instances of 'str' and 'tuple'
>>> scores
["(20, 'jane')", (10, 'jack')]
>>> scores[0]
"(20, 'jane')"
>>> type(scores[0])
<class 'str'>
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
('(', '2', '0', ',', ' ', "'", 'j', 'a', 'n', 'e', "'", ')')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>>  type(scores[0])
SyntaxError: unexpected indent
>>> type(scores[0])
<class 'str'>
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(10, 'jack')]
[(10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
[]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
[]
["(20, 'jane')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
[]
["(20, 'jane')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 11
[(11, 'jack')]
[(11, 'jack')]
[]
["(11, 'jack')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
[]
["(20, 'jane')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
[]
["(20, 'jane')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]
[]

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
["(20, 'jane')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
[]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]

>>> scores
[(20, 'jane')]
>>> scores[0]
(20, 'jane')
>>> scores[0][0]
20
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
["(20, 'jane')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[(10, 'jane')]
[(10, 'jane')]

>>> scores
[(10, 'jane')]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
["(10, 'jane')"]
(10, 'jane')
(

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
["(20, 'jane')"]
(20, 'jane')
(

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
    
[]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]

>>> scores
    
[(20, 'jane')]
>>> scores[0]
    
(20, 'jane')
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
["(20, 'jane')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
    
["(20, 'jane')"]
>>> scores[0]
    
"(20, 'jane')"
>>> scores[0][0]
    
'('
>>> a = tuple(scores[0]
	      )
    
>>> a
    
('(', '2', '0', ',', ' ', "'", 'j', 'a', 'n', 'e', "'", ')')
>>> a = eval(scores[0])
    
>>> a
    
(20, 'jane')
>>> a = eval(scores[0])[0]
    
>>> a
    
20
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
["(20, 'jane')"]
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane')]

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
["(20, 'jane')"]
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 30
[(30, 'jack')]
[(30, 'jack')]
["(30, 'jack')"]
(30, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
["(20, 'jane')"]
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[]
[(10, 'jack')]
[(10, 'jack')]
["(10, 'jack')"]
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[]
[(10, 'jack')]
[(10, 'jack')]
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[]
[(10, 'jane')]
[(10, 'jane')]
(10, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[]
[(10, 'jane')]
[(10, 'jane')]
(10, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')](20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[]
[(10, 'jack')]
[(10, 'jack')]
[(10, 'jack')](10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
==== RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/d.py ====
>>> 
==== RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/d.py ====
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jnae
What score did the player get?: 20
[]
[(20, 'jnae')]
[(20, 'jnae')]

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
(20, 'jnae')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

s
>>> scores
    
[]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 75, in <module>
    file.write((str(lines)))
io.UnsupportedOperation: not writable
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[]
[(10, 'jack')]
[(10, 'jack')]

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
["(20, 'jane')"]
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[]
[(10, 'jane')]
[(10, 'jane')]

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: tr
What score did the player get?: 20
[]
[(20, 'tr')]
[(20, 'tr')]

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 55, in <module>
    for lines in scores:
NameError: name 'scores' is not defined
>>> 
=== RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/new.py ===
try
num0
>>> 
=== RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/new.py ===
try
numhi
except
something went wrong
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
["(20, 'jane')"]
>>> eval(scores)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    eval(scores)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> scores[0]
"(20, 'jane')"
>>> eval(scores[0])
(20, 'jane')
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(20, 'jane')
(
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> line
"(20, 'jane')"
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(20, 'jane')
20
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
["(20, 'jane')"]
>>> line
(20, 'jane')
>>> line[0]
20
>>> a=[]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> a= []
>>> a.append(1,2)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a.append(1,2)
TypeError: append() takes exactly one argument (2 given)
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(20, 'jane')
["(20, 'jane')", (20, 'jane')]
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

s
>>> scores
["(20, 'jane')", (20, 'jane')]
>>> line
(20, 'jane')
>>> tup
(20, 'jane')
>>> type(tup)
<class 'tuple'>
>>> a=[]
>>> a.append(tup)
>>> a
[(20, 'jane')]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(20, 'jane')
["(20, 'jane')", (20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> tup
(20, 'jane')
>>> scores
["(20, 'jane')", (20, 'jane')]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> tup
(20, 'jane')
s
>>> scores
["(20, 'jane')", (20, 'jane')]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
["(20, 'jane')", (20, 'jane')]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')", (20, 'jane')]
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
["(20, 'jane')", (20, 'jane')]
["(20, 'jane')", (20, 'jane'), (10, 'jack')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 68, in <module>
    scores.sort(reverse = True)
TypeError: '<' not supported between instances of 'str' and 'tuple'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')", (20, 'jane')]
["(20, 'jane')\n", "(10, 'jack')", (20, 'jane'), (10, 'jack')]
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
(20, 'jane')

["(20, 'jane')\n", "(10, 'jack')", (20, 'jane')]
(10, 'jack')
["(20, 'jane')\n", "(10, 'jack')", (20, 'jane'), (10, 'jack')]
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]
(20, 'jane')

["(20, 'jane')\n", "(10, 'jack')", (20, 'jane')]
(10, 'jack')
["(20, 'jane')\n", "(10, 'jack')", (20, 'jane'), (10, 'jack')]
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]
(20, 'jane')

["(20, 'jane')\n", "(10, 'jack')", (20, 'jane')]
(10, 'jack')
["(20, 'jane')\n", "(10, 'jack')", (20, 'jane'), (10, 'jack')]
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]
(20, 'jane')

(10, 'jack')
["(20, 'jane')\n", "(10, 'jack')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]
(20, 'jane')

(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]
(20, 'jane')

(20, 'jane')
(10, 'jack')
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]
(20, 'jane')

(20, 'jane')
(20, 'jane')
(10, 'jack')
(10, 'jack')
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]
(20, 'jane')

(20, 'jane')
<class 'tuple'>
(10, 'jack')
(10, 'jack')
<class 'tuple'>

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]
(20, 'jane')

(20, 'jane')
<class 'tuple'>
["(20, 'jane')\n", "(10, 'jack')", (20, 'jane')]
(10, 'jack')
(10, 'jack')
<class 'tuple'>
["(20, 'jane')\n", "(10, 'jack')", (20, 'jane'), (10, 'jack')]
(20, 'jane')
except

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
[]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> score
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    score
NameError: name 'score' is not defined
>>> scores
[]
>>> newscores
["(20, 'jane')\n", "(10, 'jack')"]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]
(20, 'jane')

(20, 'jane')
<class 'tuple'>
[(20, 'jane')]
(10, 'jack')
(10, 'jack')
<class 'tuple'>
[(20, 'jane'), (10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
[(20, 'jane'), (10, 'jack')]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(20, 'jane')\n", "(10, 'jack')"]
(20, 'jane')

(20, 'jane')
<class 'tuple'>
[(20, 'jane')]
(10, 'jack')
(10, 'jack')
<class 'tuple'>
[(20, 'jane'), (10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 22
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack'), (22, 'jill')]
[(22, 'jill'), (20, 'jane'), (10, 'jack')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 83, in <module>
    file.write((str(lines)))
ValueError: I/O operation on closed file.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
try
["(22, 'jill')\n", "(10, 'jack')"]
(22, 'jill')

(22, 'jill')
<class 'tuple'>
[(22, 'jill')]
(10, 'jack')
(10, 'jack')
<class 'tuple'>
[(22, 'jill'), (10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(22, 'jill')
(10, 'jack')
try
["(22, 'jill')\n", "(10, 'jack')"]
(22, 'jill')

(22, 'jill')
<class 'tuple'>
[(22, 'jill'), (10, 'jack'), (22, 'jill')]
(10, 'jack')
(10, 'jack')
<class 'tuple'>
[(22, 'jill'), (10, 'jack'), (22, 'jill'), (10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(22, 'jill')
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 12
[(22, 'jill'), (10, 'jack'), (22, 'jill'), (10, 'jack')]
[(22, 'jill'), (10, 'jack'), (22, 'jill'), (10, 'jack'), (12, 'jane')]
[(22, 'jill'), (22, 'jill'), (12, 'jane'), (10, 'jack'), (10, 'jack')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 83, in <module>
    file.write((str(lines)))
ValueError: I/O operation on closed file.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(22, 'jill')
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[(22, 'jill'), (10, 'jack'), (22, 'jill'), (10, 'jack')]
[(22, 'jill'), (10, 'jack'), (22, 'jill'), (10, 'jack'), (10, 'jane')]
[(22, 'jill'), (22, 'jill'), (10, 'jane'), (10, 'jack'), (10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(22, 'jill')
(22, 'jill')
(10, 'jane')
(10, 'jack')
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(22, 'jill')
(22, 'jill')
(10, 'jane')
(10, 'jack')
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(20, 'jane')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(20, 'jane')
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(20, 'jane'), (20, 'jane')]
[(20, 'jane'), (20, 'jane'), (10, 'jack')]
[(20, 'jane'), (20, 'jane'), (10, 'jack')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 83, in <module>
    file.write((str(lines)))
ValueError: I/O operation on closed file.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 22
[(20, 'jane')]
[(20, 'jane'), (22, 'jack')]
[(22, 'jack'), (20, 'jane')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 83, in <module>
    file.write((str(lines)))
ValueError: I/O operation on closed file.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(22, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[(22, 'jack')]
[(22, 'jack'), (10, 'jane')]
[(22, 'jack'), (10, 'jane')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 83, in <module>
    file.write((str(lines)))
ValueError: I/O operation on closed file.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(22, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[(22, 'jack')]
[(22, 'jack'), (10, 'jane')]
[(22, 'jack'), (10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(22, 'jack')
(10, 'jane')
[(22, 'jack'), (10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(22, 'jack')
(10, 'jane')
[(22, 'jack'), (10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
Sorry, but  isn't a valid choice.
list of high scores [(22, 'jack'), (10, 'jane')]
[(22, 'jack'), (10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[(22, 'jack'), (10, 'jane')]
[(22, 'jack'), (10, 'jane'), (10, 'jane')]
[(22, 'jack'), (10, 'jane'), (10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
[(22, 'jack'), (10, 'jane'), (10, 'jane')]
>>> scores[0]
(22, 'jack')
>>> newfile = open('new.txt', 'r+')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    newfile = open('new.txt', 'r+')
FileNotFoundError: [Errno 2] No such file or directory: 'new.txt'
>>> newfile = open('new.txt', 'w')
>>> newfile.write(scores[0])
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    newfile.write(scores[0])
TypeError: write() argument must be str, not tuple
>>> newfile.write(str(scores[0]))
12
>>> newfile.close()
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane'), (20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
Sorry, but  isn't a valid choice.
list of high scores [(20, 'jane'), (20, 'jane')]
[(20, 'jane'), (20, 'jane'), (20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 32
[(20, 'jane'), (20, 'jane'), (20, 'jane')]
[(20, 'jane'), (20, 'jane'), (20, 'jane'), (32, 'jack')]
[(32, 'jack'), (20, 'jane'), (20, 'jane'), (20, 'jane')]
[(32, 'jack'), (20, 'jane'), (20, 'jane'), (20, 'jane'), (20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
[(32, 'jack'), (20, 'jane'), (20, 'jane'), (20, 'jane'), (20, 'jane')]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane'), (20, 'jane')]
[(20, 'jane'), (20, 'jane')]
[(20, 'jane'), (20, 'jane'), (20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[]
[(10, 'jane')]
[(10, 'jane')]
[(10, 'jane'), (10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(10, 'jane')
(10, 'jane')
[(10, 'jane'), (10, 'jane'), (10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[(10, 'jane')]
[(10, 'jane')]
[(10, 'jane')]
[(10, 'jane'), (10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py l

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[]
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[]
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

s
>>> scores
[]
>>> entry
(20, 'jane')
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: same
What score did the player get?: 20
[]
[]
[]
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> entry
(20, 'same')
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(20, 'jane')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> scores
[(20, 'jane'), (10, 'jack')]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 0
[]
[(0, 'jane')]
[(0, 'jane')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 91, in <module>
    print(file.readlines())
io.UnsupportedOperation: not readable
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> newscores
["(20, 'jane')"]
>>> scores
[(20, 'jane')]
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(20, 'jane')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack'), (10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(10, 'jack')]
[(10, 'jack'), (20, 'jane')]
[(20, 'jane'), (10, 'jack')]
[(10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 10
[]
[(10, 'jane')]
[(10, 'jane')]
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 11
[(10, 'jane')]
[(10, 'jane'), (11, 'jack')]
[(11, 'jack'), (10, 'jane')]
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> line
(10, 'jane')
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 13
[(10, 'jane')]
[(10, 'jane'), (13, 'jack')]
[(13, 'jack'), (10, 'jane')]
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 20
[(10, 'jane')]
[(10, 'jane'), (20, 'jack')]
[(20, 'jack'), (10, 'jane')]
[(20, 'jack'), (10, 'jane')]
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 22
[(10, 'jane')]
[(10, 'jane'), (22, 'jack')]
[(22, 'jack'), (10, 'jane')]
[(22, 'jack'), (10, 'jane')]
(22, 'jack')
(10, 'jane')
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 22
[(10, 'jane')]
[(10, 'jane'), (22, 'jack')]
[(22, 'jack'), (10, 'jane')]
[(22, 'jack'), (10, 'jane')]
(22, 'jack')
(10, 'jane')
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(10, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 22
[(10, 'jane')]
[(10, 'jane'), (22, 'jack')]
[(22, 'jack'), (10, 'jane')]
[(22, 'jack'), (10, 'jane')]
(22, 'jack')
(10, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 22
[]
[(22, 'jack')]
[(22, 'jack')]
[(22, 'jack')]
(22, 'jack')
[(22, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 20
[(22, 'jack')]
[(22, 'jack'), (20, 'jill')]
[(22, 'jack'), (20, 'jill')]
[(22, 'jack'), (20, 'jill')]
(22, 'jack')
(20, 'jill')
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 92, in <module>
    file.write((str(lines)))
ValueError: I/O operation on closed file.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(22, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(22, 'jack')]
[(22, 'jack'), (20, 'jane')]
[(22, 'jack'), (20, 'jane')]
[(22, 'jack'), (20, 'jane')]
(22, 'jack')
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(20, 'jane')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]
(20, 'jane')
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 29
[]
[(29, 'jane')]
[(29, 'jane')]
[(29, 'jane')]
(29, 'jane')
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: chase
What score did the player get?: 20
[]
[(20, 'chase')]
[(20, 'chase')]
[(20, 'chase')]
(20, 'chase')
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(20, 'jane')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]
(20, 'jane')
(10, 'jack')
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 91, in <module>
    file.write((str(lines)))
ValueError: I/O operation on closed file.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 20
[(20, 'jane')]
[(20, 'jane'), (20, 'jack')]
[(20, 'jane'), (20, 'jack')]
[(20, 'jane'), (20, 'jack')]
(20, 'jane')
(20, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 20
[]
[(20, 'jack')]
[(20, 'jack')]
[(20, 'jack')]
(20, 'jack')
[(20, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 22
[(20, 'jack')]
[(20, 'jack'), (22, 'jane')]
[(22, 'jane'), (20, 'jack')]
[(22, 'jane'), (20, 'jack')]
(22, 'jane')
(20, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(20, 'jane')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]
[(20, 'jane'), (10, 'jack')]
(20, 'jane')
(10, 'jack')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: jack
Sorry, but jack isn't a valid choice.
list of high scores [(20, 'jane')]
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 40
[(20, 'jane')]
[(20, 'jane'), (40, 'jack')]
[(40, 'jack'), (20, 'jane')]
[(40, 'jack'), (20, 'jane')]
(40, 'jack')
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
writing
[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 11
[(20, 'jane')]
[(20, 'jane'), (11, 'jack')]
[(20, 'jane'), (11, 'jack')]
[(20, 'jane'), (11, 'jack')]
(20, 'jane')
writing
(11, 'jack')
writing

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
writing
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 94, in <module>
    print('file is currently'+ file.read())
io.UnsupportedOperation: not readable
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
writing
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 94, in <module>
    print('file is currently'+ file.read())
io.UnsupportedOperation: not readable
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
writing
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 94, in <module>
    print('file is currently'+ str(file.read()))
io.UnsupportedOperation: not readable
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
writing
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 94, in <module>
    read = file.read()
io.UnsupportedOperation: not readable
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
writing

[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 22
[(20, 'jane')]
[(20, 'jane'), (22, 'jack')]
[(22, 'jack'), (20, 'jane')]
[(22, 'jack'), (20, 'jane')]
(22, 'jack')
writing

(20, 'jane')
writing


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 23
[]
[(23, 'jane')]
[(23, 'jane')]
[(23, 'jane')]
(23, 'jane')
writing

[(23, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 10
[(23, 'jane')]
[(23, 'jane'), (10, 'jack')]
[(23, 'jane'), (10, 'jack')]
[(23, 'jane'), (10, 'jack')]
(23, 'jane')
writing

(10, 'jack')
writing

[(10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 22
[(10, 'jack')]
[(10, 'jack'), (22, 'jane')]
[(22, 'jane'), (10, 'jack')]
[(22, 'jane'), (10, 'jack')]
(22, 'jane')
0
writing
12

(10, 'jack')
0
writing
12

[(10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(10, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 22
[(10, 'jack')]
[(10, 'jack'), (22, 'jane')]
[(22, 'jane'), (10, 'jack')]
[(22, 'jane'), (10, 'jack')]
(22, 'jane')
0
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 93, in <module>
    file.write((str(lines +'\n')))
TypeError: can only concatenate tuple (not "str") to tuple
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
0
writing
13

[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 12
[(20, 'jane')]
[(20, 'jane'), (12, 'jack')]
[(20, 'jane'), (12, 'jack')]
[(20, 'jane'), (12, 'jack')]
(20, 'jane')
0
writing
13

(12, 'jack')
0
writing
13

[(12, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(12, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(12, 'jack')]
[(12, 'jack'), (20, 'jane')]
[(20, 'jane'), (12, 'jack')]
[(20, 'jane'), (12, 'jack')]
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 91, in <module>
    print(lines.rstrip())
AttributeError: 'tuple' object has no attribute 'rstrip'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 95, in <module>
    file.write(str(i) + ": " + line)
TypeError: can only concatenate str (not "tuple") to str
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 22
[]
[(22, 'jane')]
[(22, 'jane')]
[(22, 'jane')]
(22, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
0
writing
13

[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 2
[(20, 'jane')]
[(20, 'jane'), (2, 'jack')]
[(20, 'jane'), (2, 'jack')]
[(20, 'jane'), (2, 'jack')]
(20, 'jane')
0
writing
13

(2, 'jack')
0
writing
12

[(2, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(2, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[(2, 'jack')]
[(2, 'jack'), (20, 'jane')]
[(20, 'jane'), (2, 'jack')]
[(20, 'jane'), (2, 'jack')]
(20, 'jane')
12
writing
25

(2, 'jack')
25
writing
37

[(2, 'jack'), (20, 'jane'), (2, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 20
[]
[(20, 'jane')]
[(20, 'jane')]
[(20, 'jane')]
(20, 'jane')
0
writing
13

[(20, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 11
[(20, 'jane')]
[(20, 'jane'), (11, 'jack')]
[(20, 'jane'), (11, 'jack')]
[(20, 'jane'), (11, 'jack')]
(20, 'jane')
13
writing
26

(11, 'jack')
26
writing
39

[(20, 'jane'), (20, 'jane'), (11, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(20, 'jane'), (20, 'jane'), (11, 'jack')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: chase
What score did the player get?: 22
[(20, 'jane'), (20, 'jane'), (11, 'jack')]
[(20, 'jane'), (20, 'jane'), (11, 'jack'), (22, 'chase')]
[(22, 'chase'), (20, 'jane'), (20, 'jane'), (11, 'jack')]
[(22, 'chase'), (20, 'jane'), (20, 'jane'), (11, 'jack')]
(22, 'chase')
0
writing
14

(20, 'jane')
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py", line 93, in <module>
    print(file.tell())
ValueError: I/O operation on closed file.
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 
[(22, 'chase')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jane
What score did the player get?: 12
[(22, 'chase')]
[(22, 'chase'), (12, 'jane')]
[(22, 'chase'), (12, 'jane')]
[(22, 'chase'), (12, 'jane')]
(22, 'chase')
0
writing
14

(12, 'jane')
14
writing
27

[(22, 'chase'), (12, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jack
What score did the player get?: 30
[(22, 'chase'), (12, 'jane')]
[(22, 'chase'), (12, 'jane'), (30, 'jack')]
[(30, 'jack'), (22, 'chase'), (12, 'jane')]
[(30, 'jack'), (22, 'chase'), (12, 'jane')]
(30, 'jack')
0
writing
13

(22, 'chase')
13
writing
27

(12, 'jane')
27
writing
40

[(30, 'jack'), (22, 'chase'), (12, 'jane')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jill
What score did the player get?: 5
[(30, 'jack'), (22, 'chase'), (12, 'jane')]
[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill')]
[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill')]
[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill')]
(30, 'jack')
0
writing
13

(22, 'chase')
13
writing
27

(12, 'jane')
27
writing
40

(5, 'jill')
40
writing
52

[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: charlie
Sorry, but charlie isn't a valid choice.
list of high scores [(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill')]
[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: charlie
What score did the player get?: 1
[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill')]
[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill'), (1, 'charlie')]
[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill'), (1, 'charlie')]
[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill'), (1, 'charlie')]
(30, 'jack')
0
writing
13

(22, 'chase')
13
writing
27

(12, 'jane')
27
writing
40

(5, 'jill')
40
writing
52

(1, 'charlie')
52
writing
67

[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill'), (1, 'charlie')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jina
What score did the player get?: 24
[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill'), (1, 'charlie')]
[(30, 'jack'), (22, 'chase'), (12, 'jane'), (5, 'jill'), (1, 'charlie'), (24, 'jina')]
[(30, 'jack'), (24, 'jina'), (22, 'chase'), (12, 'jane'), (5, 'jill'), (1, 'charlie')]
[(30, 'jack'), (24, 'jina'), (22, 'chase'), (12, 'jane'), (5, 'jill')]
(30, 'jack')
0
writing
13

(24, 'jina')
13
writing
26

(22, 'chase')
26
writing
40

(12, 'jane')
40
writing
53

(5, 'jill')
53
writing
65

[(30, 'jack'), (24, 'jina'), (22, 'chase'), (12, 'jane'), (5, 'jill')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(30, 'jack')
(24, 'jina')
(22, 'chase')
(12, 'jane')
(5, 'jill')
[(30, 'jack'), (24, 'jina'), (22, 'chase'), (12, 'jane'), (5, 'jill')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-highscores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(30, 'jack')
(24, 'jina')
(22, 'chase')
(12, 'jane')
(5, 'jill')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 03
Sorry, but 03 isn't a valid choice.
list of high scores [(30, 'jack'), (24, 'jina'), (22, 'chase'), (12, 'jane'), (5, 'jill')]

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: jas
What score did the player get?: 43

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(43, 'jas')
(30, 'jack')
(24, 'jina')
(22, 'chase')
(12, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.


    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
The player's health is at 0 or below
gChaserFirst is currently False
Runner lost!Chaser won in 58 ticks
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
The player's health is at 0 or below
gChaserFirst is currently False
Runner lost!Chaser won in 71 ticks

 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(43, 'jas')
(30, 'jack')
(24, 'jina')
(22, 'chase')
(12, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: 
What score did the player get?: 
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py", line 13, in <module>
    from  pa13Player  import Player
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13Player.py", line 155, in <module>
    score = int(input("What score did the player get?: "))
ValueError: invalid literal for int() with base 10: ''
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(43, 'jas')
(30, 'jack')
(24, 'jina')
(22, 'chase')
(12, 'jane')

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 2
What is the player's name?: 
What score did the player get?: e
Traceback (most recent call last):
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py", line 13, in <module>
    from  pa13Player  import Player
  File "/Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13Player.py", line 155, in <module>
    score = int(input("What score did the player get?: "))
ValueError: invalid literal for int() with base 10: 'e'
>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
The player's health is at 0 or below
gChaserFirst is currently False
Runner lost!Chaser won in 103 ticks

    High Scores 2.0
    
    0 - Quit (Start the Game)
    1 - List Scores
    2 - Add a Score
    
Choice: 2
(103, 'Chaser')

    High Scores 2.0
    
    0 - Quit (Start the Game)
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(12, 'jane')
(22, 'chase')
(24, 'jina')
(30, 'jack')
(43, 'jas')

    High Scores 2.0
    
    0 - Quit (Start the Game)
    1 - List Scores
    2 - Add a Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
The player's health is at 0 or below
gChaserFirst is currently False
gChaserFirst is currently False
Chaser lost!Runner won in 53 ticks

    High Scores 2.0
    
    0 - Quit (Start the Game)
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE

    High Scores 2.0
    
    0 - Quit (Start the Game)
    1 - List Scores
    2 - Add a Score
    
Choice: 2
(53, 'Runner')

    High Scores 2.0
    
    0 - Quit (Start the Game)
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(53, 'Runner')

    High Scores 2.0
    
    0 - Quit (Start the Game)
    1 - List Scores
    2 - Add a Score
    
Choice: 2
(53, 'Runner')

    High Scores 2.0
    
    0 - Quit (Start the Game)
    1 - List Scores
    2 - Add a Score
    
Choice: 1
High Scores

NAME	SCORE
(53, 'Runner')
(53, 'Runner')

    High Scores 2.0
    
    0 - Quit (Start the Game)
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
The player's health is at 0 or below
gChaserFirst is currently False
Runner lost!Chaser won in 68 ticks

    High Scores 2.0
    
    0 - Quit 
    1 - List Scores
    2 - Add the previous Score
    
Choice: 2
(68, 'Chaser')

    High Scores 2.0
    
    0 - Quit 
    1 - List Scores
    2 - Add the previous Score
    
Choice: 1
High Scores

SCORE	NAME
(68, 'Chaser')

    High Scores 2.0
    
    0 - Quit 
    1 - List Scores
    2 - Add the previous Score
    
Choice: 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
The player's health is at 0 or below
gChaserFirst is currently False
gChaserFirst is currently False
Chaser lost!Runner won in 55 ticks

    High Scores 2.0
    
    0 - Quit 
    1 - List Scores
    2 - Add the previous Score
    
Choice: 2
(55, 'Runner')

    High Scores 2.0
    
    0 - Quit 
    1 - List Scores
    2 - Add the previous Score
    
Choice: 1
High Scores

SCORE	NAME
(55, 'Runner')
(68, 'Chaser')

    High Scores 2.0
    
    0 - Quit 
    1 - List Scores
    2 - Add the previous Score
    
Choice: 0
Good-bye.

>>> 
 RESTART: /Users/janechoi/Desktop/IU/INTRO  TO PROGRAMMING/pa13/pa13-game-high-scores.py 

    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
Choice: 0
Good-bye.

gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
gChaserFirst is currently False
Runner "hit" the Chaser!
gChaserFirst is currently False
gChaserFirst is currently False
Chaser "hit" the Runner!
gChaserFirst is currently True
The player's health is at 0 or below
gChaserFirst is currently False
Runner lost!Chaser won in 59 ticks

    High Scores 2.0
    
    0 - Quit 
    1 - List Scores
    2 - Add the previous Score
    
Choice: 2
(59, 'Chaser')

    High Scores 2.0
    
    0 - Quit 
    1 - List Scores
    2 - Add the previous Score
    
Choice: 1
High Scores

SCORE	NAME
(55, 'Runner')
(59, 'Chaser')
(68, 'Chaser')

    High Scores 2.0
    
    0 - Quit 
    1 - List Scores
    2 - Add the previous Score
    
Choice: 0
Good-bye.

>>> 1/0
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> 
