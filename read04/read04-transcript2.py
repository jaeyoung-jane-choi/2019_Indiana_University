Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/janechoi/Documents/read04.functions.py ===========
factorial has been called with n = 5
factorial has been called with n = 4
factorial has been called with n = 3
factorial has been called with n = 2
factorial has been called with n = 1
intermediate result for  2  * factorial( 1 ):  2
intermediate result for  3  * factorial( 2 ):  6
intermediate result for  4  * factorial( 3 ):  24
intermediate result for  5  * factorial( 4 ):  120
120
>>> help(facotorial)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    help(facotorial)
NameError: name 'facotorial' is not defined
>>> help(factorial)
Help on function factorial in module __main__:

factorial(n)
    This function takes a number and returns the factorial of the number
    
    
    number -> number

>>> 
=========== RESTART: /Users/janechoi/Documents/read04-turtle01.py ===========
>>> 
=========== RESTART: /Users/janechoi/Documents/read04-turtle02.py ===========
I'm going to draw a Koch fractal curve.
What's the size of the smallest detail you'd like to see?
e.g. 200 no details, smaller more details: 200
>>> 
=========== RESTART: /Users/janechoi/Documents/read04-turtle02.py ===========
I'm going to draw a Koch fractal curve.
What's the size of the smallest detail you'd like to see?
e.g. 200 no details, smaller more details: 100
>>> 
=========== RESTART: /Users/janechoi/Documents/read04-turtle02.py ===========
I'm going to draw a Koch fractal curve.
What's the size of the smallest detail you'd like to see?
e.g. 200 no details, smaller more details: 
Traceback (most recent call last):
  File "/Users/janechoi/Documents/read04-turtle02.py", line 47, in <module>
    smallestDetail = int(input("e.g. 200 no details, smaller more details: "))
ValueError: invalid literal for int() with base 10: ''
>>> 
=========== RESTART: /Users/janechoi/Documents/read04-turtle02.py ===========
I'm going to draw a Koch fractal curve.
What's the size of the smallest detail you'd like to see?
e.g. 200 no details, smaller more details: 10
