Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon02.py ===========
please enter a number: 10
triple your number is... None
>>> type(pass)
SyntaxError: invalid syntax
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon02.py ===========
please enter a number: 100
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture05afternoon02.py", line 19, in <module>
    result2
NameError: name 'result2' is not defined
>>> print(triplicate)
<function triplicate at 0x10d0c5a70>
>>> type(triplicate)
<class 'function'>
>>> saved = print("hello")
hello
>>> saved
>>> type(saved)
<class 'NoneType'>
>>> print(saved)
None
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon02.py ===========
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture05afternoon02.py", line 19, in <module>
    print(pNumber)
NameError: name 'pNumber' is not defined
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon02.py ===========
please enter a number: 100None
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture05afternoon02.py", line 27, in <module>
    result = cubify( aNumber )
  File "/Users/Shared/Desktop/lecture05afternoon02.py", line 8, in cubify
    lTotal = pNumber * pNumber * pNumber
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon02.py ===========
1
please enter a number: 100
2
A
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture05afternoon02.py", line 34, in <module>
    result = cubify( aNumber )
  File "/Users/Shared/Desktop/lecture05afternoon02.py", line 12, in cubify
    lTotal = pNumber * pNumber * pNumber
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon02.py ===========
1
please enter a number: 100
2
A
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture05afternoon02.py", line 35, in <module>
    result = cubify( aNumber )
  File "/Users/Shared/Desktop/lecture05afternoon02.py", line 12, in cubify
    lTotal = pNumber ** 3
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon02.py ===========
1
please enter a number: 100
2
A
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture05afternoon02.py", line 38, in <module>
    result = cubify( aStringContainingANumber )
  File "/Users/Shared/Desktop/lecture05afternoon02.py", line 12, in cubify
    lTotal = pNumber * pNumber * pNumber
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon02.py ===========
1
please enter a number: 100
2
A
B
3
triple your number is... 1000000
4
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon02.py ===========
please enter a number: 100
triple your number is... 1000000
>>> cubifyPlusTip(100)
1000010.0
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon03.py ===========
are you happy today?no
I'm sorry...
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon03.py ===========
are you happy today? yes
That's great!
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon03.py ===========
are you happy today? NO
That's great!
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture05afternoon03.py ===========
are you happy today? NO
I'm sorry...
>>> 
