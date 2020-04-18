Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /Users/Shared/Desktop/example01.py =================
 we're computing a square: 
 enter a number 22
 the square is: 484.0
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> print(def)
SyntaxError: invalid syntax
>>> print("hello")
hello
>>> input("hello")
hello
''
>>> len("plenty of functions accept strings as inputs")
44
>>> str("string")
'string'
>>> print("hello", end="")
hello
>>> print( str ( 10 / 0 ) )
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print( str ( 10 / 0 ) )
ZeroDivisionError: division by zero
>>> "hello"[0]
'h'
>>> a = "hello"
>>> a[0]
'h'
>>> a[0] = "H"
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a[0] = "H"
TypeError: 'str' object does not support item assignment
>>> a[0].upper()
'H'
>>> a
'hello'
>>> int("22")
22
>>> int("twentytwo")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int("twentytwo")
ValueError: invalid literal for int() with base 10: 'twentytwo'
>>> int(True)
1
>>> int(print)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    int(print)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'builtin_function_or_method'
>>> 1 =
SyntaxError: invalid syntax
>>> 
=============== RESTART: /Users/Shared/Desktop/test01written.py ===============
Traceback (most recent call last):
  File "/Users/Shared/Desktop/test01written.py", line 11, in <module>
    len(my_word)
NameError: name 'my_word' is not defined
>>> 
=============== RESTART: /Users/Shared/Desktop/test01written.py ===============
>>> 
=============== RESTART: /Users/Shared/Desktop/test01written.py ===============
-2
2
0.09090909090909091

12.3
-3.1415926
true
True
True
no
11
g
_
n
4.0
3.6666666666666665
11
programmingprogrammingprogramming
False
False
True
False
>>> 
================= RESTART: /Users/Shared/Desktop/example01.py =================
 we're computing a square: 
 enter a number 11
 the square is: (121.0, 22, 'hello')
>>> 
