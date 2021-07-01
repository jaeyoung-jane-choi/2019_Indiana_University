Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/janechoi/Documents/read03-functions.py ===========
>>> square(5)
25
>>> square(2.2) + 6
10.84
>>> 
=========== RESTART: /Users/janechoi/Documents/read03-functions.py ===========
the square of -6 is36
>>> square(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    square(a)
NameError: name 'a' is not defined
>>> 
=========== RESTART: /Users/janechoi/Documents/read03-functions.py ===========
the square of -6 is36
>>> square2(3)
9
>>> square(2.7)
7.290000000000001
>>> num
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> def square3(num):
	return num*num

>>> square3(5)
25
>>> 
=========== RESTART: /Users/janechoi/Documents/read03-functions.py ===========
the square of -6 is36
Currently, the variable result has the value 100
We're about to call the function square4.
We're inside the function square4.
Here, the variable result has the value 2.25
square4(1.5) is 2.25
We've just finished calling square4.
Now, result has the value 100
>>> 
=========== RESTART: /Users/janechoi/Documents/read03-functions.py ===========
the square of -6 is36
Currently, the variable result has the value 100
We're about to call the function square4.
We're inside the function square4.
Here, the variable result has the value 2.25
square4(1.5) is 2.25
We've just finished calling square4.
Now, result has the value 100
>>> double_dahs('na')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    double_dahs('na')
NameError: name 'double_dahs' is not defined
>>> double_dash('na')
'na-na'
>>> 
=========== RESTART: /Users/janechoi/Documents/read03-functions.py ===========
the square of -6 is36
Currently, the variable result has the value 100
We're about to call the function square4.
We're inside the function square4.
Here, the variable result has the value 2.25
square4(1.5) is 2.25
We've just finished calling square4.
Now, result has the value 100
>>> box_volume(2,5,1)
10
>>> 
=========== RESTART: /Users/janechoi/Documents/read03-functions.py ===========
the square of -6 is36
Currently, the variable result has the value 100
We're about to call the function square4.
We're inside the function square4.
Here, the variable result has the value 2.25
square4(1.5) is 2.25
We've just finished calling square4.
Now, result has the value 100
>>> help(square)
Help on function square in module __main__:

square(num)
    This function takes a number(float/int) into the square of the number
    
    num -> num

>>> help(square2)
Help on function square2 in module __main__:

square2(num)
    This function takes a number(float/int) into the square of the number and returns the result of it
    
    num -> num

>>> help(square3)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    help(square3)
NameError: name 'square3' is not defined
>>> help(square4)
Help on function square4 in module __main__:

square4(num)
    This function takes a number(float/int) into the square of the number
    
    num -> num

>>> help(double_dash)
Help on function double_dash in module __main__:

double_dash(text)
    This function takes a string and adds a dash inbetween
    
    string-> string

>>> help(box_volume)
Help on function box_volume in module __main__:

box_volume(width, height, depth)
    This function takes a width, a height, and a depth and calculates the volume of a box with the dimensions
    
    num, num, num -> num

>>> 
