Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
<__main__.Robot object at 0x1029785c0> <class '__main__.Robot'>
<__main__.PhysicianRobot object at 0x104409c88> <class '__main__.PhysicianRobot'>
Hi, I am James
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa12-part1.py", line 6, in <module>
    x = Robot("Marvin")
NameError: name 'Robot' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
True True
False
True
False True
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
True
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Everything will be okay! 
James takes care of you!
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Everything will be okay! 
Doc James takes care of you!
... and now the 'traditional' robot way of saying hi :-)
Hi, I am Doc James
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
health_level of Marvin1 before healing:  0.6929274128853803
Marvin1 has been healed by Dr. Frankenstein!
health_level of Marvin1 after healing:  0.8319985709837417
health_level of Marvin2 before healing:  0.2776267193843869
Marvin2 has been healed by Dr. Frankenstein!
health_level of Marvin2 after healing:  0.3312961719306965
health_level of Marvin4 before healing:  0.21310685205707447
Marvin4 has been healed by Dr. Frankenstein!
health_level of Marvin4 after healing:  0.8823422391885278
[('Marvin0', 0.8186208627647892), ('Marvin1', 0.8319985709837417), ('Marvin2', 0.3312961719306965), ('Marvin3', 0.9617921454890658), ('Marvin4', 0.8823422391885278)]
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa12-part1.py", line 7, in <module>
    class PhysicianRobot(Robot):
NameError: name 'Robot' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Hi, I am Dr. Frankenstein
and I am a physician!
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> queen_of_diamonds = Card(1, 12)
>>> queen_of_diamonds
<__main__.Card object at 0x103929cf8>
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> print(queen_of_diamonds)
Queen of Diamonds
>>> card1 = Card(2,10)
>>> print(card1)
10 of Hearts
>>> card1
<__main__.Card object at 0x10c439dd8>
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> card1= Card(2)
>>> print(card1)
2 of Hearts
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> card2 =(2,12)
>>> card2 = Card(2,12)
>>> card2.lt(card1)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    card2.lt(card1)
AttributeError: 'Card' object has no attribute 'lt'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> deck1 = Deck()
>>> print(deck1)
Ace of Clubs
2 of Clubs
3 of Clubs
4 of Clubs
5 of Clubs
6 of Clubs
7 of Clubs
8 of Clubs
9 of Clubs
10 of Clubs
Jack of Clubs
Queen of Clubs
King of Clubs
Ace of Diamonds
2 of Diamonds
3 of Diamonds
4 of Diamonds
5 of Diamonds
6 of Diamonds
7 of Diamonds
8 of Diamonds
9 of Diamonds
10 of Diamonds
Jack of Diamonds
Queen of Diamonds
King of Diamonds
Ace of Hearts
2 of Hearts
3 of Hearts
4 of Hearts
5 of Hearts
6 of Hearts
7 of Hearts
8 of Hearts
9 of Hearts
10 of Hearts
Jack of Hearts
Queen of Hearts
King of Hearts
Ace of Spades
2 of Spades
3 of Spades
4 of Spades
5 of Spades
6 of Spades
7 of Spades
8 of Spades
9 of Spades
10 of Spades
Jack of Spades
Queen of Spades
King of Spades
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> deck1 = Deck()
>>> deck1.shuffle()
>>> print(deck1)
9 of Spades
10 of Hearts
5 of Clubs
4 of Diamonds
9 of Diamonds
6 of Diamonds
3 of Hearts
7 of Diamonds
9 of Clubs
5 of Hearts
8 of Clubs
8 of Spades
7 of Hearts
3 of Diamonds
6 of Hearts
2 of Hearts
2 of Diamonds
King of Clubs
4 of Clubs
5 of Diamonds
Queen of Diamonds
King of Spades
4 of Spades
Jack of Clubs
Jack of Spades
7 of Spades
3 of Clubs
9 of Hearts
6 of Clubs
Queen of Clubs
King of Diamonds
Ace of Diamonds
2 of Clubs
Ace of Spades
10 of Clubs
Queen of Hearts
4 of Hearts
7 of Clubs
2 of Spades
Jack of Hearts
King of Hearts
Jack of Diamonds
5 of Spades
6 of Spades
8 of Hearts
Ace of Clubs
10 of Diamonds
8 of Diamonds
Ace of Hearts
3 of Spades
10 of Spades
Queen of Spades
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> hand = Hand('new hand')
>>> hand.cards
[]
>>> hand.label
'new hand'
>>> deck = Deck()
>>> card = deck.pop_card(card)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    card = deck.pop_card(card)
NameError: name 'card' is not defined
>>> card = deck.pop_card
>>> card
<bound method Deck.pop_card of <__main__.Deck object at 0x10985ef28>>
>>> print(card)
<bound method Deck.pop_card of <__main__.Deck object at 0x10985ef28>>
>>> had.add_card(card)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    had.add_card(card)
NameError: name 'had' is not defined
>>> hand.add_card(card)
>>> print(hand)
<bound method Deck.pop_card of <__main__.Deck object at 0x10985ef28>>
>>> hand.cards
[<bound method Deck.pop_card of <__main__.Deck object at 0x10985ef28>>]
>>> hand.label
'new hand'
>>> hand.cards
[<bound method Deck.pop_card of <__main__.Deck object at 0x10985ef28>>]
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> deck =Deck()
>>> had = Hand('hand1')
>>> had.add_card(deck.pop_card)
>>> had2 = Hand('hand2')
>>> had2.add_card(deck.pop_card)
>>> had.move_cards(had2,1)
>>> had
<__main__.Hand object at 0x1039afcf8>
>>> print(had)

>>> print(had2)
<bound method Deck.pop_card of <__main__.Deck object at 0x10488e438>>
<bound method Deck.pop_card of <__main__.Deck object at 0x10488e438>>
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Hi, I am Henry
Henry
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Hi, I am Henry
I was built in 2008
Hi, I am Marvin
It's not known, when I was created!
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Robot('Marvin', 1979)
Type of x_str:  <class 'str'>
Robot('Marvin', 1979)
Type of new: <class '__main__.Robot'>
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Name: Marvin, Build Year: 1979
Type of x_str:  <class 'str'>
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa12-part1.py", line 24, in <module>
    new = eval(x_str)
  File "<string>", line 1
    Name: Marvin, Build Year: 1979
        ^
SyntaxError: invalid syntax
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Robot("Marvin",1979) <class 'str'>
Name: Marvin, Build Year: 1979
Type of new: <class '__main__.Robot'>
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> x= A()
>>> x.pub
'I am public'
>>> x.pub = x.pub + " and my value can be changed"
>>> x.pub
'I am public and my value can be changed'
>>> x._prot
'I am protected'
>>> x.__priv
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    x.__priv
AttributeError: 'A' object has no attribute '__priv'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
Hi, I am Marvin
I was built in the year 1979!
Hi, I am Caliban
I was built in the year 1993!
>>> x.name
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x.name
AttributeError: 'Robot' object has no attribute 'name'
>>> x.__name
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x.__name
AttributeError: 'Robot' object has no attribute '__name'
>>> print(x)
Name: Marvin, Build Year: 1979
>>> repr(x)
"Robot('Marvin', 1979)"
>>> print(str(x))
Name: Marvin, Build Year: 1979
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a=A()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a=A()
TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
>>> a= A(2,3)
>>> a.getx()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.getx()
AttributeError: 'A' object has no attribute 'getx'
>>> a.GetX()
2
>>> a.GetY()
3
>>> a.SetY(2)
>>> a.y
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.y
AttributeError: 'A' object has no attribute 'y'
>>> a.GetY()
2
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> Thing("front door key", "under the door mat")
<__main__.Thing object at 0x10deb5c18>
>>> a =Thing("front door key", "under the door mat")
>>> a
<__main__.Thing object at 0x10ded65f8>
>>> b= Thing("rusty key", "in your jacket pocket")
>>> b
<__main__.Thing object at 0x10f967ac8>
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a = Thing("rusty key", "in your jacket pocket")
>>> a.description()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.description()
TypeError: description() takes 0 positional arguments but 1 was given
>>> a.description()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.description()
TypeError: description() takes 0 positional arguments but 1 was given
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a=  Thing("rusty key", "in your jacket pocket")
>>> a.description()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.description()
  File "/Users/janechoi/Documents/pa12-part1.py", line 27, in description
    return 'The' + self.name +  'is' + self.location
AttributeError: 'Thing' object has no attribute 'location'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>>  Thing("rusty key", "in your jacket pocket")
SyntaxError: unexpected indent
>>> a= Thing("rusty key", "in your jacket pocket")
>>> a.description()
'Therusty keyisin your jacket pocket'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a= Thing("rusty key", "in your jacket pocket")
>>> a.description()
'Therusty key is in your jacket pocket'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a = Openable("small window", "in the north wall", True)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a = Openable("small window", "in the north wall", True)
  File "/Users/janechoi/Documents/pa12-part1.py", line 38, in __init__
    super().__init__()
TypeError: __init__() missing 2 required positional arguments: 'pname' and 'plocation'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a= Openable("small window", "in the north wall", True)
>>> a.description()
'Thesmall window is in the north wall'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a= Openable("small window", "in the north wall", True)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a= Openable("small window", "in the north wall", True)
TypeError: __init__() takes from 1 to 2 positional arguments but 4 were given
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a=Openable("small window", "in the north wall", True)
>>> a.description()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.description()
  File "/Users/janechoi/Documents/pa12-part1.py", line 47, in description
    return super().description + 'is' + self.open
TypeError: unsupported operand type(s) for +: 'method' and 'str'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a=Openable("small window", "in the north wall", True)
>>> a.description()
<bound method Thing.description of <__main__.Openable object at 0x105907be0>>
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>>  a=Openable("small window", "in the north wall", True)
SyntaxError: unexpected indent
>>> a=Openable("small window", "in the north wall", True)
>>> a.description()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.description()
  File "/Users/janechoi/Documents/pa12-part1.py", line 48, in description
    return 'The' + self.name  + self.location + 'is' + self.open
TypeError: can only concatenate str (not "bool") to str
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a=Openable("small window", "in the north wall", True)
>>> a.description()
'Thesmall windowin the north wallisTrue'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a=Openable("small window", "in the north wall", True)
>>> a.description()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.description()
  File "/Users/janechoi/Documents/pa12-part1.py", line 47, in description
    if self.open == T:
NameError: name 'T' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a=Openable("small window", "in the north wall", True)
>>> a.description()
'Thesmall windowin the north wallis open'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a=Openable("small window", "in the north wall", True)
>>> a.description()
'The small windowin the north wall is open'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> w.try_open()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    w.try_open()
NameError: name 'w' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> w.try_open()
False
>>> n.try_open()
True
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a=Lockable("front door", "in the foyer", house_key, False, True)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a=Lockable("front door", "in the foyer", house_key, False, True)
NameError: name 'house_key' is not defined
>>> house_key = Thing('house_key', 'house')
>>> a =Lockable("front door", "in the foyer", house_key, False, True)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a =Lockable("front door", "in the foyer", house_key, False, True)
  File "/Users/janechoi/Documents/pa12-part1.py", line 69, in __init__
    super().__init(self, pname,plocation, popen = False)
AttributeError: 'super' object has no attribute '_Lockable__init'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a =Lockable("front door", "in the foyer", house_key, False, True)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a =Lockable("front door", "in the foyer", house_key, False, True)
  File "/Users/janechoi/Documents/pa12-part1.py", line 69, in __init__
    super().__init(self, pname,plocation, popen )
AttributeError: 'super' object has no attribute '_Lockable__init'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a =Lockable("front door", "in the foyer", house_key, False, True)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a =Lockable("front door", "in the foyer", house_key, False, True)
  File "/Users/janechoi/Documents/pa12-part1.py", line 69, in __init__
    super().__init__(self, pname,plocation,popen)
TypeError: __init__() takes from 3 to 4 positional arguments but 5 were given
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a =Lockable("front door", "in the foyer", house_key, False, True)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a =Lockable("front door", "in the foyer", house_key, False, True)
  File "/Users/janechoi/Documents/pa12-part1.py", line 68, in __init__
    super().__init__(self, pname,plocation,popen)
TypeError: __init__() takes from 3 to 4 positional arguments but 5 were given
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> a =Lockable("front door", "in the foyer", house_key, False, True)
>>> a.description()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.description()
  File "/Users/janechoi/Documents/pa12-part1.py", line 47, in description
    if self.open == True :
AttributeError: 'Lockable' object has no attribute 'open'
>>> a.key
<__main__.Thing object at 0x1102b3128>
>>> a.is_locked
True
>>> p.is_open
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    p.is_open
NameError: name 'p' is not defined
>>> a.is_open
False
>>> b =Lockable("ancient treasure chest", "at the bottom of the sea", rusty_key)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    b =Lockable("ancient treasure chest", "at the bottom of the sea", rusty_key)
TypeError: __init__() missing 1 required positional argument: 'popen'
>>> b=Lockable("ancient treasure chest", "at the bottom of the sea", rusty_key)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    b=Lockable("ancient treasure chest", "at the bottom of the sea", rusty_key)
TypeError: __init__() missing 1 required positional argument: 'popen'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> b=Lockable("ancient treasure chest", "at the bottom of the sea", rusty_key)
>>> b.open
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    b.open
AttributeError: 'Lockable' object has no attribute 'open'
>>> b.is_open
False
>>> b.is_locked
False
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> chest.description()
'The ancient treasure chestat the bottom of the sea is closed but unlocked'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> diary.description()
"The diaryunder Sam's bed is open"
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> diary.try_open()
>>> chest.try_open()
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> diary.try_open()
False
>>> chest.try_open()
True
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> newdiary_try_open()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    newdiary_try_open()
NameError: name 'newdiary_try_open' is not defined
>>> newdiary.try_open()
False
>>> newdiary.description()
"The diary under Sam's bed is locked"
>>> diary.description()
"The diary under Sam's bed is open"
>>> diary.try_open()
False
>>> chest.description()
'The ancient treasure chest at the bottom of the sea is closed but unlocked'
>>> chest.try_open()
True
>>> chest.decription()
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    chest.decription()
AttributeError: 'Lockable' object has no attribute 'decription'
>>> chest.description()
'The ancient treasure chest at the bottom of the sea is closed but unlocked'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> chest.description()
'The ancient treasure chest at the bottom of the sea is closed but unlocked'
>>> chest.try_open()
True
>>> chest.description()
'The ancient treasure chest at the bottom of the sea is open'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> chest.description()
'The ancient treasure chest at the bottom of the sea is closed but unlocked'
>>> chest.try_unlock_with(rusty_key)
False
>>> diary.description()
"The diary under Sam's bed is open"
>>> diary.try_unlock_with(rusty_key)
False
>>> newdiary_description()
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    newdiary_description()
NameError: name 'newdiary_description' is not defined
>>> newdiary.description()
"The diary under Sam's bed is locked"
>>> newdiary.try_unlock_with(rusty_key)
True
>>> newdiary.description()
"The diary under Sam's bed is closed but unlocked"
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
>>> door.description()
'The door  at front door  is locked'
>>> door.try_unlock_with(rusty_key)
False
>>> door.description()
'The door  at front door  is locked'
>>> door.try_unlock_with(house_key)
True
>>> door.description()
'The door  at front door  is closed but unlocked'
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
***First, let's test the Thing class***
Creating house_key with name 'front door key' and location 'in your jacket pocket'...
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
***First, let's test the Thing class***
Creating house_key with name 'front door key' and location 'in your jacket pocket'...
Thehouse key is in your jacket pocket
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
***First, let's test the Thing class***
Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
***First, let's test the Thing class***
Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
***Now, let's test the Openable class***
Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large windowin the south wall is open
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
***First, let's test the Thing class***
\Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
\***Now, let's test the Openable class***
\Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large windowin the south wall is open
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large windowin the south wall is open
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large windowin the south wall is open
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa12-part1.py", line 135, in <module>
    print('window1.try_open() returned the value' + window1.try_open())
TypeError: can only concatenate str (not "bool") to str
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
window1.try_open() returned the valueFalse

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...

 window1.try_open() returned the value False
The large window in the south wall is open

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
\n Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
---------------------------------------------------------------------------------------------------------------------------

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 Now, a book ***

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
---------------------------------------------------------------------------------------------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
-----------------------------------------------------------------------------------

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 Now, a book ***

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
-----------------------------------------------------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
--------------------------------------------------------------------------------

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 Now, a book ***

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
--------------------------------------------------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
--------------------------------------------------------------------------------

 ***Now, let's test the Openable class***

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### Now, a book 

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
--------------------------------------------------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------

 ***First, let's test the Thing class***

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
--------------------------------------------------------------------------------

 ***Now, let's test the Openable class***

 #### a window 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book 

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
--------------------------------------------------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------

 ***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
--------------------------------------------------------------------------------

 ***Now, let's test the Openable class***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
--------------------------------------------------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 
Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable class***

 #### a window (Openable) 
Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)
Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
--------------------------------------------------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 
Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable class***

 #### a window (Openable) 
Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open
Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)
Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed
Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable class***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'Front door' and location 'at front door' ,key house_key,  open state False, and locked status True...
The Front door  at front door  is locked
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'Front door' and location 'at front of the house' ,key house_key,  open state False, and locked status True...
The Front door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the valueFalse
The Front door  at front of the house  is locked

 #### a diary (Lockable) 
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'Front door' and location 'at front of the house' ,key house_key,  open state False, and locked status True...
The Front door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The Front door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa12-part1.py", line 174, in <module>
    print('door1.try_unlock_with(rusty_key) returned the value ' + str(door1.try_unlock_with(rusty_key)))
NameError: name 'rusty_key' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The house key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The rusty key is in your jeans pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'Front door' and location 'at front of the house' ,key house_key,  open state False, and locked status True...
The Front door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The Front door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa12-part1.py", line 182, in <module>
    print('door1.try_unlock_with(rusty_key) returned the value ' + str(door1.try_unlock_with(rusty_key)))
NameError: name 'rusty_key' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'Front door' and location 'at front of the house' ,key house_key,  open state False, and locked status True...
The Front door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The Front door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The Front door  at front of the house  is locked

 #### a diary (Lockable) 
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked status True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 #### a diary (Lockable) 
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked status True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 #### a diary (Lockable) 
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked status True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open

 #### a diary (Lockable) 
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket

 #### a tiny_key (Thing) 

 Creating tiny_key with name 'tiny key' and location 'in the back yard'...
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open

 #### a diary (Lockable) 

 Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...
The diary under clothes is open
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket

 #### a tiny_key (Thing) 

 Creating tiny_key with name 'tiny key' and location 'in the back yard'...
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open

 #### a diary (Lockable) 

 Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...
The diary under clothes is open

 Attempting to open my_diary...
my_diary.try_open() returned the value False
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket

 #### a tiny_key (Thing) 

 Creating tiny_key with name 'tiny key' and location 'in the back yard'...
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open

 #### a diary (Lockable) 

 Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...
The diary under clothes is open

 Attempting to open my_diary...
my_diary.try_open() returned the value False

 Attempting to unlock my_diary with tiny_key...
my_diary.try_unlock_with(tiny_key) returned the value False
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket

 #### a tiny_key (Thing) 

 Creating tiny_key with name 'tiny key' and location 'in the back yard'...
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open

 #### a diary (Lockable) 

 Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...
The diary under clothes is open

 Attempting to open my_diary...
my_diary.try_open() returned the value False
The diary under clothes is open

 Attempting to unlock my_diary with tiny_key...
my_diary.try_unlock_with(tiny_key) returned the value False
The diary under clothes is open
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket

 #### a tiny_key (Thing) 

 Creating tiny_key with name 'tiny key' and location 'in the back yard'...
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open

 #### a diary (Lockable) 

 Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...
The diary under clothes is open

 Attempting to open my_diary...
my_diary.try_open() returned the value False
The diary under clothes is open

 Attempting to unlock my_diary with tiny_key...
my_diary.try_unlock_with(tiny_key) returned the value False
The diary under clothes is open

 #### an ancient treasure chest (Lockable) 

 Creating chest with name 'ancient treasure chest' and location 'at the bottom of the sea' ,key rusty_key,  and default open state and locked state...
The ancient treasure chest at the bottom of the sea is closed but unlocked
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket

 #### a tiny_key (Thing) 

 Creating tiny_key with name 'tiny key' and location 'in the back yard'...
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open

 #### a diary (Lockable) 

 Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...
The diary under clothes is open

 Attempting to open my_diary...
my_diary.try_open() returned the value False
The diary under clothes is open

 Attempting to unlock my_diary with tiny_key...
my_diary.try_unlock_with(tiny_key) returned the value False
The diary under clothes is open

 #### an ancient treasure chest (Lockable) 

 Creating chest with name 'ancient treasure chest' and location 'at the bottom of the sea' ,key rusty_key,  and default open state and locked state...
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to unlock chest with house_key...
chest.try_unlock_with(house_key) returned the value False
The ancient treasure chest at the bottom of the sea is closed but unlocked
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket

 #### a tiny_key (Thing) 

 Creating tiny_key with name 'tiny key' and location 'in the back yard'...
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open

 #### a diary (Lockable) 

 Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...
The diary under clothes is open

 Attempting to open my_diary...
my_diary.try_open() returned the value False
The diary under clothes is open

 Attempting to unlock my_diary with tiny_key...
my_diary.try_unlock_with(tiny_key) returned the value False
The diary under clothes is open

 #### an ancient treasure chest (Lockable) 

 Creating chest with name 'ancient treasure chest' and location 'at the bottom of the sea' ,key rusty_key,  and default open state and locked state...
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to unlock chest with house_key...
chest.try_unlock_with(house_key) returned the value False
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to unlock chest with rusty_key...
chest.try_unlock_with(rusty_key) returned the value False
The ancient treasure chest at the bottom of the sea is closed but unlocked
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket

 #### a tiny_key (Thing) 

 Creating tiny_key with name 'tiny key' and location 'in the back yard'...
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open

 #### a diary (Lockable) 

 Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...
The diary under clothes is open

 Attempting to open my_diary...
my_diary.try_open() returned the value False
The diary under clothes is open

 Attempting to unlock my_diary with tiny_key...
my_diary.try_unlock_with(tiny_key) returned the value False
The diary under clothes is open

 #### an ancient treasure chest (Lockable) 

 Creating chest with name 'ancient treasure chest' and location 'at the bottom of the sea' ,key rusty_key,  and default open state and locked state...
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to unlock chest with house_key...
chest.try_unlock_with(house_key) returned the value False
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to unlock chest with rusty_key...
chest.try_unlock_with(rusty_key) returned the value False
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to open chest...
chest.try_open() returned the value True
The ancient treasure chest at the bottom of the sea is open
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket
-----------------------------------------

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The front door key is in your jacket pocket
-----------------------------------------

 #### a tiny_key (Thing) 

 Creating tiny_key with name 'tiny key' and location 'in the back yard'...
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open
-----------------------------------------

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open
-----------------------------------------

 #### a diary (Lockable) 

 Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...
The diary under clothes is open

 Attempting to open my_diary...
my_diary.try_open() returned the value False
The diary under clothes is open

 Attempting to unlock my_diary with tiny_key...
my_diary.try_unlock_with(tiny_key) returned the value False
The diary under clothes is open
-----------------------------------------

 #### an ancient treasure chest (Lockable) 

 Creating chest with name 'ancient treasure chest' and location 'at the bottom of the sea' ,key rusty_key,  and default open state and locked state...
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to unlock chest with house_key...
chest.try_unlock_with(house_key) returned the value False
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to unlock chest with rusty_key...
chest.try_unlock_with(rusty_key) returned the value False
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to open chest...
chest.try_open() returned the value True
The ancient treasure chest at the bottom of the sea is open
>>> 
============== RESTART: /Users/janechoi/Documents/pa12-part1.py ==============
--------------------------------------------------------------------------------
***First, let's test the Thing class***

 #### a house_key (Thing) 

 Creating house_key with name 'front door key' and location 'in your jacket pocket'...
The front door key is in your jacket pocket
-----------------------------------------

 #### a rusty_key (Thing) 

 Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...
The rusty key is in your jeans pocket
-----------------------------------------

 #### a tiny_key (Thing) 

 Creating tiny_key with name 'tiny key' and location 'in the back yard'...
The tiny key is in the back yard
--------------------------------------------------------------------------------
***Now, let's test the Openable ***

 #### a window (Openable) 

 Creating window1 with name 'large window' and location 'in the south wall' , and open state True...
The large window in the south wall is open

 Attempting to open window1...
window1.try_open() returned the value False
The large window in the south wall is open
-----------------------------------------

 #### a book (Openable)

 Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...
The Harry Potter on the bookshelf is closed

 Attempting to open book1...
book1.try_open() returned the value True
The Harry Potter on the bookshelf is open
--------------------------------------------------------------------------------
***And now, let's test the Lockable ***

 #### a door (Lockable) 

 Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...
The door  at front of the house  is locked

 Attempting to open door1...
door1.try_open() returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with rusty_key...
door1.try_unlock_with(rusty_key) returned the value False
The door  at front of the house  is locked

 Attempting to unlock door1 with house_key...
door1.try_unlock_with(house_key) returned the value True
The door  at front of the house  is closed but unlocked

 Attempting to open door1...
door1.try_open() returned the value True
The door  at front of the house  is open
-----------------------------------------

 #### a diary (Lockable) 

 Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...
The diary under clothes is open

 Attempting to open my_diary...
my_diary.try_open() returned the value False
The diary under clothes is open

 Attempting to unlock my_diary with tiny_key...
my_diary.try_unlock_with(tiny_key) returned the value False
The diary under clothes is open
-----------------------------------------

 #### an ancient treasure chest (Lockable) 

 Creating chest with name 'ancient treasure chest' and location 'at the bottom of the sea' ,key rusty_key,  and default open state and locked state...
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to unlock chest with house_key...
chest.try_unlock_with(house_key) returned the value False
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to unlock chest with rusty_key...
chest.try_unlock_with(rusty_key) returned the value False
The ancient treasure chest at the bottom of the sea is closed but unlocked

 Attempting to open chest...
chest.try_open() returned the value True
The ancient treasure chest at the bottom of the sea is open
>>> 
