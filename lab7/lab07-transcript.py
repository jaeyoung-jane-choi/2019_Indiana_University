Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> a ='ab',
>>> type(a)
<class 'tuple'>
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> contains_only_integers(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    contains_only_integers(a)
NameError: name 'a' is not defined
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> contains_only_integers(1)
1
>>> contains_only_integers(1,2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    contains_only_integers(1,2)
TypeError: contains_only_integers() takes 1 positional argument but 2 were given
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> contains_only_integers('a',1,'b')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    contains_only_integers('a',1,'b')
TypeError: contains_only_integers() takes 1 positional argument but 3 were given
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> contains_only_integers(a,b,c)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    contains_only_integers(a,b,c)
NameError: name 'a' is not defined
>>> contains_only_integers('a','b',1)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    contains_only_integers('a','b',1)
TypeError: contains_only_integers() takes 1 positional argument but 3 were given
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> contains_only_integers(('2',1,11,2))
('2', 1, 11, 2)
>>> isintance(1,int)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    isintance(1,int)
NameError: name 'isintance' is not defined
>>> isinstance(1,int)
True
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> contains_only_integers(('2',1,11,2))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    contains_only_integers(('2',1,11,2))
  File "/Users/janechoi/Documents/lab07-functions.py", line 22, in contains_only_integers
    if result == T:
NameError: name 'T' is not defined
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> contains_only_integers(('2',1,11,2))
False
>>> contains_only_integers((121,1,11,2))
True
>>> contains_only_integers(('a',1,11,2))
False
>>> contains_only_integers((1.1,11.12,2.2))
False
>>> contains_only_integers((1,1,'a'))
False
>>> -1
-1
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> analyze_tuple_0(('jo',3))
2
>>> analyze_tuple_0(3)
-1
>>> analyze_tuple_0(True)
-1
>>> analyze_tuple_0(-3.4)
-1
>>> analyze_tuple_0(('jill','jo','jack'))
3
>>> analyze_tuple_0((3,4,13094,-3898237498237))
4
>>> analyze_tuple_0(('jo',3,'jakie'))
3
>>> analyze_tuple_0(1)
-1
>>> analyze_tuple_0('a')
-1
>>> analyze_tuple_0(('a',1,2,3))
4
>>> analyze_tuple_0(0)
-1
>>> analyze_tuple_0(not True)
-1
>>> analyze_tuple_0()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    analyze_tuple_0()
TypeError: analyze_tuple_0() missing 1 required positional argument: 'pTuple'
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> analyze_tuple_0(False)
-1
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> analyze_tuple_0(True)
-1
>>> analyze_tuple_0('t')
-1
>>> analyze_tuple_0(('t',))
1
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> contains_only_integers((1,2,3,4,'a'))
False
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
Traceback (most recent call last):
  File "/Users/janechoi/Documents/lab07-functions.py", line 33, in <module>
    print(counter)
NameError: name 'counter' is not defined
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> contains_only_integers((1,2,3,4,'a'))
4
False
>>> 
=========== RESTART: /Users/janechoi/Documents/lab07-functions.py ===========
>>> contains_only_integers((1,2,3,4,'1'))
False
>>> contains_only_integers((1,2,3,4,1,2,3,4,5,'a'))
False
>>> 
