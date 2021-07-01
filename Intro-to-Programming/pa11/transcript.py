Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> my_list = [1,2,3,4,5,6]
>>> truncate(my_list,1)
>>> my_list
[1, 2, 3, 4, 5]
>>> truncate(my_list)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    truncate(my_list)
TypeError: truncate() missing 1 required positional argument: 'num'
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> truncate(my_list)
>>> my_list
[1, 2, 3, 4, 5, 6]
>>> truncate(my_list,2)
>>> my_list
[1, 2, 3, 4]
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> half  = Fraction(1,2)
>>> hals
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    hals
NameError: name 'hals' is not defined
>>> half
Fraction(1, 2)
>>> 
two_sixths = Fraction(2,6)
>>> two_sixths
Fraction(1, 3)
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> Card(12,'dia')
<__main__.Card object at 0x109921470>
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> Card(12,'dia')
Card(12, 'D')
>>> c1 = Card(11,'Spaes')
>>> c1
Card(11, 'S')
>>> c1.suit
'S'
>>> c1.rank
11
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> Card(3,'ca')
Card(3, 'C')
>>> Card('KD')
Card(13, 'D')
>>> Card('3s')
Card(3, 'S')
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> blank = Point(4,2)
>>> blank
<__main__.Point object at 0x10e487ef0>
>>> blank.x
4
>>> blank.y
2
>>> blank.z
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    blank.z
AttributeError: 'Point' object has no attribute 'z'
>>> isinstance(blank, Point)
True
>>> hasattr(blank,'x')
True
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> print_time(start)
09:45:00
>>> start.print_time
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    start.print_time
AttributeError: 'Time' object has no attribute 'print_time'
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> start.print_time
<bound method Time.print_time of <__main__.Time object at 0x108376438>>
>>> start.print_time()
09:45:00
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> time = Time()
>>> time.print_time()
00:00:00
>>> time = Time(9)
>>> time.print_time()
09:00:00
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> time = Time(9,20)
>>> time
<__main__.Time object at 0x10aa156d8>
>>> print(time)
09:20:00
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-a.py ================
>>> bike1 = Bike('Jane',-10)
>>> bike2 = Bike(,10)
SyntaxError: invalid syntax
>>> bike2 = Bike(1)
>>> bike2.status()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    bike2.status()
  File "/Users/janechoi/Documents/pa11-a.py", line 18, in status
    print("The bike's name is.."+ self.name +'\n and the tire pressure is..'+ self.tire_pressure)
TypeError: can only concatenate str (not "int") to str
>>> bike2.name()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    bike2.name()
TypeError: 'int' object is not callable
>>> bike2.tire_pressure()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    bike2.tire_pressure()
TypeError: 'int' object is not callable
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> f1 = Fraction(,1)
SyntaxError: invalid syntax
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-a.py ================
>>> bike1 = Bike('k')
>>> bike1.name()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    bike1.name()
TypeError: 'str' object is not callable
>>> bike.name
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    bike.name
NameError: name 'bike' is not defined
>>> bike1.name
'k'
>>> bike1.tire_pressure
0
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-a.py ================
>>> bike1 = Bike('jane',-10)
>>> bike2 = Bike(20)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    bike2 = Bike(20)
  File "/Users/janechoi/Documents/pa11-a.py", line 25, in __init__
    self.tire_pressure = self.name
AttributeError: 'Bike' object has no attribute 'name'
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-a.py ================
>>> bike1 = Bike('jane', -20)
>>> bike2 = Bike('kay')
>>> bike3 = Bike(20)
>>> bike4= Bike(-20)
>>> bike1.status()
The bike's name is..jane
 and the tire pressure is..0
>>> bike2.status()
The bike's name is..kay
 and the tire pressure is..0
>>> bike3.status()
The bike's name is..Celerifere
 and the tire pressure is..0
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-a.py ================
>>> bike1 = Bike('jane',-100)
>>> bike1.status()
The bike's name is..jane
 and the tire pressure is..0
>>> bike2 = Bike('Jill')
>>> bike2.status()
The bike's name is..Jill
 and the tire pressure is..0
>>> bike3 = Bike('Phil
		 
SyntaxError: EOL while scanning string literal
>>> bike3 = Bike('phil
		 
SyntaxError: EOL while scanning string literal
>>> bike3 = Bike(-20)
		 
>>> bike3.status()
		 
The bike's name is..Celerifere
 and the tire pressure is..0
>>> bike4 = Bike(20)
		 
>>> bike4.status()
		 
The bike's name is..Celerifere
 and the tire pressure is..20
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-b.py ================
>>> player1 = Player('jack',10,['ball','bat'])
		 
>>> player1.name
		 
'jack'
>>> player1.max_items
		 
10
>>> player1.items
		 
['ball', 'bat']
>>> player1.inventory()
		 
['ball', 'bat']
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-b.py ================
>>>  player1 = Player('jack',3,['ball','bat'])
		 
SyntaxError: unexpected indent
>>> player1 = Player('jack',3,['ball','bat'])
		 
>>> player1.take('water')
		 
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    player1.take('water')
  File "/Users/janechoi/Documents/pa11-b.py", line 26, in take
    if pmax <= len(self.items):
NameError: name 'pmax' is not defined
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-b.py ================
>>> player1 = Player('jack',3,['ball','bat'])
		 
>>> player1.take('water')
		 
>>> player1.items
		 
>>> player1.items()
		 
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    player1.items()
TypeError: 'NoneType' object is not callable
>>> player1.items
		 
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-b.py ================
>>> player1 = Player('jack',3,['ball','bat'])
		 
>>> player1.items
		 
['ball', 'bat']
\
>>> player.take('water')
		 
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    player.take('water')
NameError: name 'player' is not defined
>>> player1.take('water')
		 
>>> player.items
		 
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    player.items
NameError: name 'player' is not defined
>>> player1.items
		 
>>> l1 = [1,2,3,4,5]
		 
>>> l1.append(2)
		 
>>> l1
		 
[1, 2, 3, 4, 5, 2]
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-b.py ================
>>> player1 = Player('jack',3,['ball','bat'])
		 
>>> player1.take('water')
		 
>>> player1.items
		 
['ball', 'bat', 'water']
>>> player1.take('cat')
		 
The player item list has been exceeded the maximum number of items the player can carry
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-b.py ================
>>> player1 = Player('jack',3,['ball','bat'])
		 
>>> player1.take('water')
		 
>>> player1.take('s')
		 
The player item list has been exceeded the maximum number of 
 items the player can carry
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-b.py ================
>>> player1 = Player('jack',3,['ball','bat'])
		 
>>> player1.take('water')
		 
>>> player1.drop('dog')
		 
The player does not carry the item
The player does not carry the item
The player does not carry the item
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-b.py ================
>>> player1 = Player('jack',3,['ball','bat'])
		 
>>> player.drop('cat')
		 
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    player.drop('cat')
NameError: name 'player' is not defined
>>> player1.drop('cat')
		 
The player does not carry the item
>>> player1.drop('ball')
		 
>>> player1.items
		 
['bat']
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-b.py ================
>>> player2 = Player('jill',3,['ball','bat', 'water', 'tube'])
		 
>>> player2.items
		 
['ball', 'bat', 'water', 'tube']
>>> player2.take('cat')
		 
The player item list has been exceeded the maximum number of 
 items the player can carry
>>> player2.drop('cat')
		 
The player does not carry the item
>>> player2.drop('water')
		 
>>> player2.items
		 
['ball', 'bat', 'tube']
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-a.py ================
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-a.py ================
>>> m = Bike(1)
		 
>>> m.name
		 
1
>>> m.tire_pressure
		 
1
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-a.py ================
>>> m = Bike('jane')
		 
>>> m.tire_pressure
		 
0
>>> 10/1000
		 
0.01
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m = Bike('jane')
		 
>>> m.status()
		 
The bike's name is..jane
 and the tire pressure is..0
>>> m.ride(10)
		 
The bike does not have enough tire pressure to move
The bike's name is..jane
 and the tire pressure is..0
>>> m = Bike('jane', 1)
		 
>>> m.ride(1)
		 
The bike does not have enough tire pressure to move
The bike's name is..jane
 and the tire pressure is..0
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m = Bike('jane', 1)
		 
>>> m.ride(.1)
		 
The bike can not ride a distance less than 1
The bike's name is..jane
 and the tire pressure is..0
>>> m = Bike('jane',2)
		 
>>> m.status
		 
<bound method Bike.status of <__main__.Bike object at 0x103e83438>>
>>> m.status()
		 
The bike's name is..jane
 and the tire pressure is..0
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m = Bike('jane',2)
		 
>>> m.status()
		 
The bike's name is..jane
 and the tire pressure is..0.0
>>> m = Bike('j')
		 
>>> m.status()
		 
The bike's name is..j
 and the tire pressure is..0.0
>>> m = Bike(2)
		 
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    m = Bike(2)
  File "/Users/janechoi/Documents/pa11-c.py", line 38, in __init__
    if self.tire_pressure < 0.0 :
AttributeError: 'Bike' object has no attribute 'tire_pressure'
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m = Bike(2)
		 
>>> m.status
		 
<bound method Bike.status of <__main__.Bike object at 0x1068a2c50>>
>>> m.status()
		 
The bike's name is..Celerifere
 and the tire pressure is..2
>>> m = Bike('j',2)
		 
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    m = Bike('j',2)
  File "/Users/janechoi/Documents/pa11-c.py", line 29, in __init__
    if self.tire_pressure <0 :
AttributeError: 'Bike' object has no attribute 'tire_pressure'
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m = Bike('j',2)
		 
>>> m.status()
		 
The bike's name is..j
 and the tire pressure is..2
>>> m =Bike('l')
		 
>>> m.status()
		 
The bike's name is..l
 and the tire pressure is..0.0
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m = Bike('j',2)
		 
>>> m.ride(.2)
		 
The bike can not ride a distance less than 1
The bike's name is..j
 and the tire pressure is..2
>>> m.ride(3000)
		 
The bike does not have enough tire pressure to move
The bike's name is..j
 and the tire pressure is..2
>>> m.ride(20)
		 
The tire pressure has reduced to..1.98
The bike's name is..j
 and the tire pressure is..1.98
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m = Bike('a', 100)
		 
>>> m.status()
		 
The bike's name is..a
 and the tire pressure is..100
>>> m.repressurize(10)
		 
The bike tire pressure has been added with the value
The bike tire has been exploded due to too much pressure
The bike's name is..a
 and the tire pressure is..110
>>> m.ride(10)
		 
The bike is not usable, the tire has exploded
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m = Bike(100)
		 
>>> m.repressurize(.1)
		 
The bike can not be repressurized with an amount less than 1 
The bike's name is..Celerifere
 and the tire pressure is..100
>>> m.repressurize(10)
		 
The bike tire pressure has been added with the value
The bike tire has been exploded due to too much pressure
The bike's name is..Celerifere
 and the tire pressure is..110
>>> m.ride(2)
		 
The bike is not usable, the tire has exploded
The bike's name is..Celerifere
 and the tire pressure is..110
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m = Bike(100)
		 
>>>  m.repressurize(10)
		 
SyntaxError: unexpected indent
>>> m.repressurize(10)
		 
The bike tire pressure has been added with the value
The bike tire has been exploded due to too much pressure
The bike tire has been exploded before
The bike's name is..Celerifere
 and the tire pressure is..110
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m = Bike(100)
		 
>>> m.repressurize(10)
		 
The bike tire pressure has been added with the value
But..the bike tire has been exploded due to too much pressure
The bike's name is..Celerifere
 and the tire pressure is..110
>>> m.repressurize(10)
		 
The bike's name is..Celerifere
 and the tire pressure is..110
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m  = Bike(100)
		 
>>> m.repressurize(10)
		 
The bike tire pressure has been added with the value
But..the bike tire has been exploded due to too much pressure
The bike is not usable since the tire has exploded
The bike's name is..Celerifere
 and the tire pressure is..110
>>> m.repressurize(10)
		 
The bike is not usable since the tire has exploded
The bike's name is..Celerifere
 and the tire pressure is..110
>>> m1= Bike(102)
		 
>>> m1.status()
		 
The bike's name is..Celerifere
 and the tire pressure is..102
>>> m1.ride(10)
		 
The tire pressure has reduced to..101.99
The tire pressure has reduced to..101.97999999999999
The tire pressure has reduced to..101.96999999999998
The tire pressure has reduced to..101.95999999999998
The tire pressure has reduced to..101.94999999999997
The tire pressure has reduced to..101.93999999999997
The tire pressure has reduced to..101.92999999999996
The tire pressure has reduced to..101.91999999999996
The tire pressure has reduced to..101.90999999999995
The tire pressure has reduced to..101.89999999999995
The tire pressure has reduced to..101.88999999999994
The tire pressure has reduced to..101.87999999999994
The tire pressure has reduced to..101.86999999999993
The tire pressure has reduced to..101.85999999999993
The tire pressure has reduced to..101.84999999999992
The tire pressure has reduced to..101.83999999999992
The tire pressure has reduced to..101.82999999999991
The tire pressure has reduced to..101.81999999999991
The tire pressure has reduced to..101.8099999999999
The tire pressure has reduced to..101.7999999999999
The tire pressure has reduced to..101.78999999999989
The tire pressure has reduced to..101.77999999999989
The tire pressure has reduced to..101.76999999999988
The tire pressure has reduced to..101.75999999999988
The tire pressure has reduced to..101.74999999999987
The tire pressure has reduced to..101.73999999999987
The tire pressure has reduced to..101.72999999999986
The tire pressure has reduced to..101.71999999999986
The tire pressure has reduced to..101.70999999999985
The tire pressure has reduced to..101.69999999999985
The tire pressure has reduced to..101.68999999999984
The tire pressure has reduced to..101.67999999999984
The tire pressure has reduced to..101.66999999999983
The tire pressure has reduced to..101.65999999999983
The tire pressure has reduced to..101.64999999999982
The tire pressure has reduced to..101.63999999999982
The tire pressure has reduced to..101.62999999999981
The tire pressure has reduced to..101.6199999999998
The tire pressure has reduced to..101.6099999999998
The tire pressure has reduced to..101.5999999999998
The tire pressure has reduced to..101.58999999999979
The tire pressure has reduced to..101.57999999999979
The tire pressure has reduced to..101.56999999999978
The tire pressure has reduced to..101.55999999999977
The tire pressure has reduced to..101.54999999999977
The tire pressure has reduced to..101.53999999999976
The tire pressure has reduced to..101.52999999999976
The tire pressure has reduced to..101.51999999999975
The tire pressure has reduced to..101.50999999999975
The tire pressure has reduced to..101.49999999999974
The tire pressure has reduced to..101.48999999999974
The tire pressure has reduced to..101.47999999999973
The tire pressure has reduced to..101.46999999999973
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    m1.ride(10)
  File "/Users/janechoi/Documents/pa11-c.py", line 73, in ride
    print('The tire pressure has reduced to..' + str(self.tire_pressure))
KeyboardInterrupt
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> m1 = Bike(100)
		 
>>> m1.ride(10)
		 
The tire pressure has reduced to..99.99
The bike's name is..Celerifere
 and the tire pressure is..99.99
>>> m.repressurize(10)
		 
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    m.repressurize(10)
NameError: name 'm' is not defined
>>> m1.repressurize(10)
		 
The bike tire pressure has been added with the value
But..the bike tire has been exploded due to too much pressure
The bike's name is..Celerifere
 and the tire pressure is..109.99
>>> m1.ride(10)
		 
The bike is not usable, the tire has exploded
The bike's name is..Celerifere
 and the tire pressure is..109.99
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
>>> d =Dot(1,2,'blue')
		 
>>> print(d)
		 
Dot(1,2,blue,)
>>> 2**4
		 
16
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
>>> d1 = Dot(1,2,'blue')
		 
>>> d2 = Dot(2,3,'blue')
		 
>>> d1.distance_to(d2)
		 
1.4142135623730951
>>> sqrt((1 - 2)**2 + (2- 3)**2)
		 
1.4142135623730951
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
>>> d1 =Dot(1,2,'blue')
		 
>>> d1.move_up(2)
		 
>>> print(d1)
		 
Dot(1,4,blue)
>>> d1.move_right(1)
		 
>>> print(d1)
		 
Dot(2,4,blue)
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,75)...
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa11-d.py", line 39, in <module>
    print("dot1 is now: " + repr(dot1))
NameError: name 'dot1' is not defined
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,75)...
d1 is now: <__main__.Dot object at 0x10adb3cc0>
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,75)...
d1 is now: Dot(10,75,blue)
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
>>> d1.draw()
		 
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    d1.draw()
  File "/Users/janechoi/Documents/pa11-d.py", line 37, in draw
    Window = turtle.Screen()
UnboundLocalError: local variable 'turtle' referenced before assignment
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
>>> d1.draw()
		 
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
>>> d1.draw()
		 
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa11-d.py", line 84, in <module>
    d1.draw()
  File "/Users/janechoi/Documents/pa11-d.py", line 38, in draw
    Window = turtle.Screen()
UnboundLocalError: local variable 'turtle' referenced before assignment
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: Dot(10,35,blue)
Moving d2 , 15 places to the left 
d2 is now: Dot(15,75,green)
Changing d1 color to red
d1 is now: Dot(10,35,red)
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: The dot x coordinate is 10 , the y coordinate35,
 the color isblue)
Moving d2 , 15 places to the left 
d2 is now: The dot x coordinate is 15 , the y coordinate75,
 the color isgreen)
Changing d1 color to red
d1 is now: The dot x coordinate is 10 , the y coordinate35,
 the color isred)
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: The dot x coordinate is 10 , the y coordinate35,
 the color isblue
Moving d2 , 15 places to the left 
d2 is now: The dot x coordinate is 15 , the y coordinate75,
 the color isgreen
Changing d1 color to red
d1 is now: The dot x coordinate is 10 , the y coordinate35,
 the color isred
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: The dot x coordinate is.. 10 , the y coordinate is..35,
 the color isblue
Moving d2 , 15 places to the left 
d2 is now: The dot x coordinate is.. 15 , the y coordinate is..75,
 the color isgreen
Changing d1 color to red
d1 is now: The dot x coordinate is.. 10 , the y coordinate is..35,
 the color isred
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: The dot x coordinate is.. 10 , the y coordinate is..35,
 the color is..blue
Moving d2 , 15 places to the left 
d2 is now: The dot x coordinate is.. 15 , the y coordinate is..75,
 the color is..green
Changing d1 color to red
d1 is now: The dot x coordinate is.. 10 , the y coordinate is..35,
 the color is..red
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Creating a green Dot called dot1 with coordinates (30,75)...
Moving d1 , 15 places up
d1 is now: 10,35,blue
Moving d2 , 15 places to the left 
d2 is now: 15,75,green
Changing d1 color to red
d1 is now: 10,35,red
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
10,20,blue
Creating a green Dot called dot1 with coordinates (30,75)...
30,75,green
Moving d1 , 15 places up
d1 is now: 10,35,blue
Moving d2 , 15 places to the left 
d2 is now: 15,75,green
Changing d1 color to red
d1 is now: 10,35,red
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa11-d.py", line 82, in <module>
    print('d1 is' +d1)
TypeError: can only concatenate str (not "Dot") to str
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
10,20,blue
Creating a green Dot called dot1 with coordinates (30,75)...
30,75,green
Moving d1 , 15 places up
d1 is now: 10,35,blue
Moving d2 , 15 places to the left 
d2 is now: 15,75,green
Changing d1 color to red
d1 is now: 10,35,red
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> a = print(d1)
10,35,red
>>> type(a)
<class 'NoneType'>
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
10,20,blue
Creating a green Dot called dot1 with coordinates (30,75)...
30,75,green
Moving d1 , 15 places up
d1 is now: 10,35,blue
Moving d2 , 15 places to the left 
d2 is now: 15,75,green
Changing d1 color to red
d1 is now: 10,35,red
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-d.py ================
Creating a blue Dot called dot1 with coordinates (10,20)...
10,20,blue
Creating a green Dot called dot1 with coordinates (30,75)...
30,75,green
Moving d1 , 15 places up
d1 is now: 10,35,blue
Moving d2 , 15 places to the left 
d2 is now: 15,75,green
Changing d1 color to red
d1 is now: 10,35,red
The distance between the two dots d1, d2 is...
40.311288741492746
We will now draw the dots...
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-a.py ================
>>> a =Bike()
>>> a.name
'Celerifere'
>>> a.tire_pressure
0.0
>>> 
================ RESTART: /Users/janechoi/Documents/pa11-c.py ================
>>> 
