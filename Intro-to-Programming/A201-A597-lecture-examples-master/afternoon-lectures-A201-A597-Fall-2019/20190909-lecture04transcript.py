Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> .lower()
SyntaxError: invalid syntax
>>> "hello".lower()
'hello'
>>> type("hello")
<class 'str'>
>>> "hello".upper()
'HELLO'
>>> dir("hello
    
SyntaxError: EOL while scanning string literal
>>> dir("hello")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> "hello".encode()
b'hello'
>>> "hello".islower()
True
>>> "Hello".islower()
False
>>> dir(12)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 12.to_bytes()
SyntaxError: invalid syntax
>>> aNumer = 12
>>> aNumer.to_bytes()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    aNumer.to_bytes()
TypeError: to_bytes() missing required argument 'length' (pos 1)
>>> aNumer.to_bytes(10)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    aNumer.to_bytes(10)
TypeError: to_bytes() missing required argument 'byteorder' (pos 2)
>>> aNumer.to_bytes(10, 1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    aNumer.to_bytes(10, 1)
TypeError: to_bytes() argument 2 must be str, not int
>>> aNumer.to_bytes(10, "let's try")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    aNumer.to_bytes(10, "let's try")
ValueError: byteorder must be either 'little' or 'big'
>>> aNumer.to_bytes(10, "little")
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> storeHere = int(aNumer)
>>> whatIsReturnedByPrint = print("helllllllooooo")
helllllllooooo
>>> whatIsReturnedByPrint
>>> type(whatIsReturnedByPrint)
<class 'NoneType'>
>>> None
>>> type(None)
<class 'NoneType'>
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture04afternoon01.py ===========
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture04afternoon01.py ===========
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture04afternoon01.py ===========
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture04afternoon01.py", line 5, in <module>
    gameStartingBanner()
NameError: name 'gameStartingBanner' is not defined
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture04afternoon01.py ===========
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture04afternoon01.py ===========
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
>>> print("the input to the function is the function's ...")
the input to the function is the function's ...
>>> sin(90)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    sin(90)
NameError: name 'sin' is not defined
>>> import Math
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    import Math
ModuleNotFoundError: No module named 'Math'
>>> import math
>>> math.sin(90)
0.8939966636005579
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture04afternoon01.py ===========
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture04afternoon01.py ===========
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture04afternoon01.py ===========
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
>>> thisIsTheOuputStorage
126
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture04afternoon01.py ===========
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
Traceback (most recent call last):
  File "/Users/Shared/Desktop/lecture04afternoon01.py", line 44, in <module>
    myInputParameter
NameError: name 'myInputParameter' is not defined
>>> 
=========== RESTART: /Users/Shared/Desktop/lecture04afternoon01.py ===========
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
---------------------------------
                                 
  colossal cave adventure game   
                                 
---------------------------------
three times 42 is 126
>>> triplicate(100)
300
>>> tip15(29.99)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tip15(29.99)
NameError: name 'tip15' is not defined
>>> 
