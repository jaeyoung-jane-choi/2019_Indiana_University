Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/Shared/Desktop/lecture08example01.py ============
>>> myString[10]
'k'
>>> 
============ RESTART: /Users/Shared/Desktop/lecture08example01.py ============
>>> myOtherString[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    myOtherString[0]
IndexError: string index out of range
>>> 
============ RESTART: /Users/Shared/Desktop/lecture08example01.py ============
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
>>> myString = ""
>>> print_a_char(myString)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print_a_char(myString)
  File "/Users/Shared/Desktop/lecture08example01.py", line 21, in print_a_char
    print( myString[i] )
TypeError: string indices must be integers
>>> print_a_char(0)
>>> 
============ RESTART: /Users/Shared/Desktop/lecture08example01.py ============
debugging recursion... now i = 0
a
debugging recursion... now i = 1
b
debugging recursion... now i = 2
c
debugging recursion... now i = 3
d
debugging recursion... now i = 4
e
debugging recursion... now i = 5
f
debugging recursion... now i = 6
g
debugging recursion... now i = 7
h
debugging recursion... now i = 8
i
debugging recursion... now i = 9
j
debugging recursion... now i = 10
k
debugging recursion... now i = 11
l
debugging recursion... now i = 12
m
debugging recursion... now i = 13
n
debugging recursion... now i = 14
o
debugging recursion... now i = 15
p
debugging recursion... now i = 16
q
debugging recursion... now i = 17
r
debugging recursion... now i = 18
s
debugging recursion... now i = 19
t
debugging recursion... now i = 20
u
debugging recursion... now i = 21
v
debugging recursion... now i = 22
w
debugging recursion... now i = 23
x
debugging recursion... now i = 24
y
debugging recursion... now i = 25
z
debugging base case... now i = 26
>>> 
============ RESTART: /Users/Shared/Desktop/lecture08example02.py ============
please enter a string
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture08example02.py", line 14, in <module>
    myString = input("please enter a string")
KeyboardInterrupt
>>> 
============ RESTART: /Users/Shared/Desktop/lecture08example02.py ============
please enter a string: let me enter a string
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
l
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture08example02.py", line 23, in <module>
    print(  myString[myIndex] )
KeyboardInterrupt
>>> 
============ RESTART: /Users/Shared/Desktop/lecture08example02.py ============
please enter a string: let's see if now it works
l
e
t
'
s
 
s
e
e
 
i
f
 
n
o
w
 
i
t
 
w
o
r
k
s
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture08example02.py", line 23, in <module>
    print(  myString[myIndex] )
IndexError: string index out of range
>>> 
============ RESTART: /Users/Shared/Desktop/lecture08example02.py ============
please enter a string: keep printing
k
e
e
p
 
p
r
i
n
t
i
n
g
>>> 
============ RESTART: /Users/Shared/Desktop/lecture08example02.py ============
please enter a string: let's test our debugging
debug, before while loop begins, myIdex = 0
debug, before printing, myIdex = 0
l
debug, after printing, myIdex = 0
debug, after incrementing, myIdex = 1
debug, before printing, myIdex = 1
e
debug, after printing, myIdex = 1
debug, after incrementing, myIdex = 2
debug, before printing, myIdex = 2
t
debug, after printing, myIdex = 2
debug, after incrementing, myIdex = 3
debug, before printing, myIdex = 3
'
debug, after printing, myIdex = 3
debug, after incrementing, myIdex = 4
debug, before printing, myIdex = 4
s
debug, after printing, myIdex = 4
debug, after incrementing, myIdex = 5
debug, before printing, myIdex = 5
 
debug, after printing, myIdex = 5
debug, after incrementing, myIdex = 6
debug, before printing, myIdex = 6
t
debug, after printing, myIdex = 6
debug, after incrementing, myIdex = 7
debug, before printing, myIdex = 7
e
debug, after printing, myIdex = 7
debug, after incrementing, myIdex = 8
debug, before printing, myIdex = 8
s
debug, after printing, myIdex = 8
debug, after incrementing, myIdex = 9
debug, before printing, myIdex = 9
t
debug, after printing, myIdex = 9
debug, after incrementing, myIdex = 10
debug, before printing, myIdex = 10
 
debug, after printing, myIdex = 10
debug, after incrementing, myIdex = 11
debug, before printing, myIdex = 11
o
debug, after printing, myIdex = 11
debug, after incrementing, myIdex = 12
debug, before printing, myIdex = 12
u
debug, after printing, myIdex = 12
debug, after incrementing, myIdex = 13
debug, before printing, myIdex = 13
r
debug, after printing, myIdex = 13
debug, after incrementing, myIdex = 14
debug, before printing, myIdex = 14
 
debug, after printing, myIdex = 14
debug, after incrementing, myIdex = 15
debug, before printing, myIdex = 15
d
debug, after printing, myIdex = 15
debug, after incrementing, myIdex = 16
debug, before printing, myIdex = 16
e
debug, after printing, myIdex = 16
debug, after incrementing, myIdex = 17
debug, before printing, myIdex = 17
b
debug, after printing, myIdex = 17
debug, after incrementing, myIdex = 18
debug, before printing, myIdex = 18
u
debug, after printing, myIdex = 18
debug, after incrementing, myIdex = 19
debug, before printing, myIdex = 19
g
debug, after printing, myIdex = 19
debug, after incrementing, myIdex = 20
debug, before printing, myIdex = 20
g
debug, after printing, myIdex = 20
debug, after incrementing, myIdex = 21
debug, before printing, myIdex = 21
i
debug, after printing, myIdex = 21
debug, after incrementing, myIdex = 22
debug, before printing, myIdex = 22
n
debug, after printing, myIdex = 22
debug, after incrementing, myIdex = 23
debug, before printing, myIdex = 23
g
debug, after printing, myIdex = 23
debug, after incrementing, myIdex = 24
>>> 
============ RESTART: /Users/Shared/Desktop/lecture08example02.py ============
please enter a string: small
debug, before while loop begins, myIdex = 0
debug, before printing, myIdex = 0
s
debug, after printing, myIdex = 0
debug, after incrementing, myIdex = 1
debug, before printing, myIdex = 1
m
debug, after printing, myIdex = 1
debug, after incrementing, myIdex = 2
debug, before printing, myIdex = 2
a
debug, after printing, myIdex = 2
debug, after incrementing, myIdex = 3
debug, before printing, myIdex = 3
l
debug, after printing, myIdex = 3
debug, after incrementing, myIdex = 4
debug, before printing, myIdex = 4
l
debug, after printing, myIdex = 4
debug, after incrementing, myIdex = 5
>>> 
============= RESTART: /Users/Shared/Desktop/pa03-functions.py =============
This program will calculate the escape velocity for an object on a given body.
mass of the planet/body the object is escaping from (in Kg): 10
object's distance from center of planet (in m): 20
The escape velocity for the object is 8.167006795638167e-06 m/s.
>>> 
========= RESTART: /Users/Shared/Desktop/fileWithUnicodeInComments.py =========
This program will calculate the escape velocity for an object on a given body.
mass of the planet/body the object is escaping from (in Kg): 
