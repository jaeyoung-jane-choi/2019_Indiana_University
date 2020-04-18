Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskA.py ==============
>>> isInRecord('k',dic)
True
>>> isInRecord('o',dic)
True
>>> isInRecord('r',dic)
False
>>> isInRecord('?',dic)
True
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskA.py ==============
>>> addToRecord('k',dic)
{'K': 2, 'o': 4, 'k': 2, 'm': 2, '?': 1}
>>> addToRecord('k',dic)
{'K': 3, 'o': 5, 'k': 3, 'm': 3, '?': 1}
>>> addToRecord('r',dic)
{'K': 4, 'o': 6, 'k': 4, 'm': 4, '?': 1}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskA.py ==============
>>> addToRecord('k',dic)
{'K': 2, 'o': 4, 'k': 2, 'm': 2, '?': 2}
>>> addToRecord('r',dic)
{'K': 3, 'o': 5, 'k': 3, 'm': 3, '?': 3}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskA.py ==============
>>> addToRecord('k',dic)
{'K': 2, 'o': 4, 'k': 2, 'm': 2, '?': 2}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskA.py ==============
>>> addToRecord('k',dic)
{'K': 1, 'o': 3, 'k': 6, 'm': 1, '?': 1}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskA.py ==============
>>> addToRecord('k',dic)
{'K': 1, 'o': 3, 'k': 2, 'm': 1, '?': 1}
>>> addToRecord('k',dic)
{'K': 1, 'o': 3, 'k': 3, 'm': 1, '?': 1}
>>> addToRecord('e',dic)
{'K': 1, 'o': 3, 'k': 3, 'm': 1, '?': 1, 'e': 1}
>>> addToRecord('r',dic)
{'K': 1, 'o': 3, 'k': 3, 'm': 1, '?': 1, 'e': 1, 'r': 1}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskA.py ==============
>>> createRecord('string')
{'s': 1, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}
>>> createRecord('strings')
{'s': 1, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskA.py ==============
>>> createRecord('string')
{'s': 1, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}
>>> createRecord('strings')
{'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}
>>> createRecord('ssstring')
{'s': 3, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}
>>> createRecord('Kokomo')
{'K': 1, 'o': 3, 'k': 1, 'm': 1}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskA.py ==============
>>> frequencies('o',dic)
3
>>> frequencies('r',dic)
0
>>> frequencies('K',dic)
1
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskB.py ==============
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> makeHistogram("bicycling")
{'b': 1, 'i': 2, 'c': 2, 'y': 1, 'l': 1, 'n': 1, 'g': 1}
>>> a={'b': 1, 'i': 2, 'c': 2, 'y': 1, 'l': 1, 'n': 1, 'g': 1}
>>> a.values()
dict_values([1, 2, 2, 1, 1, 1, 1])
>>> a.values() = 's'
SyntaxError: can't assign to function call
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '#', 'c': '#', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    histoprint1(makeHistogram("bicycling"))
  File "/Users/janechoi/Documents/pa09-taskC.py", line 76, in histoprint1
    copy[keys] = '#'*keys.value()
AttributeError: 'str' object has no attribute 'value'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
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

>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'} 

>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'} 

>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))

 {'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': 2, 'c': 2, 'y': 1, 'l': 1, 'n': 1, 'g': 1}
{'b': '#', 'i': '##', 'c': 2, 'y': 1, 'l': 1, 'n': 1, 'g': 1}
{'b': '#', 'i': '##', 'c': '##', 'y': 1, 'l': 1, 'n': 1, 'g': 1}
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': 1, 'n': 1, 'g': 1}
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': 1, 'g': 1}
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': 1}
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
b : #
i : ##
c : ##
y : #
l : #
n : #
g : #
>>> histoprint1(makeHistogram("bicycling"))
b : #
i : ##
c : ##
y : #
l : #
n : #
g : #
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> histoprint2(makeHistogram("bicycling"))
b : #
i : ##
c : ##
y : #
l : #
n : #
g : #
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'},
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
{'b': '#', 'i': '##', 'c': '##', 'y': '#', 'l': '#', 'n': '#', 'g': '#'}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
b #
i ##
c ##
y #
l #
n #
g #
>>> histoprint1(makeHistogram("bicycling"))
b #
i ##
c ##
y #
l #
n #
g #
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint2(makeHistogram("bicycling"))
b #
i ##
c ##
y #
l #
n #
g #
>>> a=histoprint1(makeHistogram("bicycling"))
b #
i ##
c ##
y #
l #
n #
g #
>>> type(a)
<class 'NoneType'>
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"), 1)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    histoprint1(makeHistogram("bicycling"), 1)
TypeError: histoprint1() takes 1 positional argument but 2 were given
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"))
TypeError: histoprint3() missing 1 required positional argument: 'i'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
b #
i ##
c ##
y #
l #
n #
g #
>>> histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 113, in histoprint3
    if values >=i :
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"))
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"))
TypeError: histoprint3() missing 1 required positional argument: 'i'
>>> histoprint3(makeHistogram("bicycling"),1)
#
##
##
#
#
#
#
>>> histoprint3(makeHistogram("bicycling"),2)
##
##
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 114, in histoprint3
    print(copy(values),values)
TypeError: 'dict' object is not callable
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 114, in histoprint3
    print(copy[values],values)
KeyError: '#'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 114, in histoprint3
    print(copy[values]+values)
KeyError: '#'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 114, in histoprint3
    print(copy[values]+ str(values))
KeyError: '#'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
#
##
##
#
#
#
#
>>> a=copy[keys] = '#'* d[keys]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a=copy[keys] = '#'* d[keys]
NameError: name 'd' is not defined
>>> a=histoprint3(makeHistogram("bicycling"),1)
#
##
##
#
#
#
#
>>> type(a)
<class 'NoneType'>
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> a=histoprint3(makeHistogram("bicycling"),1)
b#
b##
b##
b#
b#
b#
b#
i#
i##
i##
i#
i#
i#
i#
c#
c##
c##
c#
c#
c#
c#
y#
y##
y##
y#
y#
y#
y#
l#
l##
l##
l#
l#
l#
l#
n#
n##
n##
n#
n#
n#
n#
g#
g##
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a=histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 115, in histoprint3
    print(key+values)
KeyboardInterrupt
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> a=histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a=histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 114, in histoprint3
    print(key+values)
NameError: name 'key' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> a=histoprint3(makeHistogram("bicycling"),1)
g#
g##
g##
g#
g#
g#
g#
>>> histoprint3(makeHistogram("bicycling"),1)
g#
g##
g##
g#
g#
g#
g#
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> a=histoprint3(makeHistogram("bicycling"),1)
#
##
##
#
#
#
#
>>> histoprint3(makeHistogram("bicycling"),2)
##
##
>>> histoprint3(makeHistogram("bicycling"),3)
>>> histoprint3(makeHistogram("bicycling"),1)
#
##
##
#
#
#
#
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 114, in histoprint3
    print(copy[values] + values)
KeyError: '#'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 113, in histoprint3
    if len(values) >= i :
TypeError: object of type 'int' has no len()
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 114, in histoprint3
    print(copy + copy[values])
KeyError: 1
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 114, in histoprint3
    print(copy +str(values))
TypeError: unsupported operand type(s) for +: 'dict' and 'str'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
#
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 113, in histoprint3
    if len(values) >=i :
TypeError: object of type 'int' has no len()
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
#
##
##
#
#
#
#
>>> histoprint3(makeHistogram("bicycling"),2)
##
##
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
b #
c ##
g #
i ##
l #
n #
y #
>>> histoprint1(makeHistogram("bicycling"))
b #
c ##
g #
i ##
l #
n #
y #
>>> histoprint2(makeHistogram("bicycling"))
b #
i ##
c ##
y #
l #
n #
g #
>>> histoprint1(makeHistogram("bicycling"))
b #
c ##
g #
i ##
l #
n #
y #
>>> histoprint1(makeHistogram("bicycling"))
b #
c ##
g #
i ##
l #
n #
y #
>>> histoprint1(makeHistogram("bicycling"))
b #
c ##
g #
i ##
l #
n #
y #
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
b #
c ##
g #
i ##
l #
n #
y #
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling"))
b #
i ##
c ##
y #
l #
n #
g #
>>> histoprint1(makeHistogram("bicycling"))
b #
i ##
c ##
y #
l #
n #
g #
>>> histoprint2(makeHistogram("bicycling"))
b #
c ##
g #
i ##
l #
n #
y #
>>> histoprint1(makeHistogram("bicycling"))
b #
i ##
c ##
y #
l #
n #
g #
>>> histoprint1(makeHistogram("bicycling"))
b #
i ##
c ##
y #
l #
n #
g #
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
#
##
##
#
#
#
#
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),2)
##
##
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
1
2
2
1
1
1
1
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    histoprint3(makeHistogram("bicycling"),1)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 114, in histoprint3
    copy[k] == values
NameError: name 'k' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
g #
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
b #
i ##
c ##
y #
l #
n #
g #
>>> histoprint3(makeHistogram("bicycling"),2)
i ##
c ##
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1(makeHistogram("bicycling")
		)
b #
i ##
c ##
y #
l #
n #
g #
>>> histoprint2(makeHistogram("bicycling"))
b #
c ##
g #
i ##
l #
n #
y #
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),1)
b #
i ##
c ##
y #
l #
n #
g #
>>> histoprint3(makeHistogram("bicycling"),2)
i ##
c ##
>>> histoprint3(makeHistogram("bicycling"),3)
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3(makeHistogram("bicycling"),2)
i : ##
c : ##
>>> histoprint2(makeHistogram("bicycling"))
b : #
c : ##
g : #
i : ##
l : #
n : #
y : #
>>> histoprint1(makeHistogram("bicycling"))
b : #
i : ##
c : ##
y : #
l : #
n : #
g : #
>>> 
histoprint1(makeHistogram("bicycling"))
b : #
i : ##
c : ##
y : #
l : #
n : #
g : #
>>> histoprint3((makeHistogram("A man, a plan, a canal: panama.")),2)
  : ######
m : ##
a : #########
n : ####
, : ##
p : ##
l : ##
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> copy[keys] = '#'* d[keys]
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    copy[keys] = '#'* d[keys]
NameError: name 'd' is not defined
>>> histoprint3((makeHistogram("A man, a plan, a canal: panama.")),2)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    histoprint3((makeHistogram("A man, a plan, a canal: panama.")),2)
  File "/Users/janechoi/Documents/pa09-taskC.py", line 112, in histoprint3
    if copy[keys] >= i :
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3((makeHistogram("A man, a plan, a canal: panama.")),2)
A
  : ######
m : ##
a : #########
n : ####
, : ##
p : ##
l : ##
c
:
.
>>> histoprint3((makeHistogram("A man, a plan, a canal: panama.")),2)
A
  : ######
m : ##
a : #########
n : ####
, : ##
p : ##
l : ##
c
:
.
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint3((makeHistogram(myString)),2)
N : ################
a : ################################################################################################################################################
h : ################################################################################################################################################################
  : ################################################################################################################################################################
n : ################################################################################################################################
, : ################################
e : ################################
y : ################
J : ################
u : ################
d : ################

 : ###############
>>> histoprint3((makeHistogram(myString)),10)
N : ################
a : ################################################################################################################################################
h : ################################################################################################################################################################
  : ################################################################################################################################################################
n : ################################################################################################################################
, : ################################
e : ################################
y : ################
J : ################
u : ################
d : ################

 : ###############
>>> a=makeHistogram(myString))
SyntaxError: invalid syntax
>>> a=makeHistogram(myString)
>>> type(a)
<class 'dict'>
>>> a
{'N': 16, 'a': 144, 'h': 160, ' ': 160, 'n': 128, ',': 32, 'e': 32, 'y': 16, 'J': 16, 'u': 16, 'd': 16, '\n': 15}
>>> a.max()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    a.max()
AttributeError: 'dict' object has no attribute 'max'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString))
		
KeyboardInterrupt
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString))
		)
		
16
144
160
160
128
32
32
16
16
16
16
15
160
N
a
h : ################################################################################################################################################################
  : ################################################################################################################################################################
n
,
e
y
J
u
d


>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
160
N
a
h : ################################################################################################################################################################
  : ################################################################################################################################################################
n
,
e
y
J
u
d


>>> histoprint3((makeHistogram(myString)),1)
		
N : ################
a : ################################################################################################################################################
h : ################################################################################################################################################################
  : ################################################################################################################################################################
n : ################################################################################################################################
, : ################################
e : ################################
y : ################
J : ################
u : ################
d : ################

 : ###############
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
16
144
160
160
160
160
160
160
160
160
160
160
160
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
16
144
160
160
160
160
160
160
160
160
160
160
160
80.0
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
16
144
160
160
160
160
160
160
160
160
160
160
160
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    histoprint4((makeHistogram(myString)))
  File "/Users/janechoi/Documents/pa09-taskC.py", line 139, in histoprint4
    print(histoprint3(d,num))
NameError: name 'd' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
16
144
160
160
160
160
160
160
160
160
160
160
160
N
a : ################################################################################################################################################
h : ################################################################################################################################################################
  : ################################################################################################################################################################
n : ################################################################################################################################
,
e
y
J
u
d


1
None
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
N
a : ################################################################################################################################################
h : ################################################################################################################################################################
  : ################################################################################################################################################################
n : ################################################################################################################################
,
e
y
J
u
d


1
None
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
N : ################
a : ################################################################################################################################################
h : ################################################################################################################################################################
  : ################################################################################################################################################################
n : ################################################################################################################################
, : ################################
e : ################################
y : ################
J : ################
u : ################
d : ################

 : ###############
1 : #
None
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
>>> 
KeyboardInterrupt
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
{'N': 16, 'a': 144, 'h': 160, ' ': 160, 'n': 128, ',': 32, 'e': 32, 'y': 16, 'J': 16, 'u': 16, 'd': 16, '\n': 15, '1': 1}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> h[keys]
		
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    h[keys]
NameError: name 'h' is not defined
>>> histoprint4((makeHistogram(myString)))
		
{'N': 10.0, 'a': 1.1111111111111112, 'h': 1.0, ' ': 1.0, 'n': 1.25, ',': 5.0, 'e': 5.0, 'y': 10.0, 'J': 10.0, 'u': 10.0, 'd': 10.0, '\n': 10.666666666666666, '1': 160.0}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
{'N': 0.1, 'a': 0.9, 'h': 1.0, ' ': 1.0, 'n': 0.8, ',': 0.2, 'e': 0.2, 'y': 0.1, 'J': 0.1, 'u': 0.1, 'd': 0.1, '\n': 0.09375, '1': 0.00625}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
{'N': 1.0, 'a': 9.0, 'h': 10.0, ' ': 10.0, 'n': 8.0, ',': 2.0, 'e': 2.0, 'y': 1.0, 'J': 1.0, 'u': 1.0, 'd': 1.0, '\n': 0.9375, '1': 0.0625}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    histoprint4((makeHistogram(myString)))
  File "/Users/janechoi/Documents/pa09-taskC.py", line 142, in histoprint4
    h[keys] = '#'* h[keys]
TypeError: can't multiply sequence by non-int of type 'float'
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
>>> 
KeyboardInterrupt
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
>>> 
KeyboardInterrupt
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
{'N': 1, 'a': 9, 'h': 10, ' ': 10, 'n': 8, ',': 2, 'e': 2, 'y': 1, 'J': 1, 'u': 1, 'd': 1, '\n': 0, '1': 0}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> h[keys] = '#'* h[keys]
		
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    h[keys] = '#'* h[keys]
NameError: name 'h' is not defined
>>> histoprint4((makeHistogram(myString)))
		
{'N': '#', 'a': '#########', 'h': '##########', ' ': '##########', 'n': '########', ',': '##', 'e': '##', 'y': '#', 'J': '#', 'u': '#', 'd': '#', '\n': '', '1': ''}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> 
		
>>> histoprint4((makeHistogram(myString)))
		
N#
a#########
h##########
 ##########
n########
,##
e##
y#
J#
u#
d#


1
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4((makeHistogram(myString)))
		
N#
a#########
h##########
 ##########
n########
,##
e##
y#
J#
u#
d#


1
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint1({'aocda'})
		
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    histoprint1({'aocda'})
  File "/Users/janechoi/Documents/pa09-taskC.py", line 79, in histoprint1
    copy[keys] = '#'* d[keys]
TypeError: 'set' object is not subscriptable
>>> myString
		
'Nah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\n1Nah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude\nNah nah nah nah nah nah, nah nah nah, hey Jude'
>>> strings ={'a','n','c','d'}
		
>>> string ={'K':1, 'o':3, 'k':1, 'm':1, '?':1}
		
>>> string['k']
		
1
>>> string['p']
		
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    string['p']
KeyError: 'p'
>>> string['k']=3
		
>>> string
		
{'K': 1, 'o': 3, 'k': 3, 'm': 1, '?': 1}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>>  histoprint1(makeHistogram("bicycling"))
		
SyntaxError: unexpected indent
>>> histoprint1(makeHistogram("bicycling"))
		
b : #
i : ##
c : ##
y : #
l : #
n : #
g : #
>>> makeHistogram('ankldj')
		
{'a': 1, 'n': 1, 'k': 1, 'l': 1, 'd': 1, 'j': 1}
>>> histoprint2(makeHistogram("bicycling"))
		
b : #
c : ##
g : #
i : ##
l : #
n : #
y : #
>>> histoprint4(makeHistogram(myString))
		
N#
a#########
h##########
 ##########
n########
,##
e##
y#
J#
u#
d#


1
>>> makeHistogram(myString)
		
{'N': 16, 'a': 144, 'h': 160, ' ': 160, 'n': 128, ',': 32, 'e': 32, 'y': 16, 'J': 16, 'u': 16, 'd': 16, '\n': 15, '1': 1}
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> makeHistogram(myString)
		
{'N': 16, 'a': 144, 'h': 160, ' ': 160, 'n': 128, ',': 32, 'e': 32, 'y': 16, 'J': 16, 'u': 16, 'd': 16, '\n': 15}
>>> histoprint4(makeHistogram(myString))
		
N#
a#########
h##########
 ##########
n########
,##
e##
y#
J#
u#
d#


>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> histoprint4(makeHistogram(myString))
		
N : #
a : #########
h : ##########
  : ##########
n : ########
, : ##
e : ##
y : #
J : #
u : #
d : #

 : 
>>> 
============== RESTART: /Users/janechoi/Documents/pa09-taskC.py ==============
>>> inHistogram('s', {'N': 16, 'a': 144, 'h': 160, ' ': 160, 'n': 128, ',': 32, 'e': 32, 'y': 16, 'J': 16, 'u': 16, 'd': 16, '\n': 15, '1': 1})
		
False
>>> addToHistogram('s',{'a': 16,  'b': 15 ,'c': 15, 'd': 1})
		
{'a': 16, 'b': 15, 'c': 15, 'd': 1, 's': 1}
>>> d ={'a': 16,  'b': 15 ,'c': 15, 'd': 1}
		
>>> addToHistogram('a',d)
		
{'a': 17, 'b': 15, 'c': 15, 'd': 1}
>>> makeHistogram('abcdabdc')
		
{'a': 2, 'b': 2, 'c': 2, 'd': 2}
>>> getFrequency('a',d)
		
17
>>> histoprint1(d)
		
a : #################
b : ###############
c : ###############
d : #
>>> histoprint2(d)
		
a : #################
b : ###############
c : ###############
d : #
>>> histoprint3(d,3)
		
a : #################
b : ###############
c : ###############
d
>>> histoprint(d)
		
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    histoprint(d)
NameError: name 'histoprint' is not defined
>>> hist
		
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    hist
NameError: name 'hist' is not defined
>>> histoprint4(d)
		
a : ##########
b : ########
c : ########
d : 
>>> 
