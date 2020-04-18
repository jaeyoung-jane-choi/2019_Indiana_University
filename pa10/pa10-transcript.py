Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /Users/janechoi/Documents/1.py ==================
>>> 
================== RESTART: /Users/janechoi/Documents/1.py ==================
Traceback (most recent call last):
  File "/Users/janechoi/Documents/1.py", line 26, in <module>
    new = Employee()
TypeError: __init__() missing 3 required positional arguments: 'name', 'birth_year', and 'salary'
>>> 
================== RESTART: /Users/janechoi/Documents/1.py ==================
Traceback (most recent call last):
  File "/Users/janechoi/Documents/1.py", line 28, in <module>
    repr(new)
TypeError: __repr__ returned non-string (type NoneType)
>>> 
================== RESTART: /Users/janechoi/Documents/1.py ==================
>>> 
================== RESTART: /Users/janechoi/Documents/1.py ==================
>>> repr(x)
'Robot("Marvin",1979)'
>>> str(x
	)
'Name: Marvin, Build Year: 1979'
>>> type(repr(x))
<class 'str'>
>>> eval(x)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    eval(x)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> eval(repr(x))
Robot("Marvin",1979)
>>> type(eval(repr(x)))
<class '__main__.Robot'>
>>> 100/10
10.0
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 68, in <module>
    bike1 = ElectricScooter()
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 11, in __init__
    self.nickname
AttributeError: 'ElectricScooter' object has no attribute 'nickname'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    bike1.info()
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 23, in info
    '\n The remaining usable minutes is...' + str(self.usableminutes))
AttributeError: 'ElectricScooter' object has no attribute 'usableminutes'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
The nickname is..
 The remaining usable minutes is...100
>>> bike1.unlock('jane', 100)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    bike1.unlock('jane', 100)
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 32, in unlock
    if self.usableminutes < 10 :
AttributeError: 'ElectricScooter' object has no attribute 'usableminutes'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
The nickname is..
 The remaining usable minutes is...100
>>> bike1.unlock('jane',100)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    bike1.unlock('jane',100)
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 32, in unlock
    if self.usableminutes < 10 :
AttributeError: 'ElectricScooter' object has no attribute 'usableminutes'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
The nickname is..
 The remaining usable minutes is...100
>>> bike1.unlock('jane',100)
The current money remaining of the scooter is..100
 and the remaining charge is..100
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('jane', 10)
The current money remaining of the scooter is..10$
 and the remaining charge is..100
>>> bike1.drive(10)
>>> bike1.nickname
'jane'
>>> bike1.usableminutes
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    bike1.usableminutes
AttributeError: 'ElectricScooter' object has no attribute 'usableminutes'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('jill',1)
The current money remaining of the scooter is..1$
 and the remaining charge is..100
>>> bike1.drive(12)
>>> bike1.useableminutes
98.8
>>> bike1.payment
0.88
>>> bike1.drive(100)
>>> bike1.useableminutes
88.8
>>> bike1.payment
1.1102230246251565e-16
>>> bike1.drive(100)
>>> bike1.payment
0.0
>>> bike1.usableminutes
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    bike1.usableminutes
AttributeError: 'ElectricScooter' object has no attribute 'usableminutes'
>>> bike1.useableminutes
78.8
>>> bike1.drive(10)
Your payment is currently 0 or the charge is below 10 usable minutes.
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.drive(10)
Your payment is currently 0 or the charge is below 10 usable minutes.
>>> bike1.lockstatus
True
>>> bike1.unlock('Jane',1)
The current money remaining of the scooter is..1$
 and the remaining charge is..100
>>> bike1.drive(10)
>>> bike1.lockstatus
False
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
The nickname is..and the remaining usable minutes is...
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    bike1.info()
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 27, in info
    print(self.usableminutes)
AttributeError: 'ElectricScooter' object has no attribute 'usableminutes'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    bike1.info()
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 26, in info
    return (self.nickname, self.usableminutes)
AttributeError: 'ElectricScooter' object has no attribute 'usableminutes'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
''
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    bike1.info()
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 26, in info
    return (self.nickname, self.usableminutes)
AttributeError: 'ElectricScooter' object has no attribute 'usableminutes'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
('', 100)
>>> a = bike1.info()
>>> a[1]
100
>>> type(a[1])
<class 'int'>
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
('', 100.0)
>>> a= bike1.info()
>>> a[1]
100.0
>>> type(a[1]
	 )
<class 'float'>
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('j',19)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    bike1.unlock('j',19)
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 41, in unlock
    current.status = str(self.payment) +str(self.usableminutes)
AttributeError: 'ElectricScooter' object has no attribute 'usableminutes'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('j',19)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    bike1.unlock('j',19)
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 41, in unlock
    current.status = str(self.payment) +str(self.useableminutes)
NameError: name 'current' is not defined
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('j',19)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    bike1.unlock('j',19)
  File "/Users/janechoi/Documents/pa10-ElectricScooter.py", line 44, in unlock
    return current.status
NameError: name 'current' is not defined
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('j',19)
'19100.0'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('j',19)
'19 100.0'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('j',100)
'100 100.0'
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('j',19)
'The current payment is..19 The current usable minutes is..100.0'
>>> bike1.unlock('j',10)
'The current payment is..10 The current usable minutes is..100.0'
>>> bike1.drive(10)
>>> bike.info()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    bike.info()
NameError: name 'bike' is not defined
>>> bike1.info()
('j', 99.0)
>>> bike1.payment
9.9
>>> bike1.unlock('jane',100)
'The current payment is..100 The current usable minutes is..99.0'
>>> bike2.unlock('Jane',100)
'The current payment is..100 The current usable minutes is..100.0'
>>> bike2.drive(10)
>>> bike2.payment
99.9
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
('', 100.0)
>>> bike1.unlock('Jane',10)
'The current payment is..10 The current usable minutes is..100.0'
>>> bike1.drive(1000)
>>> bike1.info()
('Jane', 0.0)
>>> bike1.drive(10)
Your payment is currently 0 or the charge is below 10 usable minutes.
>>> bike1.payment
0.0
>>> bike2.info()
('', 100.0)
>>> bike2.unlock('Jill',1)
'The current payment is..1 The current usable minutes is..100.0'
>>> bike2.drive(10)
>>> bike2.info()
('Jill', 99.0)
>>> bike2.drive(1)
>>> bike2.info()
('Jill', 98.9)
>>> bike2.payment
0.89
>>> bike2.drive(1)
>>> bike2.payment
0.88
>>> bike2.payment(10)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    bike2.payment(10)
TypeError: 'float' object is not callable
>>> bike2.drive(10)
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.info()
('', 100.0)
>>> bike1.unlock('Jane',10)
'The current payment is..10 The current usable minutes is..100.0'
>>> bike1.drive(1000)
Your payment is currently 0 or the charge is below 10 usable minutes.
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('jane',10)
'The current payment is..10 The current usable minutes is..100.0'
>>> bike1.drive(1000)
'The current payment is..0.0 The current usable minutes is..0.0'
>>> bike2.unlock('d',10)
'The current payment is..10 The current usable minutes is..100.0'
>>> bike2.drive(1002)
'The current payment is..-0.019999999999999574 The current usable minutes is..-0.20000000000000284'
>>> a = bike1.drive(1)
Your payment is currently 0 or the charge is below 10 usable minutes.
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> bike1.unlock('j',10)
'The current payment is..10 The current usable minutes is..100.0'
>>> bike1.drive(10)
'The current payment is..9.9 The current usable minutes is..99.0'
>>> a=bike1.info()
>>> a
('j', 99.0)
>>> type(a)
<class 'tuple'>
>>> 
========= RESTART: /Users/janechoi/Documents/pa10-ElectricScooter.py =========
>>> a = new()
>>> a.nickname
''
>>> 
