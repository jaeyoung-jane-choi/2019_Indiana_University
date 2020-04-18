Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /Users/janechoi/Documents/pa07.py =================
Please type in a word:
apple
a
p
p
l
e
I'm done!
>>> 
================= RESTART: /Users/janechoi/Documents/pa07.py =================
Please type in a word:
apple
#
p
p
l
e
I'm done!
>>> 
================= RESTART: /Users/janechoi/Documents/pa07.py =================
>>> has_vowel(apple)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    has_vowel(apple)
NameError: name 'apple' is not defined
>>> has_vowel('apple')
True
>>> has_vowel('foobar')
False
>>> 
================= RESTART: /Users/janechoi/Documents/pa07.py =================
>>> has_vowel('foobar')
True
>>> has_vowel("cwm")
False
>>> 
"a" in ("a","e","i","o","u")
True
>>> "b" in ("a","e","i","o","u")
False
>>>  "b" in "foobar"
SyntaxError: unexpected indent
>>> "b" in "foobar"
True
>>> "shear" in "misheard"
True
>>> "of" in "foobar"
False
>>> 
================= RESTART: /Users/janechoi/Documents/pa07.py =================
>>> has_vowel('foobar')
True
>>> 
================= RESTART: /Users/janechoi/Documents/pa07.py =================
foobar has a vowel!
>>> 
================= RESTART: /Users/janechoi/Documents/pa07.py =================

>>> has_positive((-4,-2,1,-7))
True
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    analyze_tuple_1(a)
NameError: name 'a' is not defined
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1('a')
-1
>>> analyze_tuple_1(-1)
-1
>>> analyze_tuple_1(('a',1,'b'))
3
>>> a=analyze_tuple_1(('a',1,'b'))
>>> a
3
>>> type(a)
<class 'int'>
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> nalyze_tuple_1(('a',1,'b'))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    nalyze_tuple_1(('a',1,'b'))
NameError: name 'nalyze_tuple_1' is not defined
>>> analyze_tuple_1(('a',1,'b'))
(((3, 'str'), 'int'), 'str')
>>> nalyze_tuple_1('a')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    nalyze_tuple_1('a')
NameError: name 'nalyze_tuple_1' is not defined
>>> analyze_tuple_1(1)
(-1, None)
>>> a=analyze_tuple_1(1)
>>> type(a)
<class 'tuple'>
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
(False, False)
(False, False)
(False, False)
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
False
False
False
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
False
False
False
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    analyze_tuple_1(('a',1,'b'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 18, in analyze_tuple_1
    element= element + new
TypeError: can only concatenate str (not "bool") to str
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
False
False
False
bFalse
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
a
1
b
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
False
True
False
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    analyze_tuple_1(('a',1,'b'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 17, in analyze_tuple_1
    count += new
UnboundLocalError: local variable 'count' referenced before assignment
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
0
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
0
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
(False, False)
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
False
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
False
True
False
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
False
(False, False)
True
(True, True)
False
(False, False)
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
False
True
False
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> isinstance(myTuple ,tuple)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    isinstance(myTuple ,tuple)
NameError: name 'myTuple' is not defined
>>> analyze_tuple_1(('a',1,'b'))
False
True
False
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
False
True
False
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
0
2
0
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
True
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
True
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> isinstance(elements ,int):
	
SyntaxError: invalid syntax
>>> analyze_tuple_1(('a',1,'b'))
str
int
str
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
(False, False)
(True, True)
(False, False)
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
(False, False)
(True, True)
(False, False)
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
False
FalseTrue
FalseTrueFalse
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
FalseTrueFalse
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    analyze_tuple_1(('a',1,'b'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 19, in analyze_tuple_1
    output = output + (what)
TypeError: can only concatenate str (not "bool") to str
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('a',1,'b'))
mixed
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    analyze_tuple_1(('a',1,'b'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 41, in analyze_tuple_1
    return result
NameError: name 'result' is not defined
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> third = max(myTuple)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    third = max(myTuple)
NameError: name 'myTuple' is not defined
>>> analyze_tuple_1(('a',1,'b'))
(3, 'mixed', None)
>>> analyze_tuple_1(('a','1','b'))
(3, 'str', None)
>>> analyze_tuple_1((2,1,3))
(3, 'mixed', None)
>>> analyze_tuple_1((2,1,3))
(3, 'mixed', None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,1,3))
(3, 'int', None)
>>> analyze_tuple_1((2,1,3))
(3, 'int', None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,1,3))
(3, 'int', None)
>>> max((2,1,3))
3
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,1,3))
3
(3, 'int', None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,1,3))
3
(3, 'int', 3)
>>> analyze_tuple_1(1)
(-1, None, None)
>>> analyze_tuple_1((2,'1',3))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    analyze_tuple_1((2,'1',3))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 40, in analyze_tuple_1
    result = (first,second,third)
UnboundLocalError: local variable 'third' referenced before assignment
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,'1',3))
(3, 'mixed', None)
>>> analyze_tuple_1((2,1,3))
(3, 'int', 3)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,'1',3))
True
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    analyze_tuple_1((2,'1',3))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 33, in analyze_tuple_1
    result = (first,second,third)
NameError: name 'second' is not defined
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,'1',3))
True
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    analyze_tuple_1((2,'1',3))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 39, in analyze_tuple_1
    return result
NameError: name 'result' is not defined
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,'1',3))
True
'True'
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,'1',3))
True
1
'True'
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,'1',3))
True
1
'True'
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,'1',3))
TrueFalseTrue
3
'TrueFalseTrue'
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((2,'1',3))
(3, 'mixed', None)
>>> analyze_tuple_1((2,1,3))
(3, 'int', 3)
>>> analyze_tuple_1(('2','1','3'))
(3, 'str', None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('2aa','1','3'))
3
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    analyze_tuple_1(('2aa','1','3'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 52, in analyze_tuple_1
    result = (first,second,third)
UnboundLocalError: local variable 'third' referenced before assignment
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('2','1','3'))
1
(3, 'str', None)
>>> analyze_tuple_1(('21','1','3'))
2
(3, 'str', None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
(3, 1, 1)
(3, 'str', None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> len(myTuple[0]) > len(myTuple[1]) > len(myTuple[2])
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    len(myTuple[0]) > len(myTuple[1]) > len(myTuple[2])
NameError: name 'myTuple' is not defined
>>> analyze_tuple_1(('abd','1','3'))
(3, 'str', '1')
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
(3, 'str', 'abd')
>>> analyze_tuple_1(('abd','1as','31212'))
(3, 'str', '31212')
>>> analyze_tuple_1(('abd','dd1','dd3'))
(3, 'str', 'abd')
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1'))
(2, 'mixed', None)
>>> analyze_tuple_1(('abd','1','3'))

(3, 1, 1)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    analyze_tuple_1(('abd','1','3'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 50, in analyze_tuple_1
    result = (first,second,third)
UnboundLocalError: local variable 'third' referenced before assignment
>>> isinstance(('a','b','c'),str)
False
>>> isinstance(('a','b','c')[1],str)
True
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> isinstance(('a','b','c'),str)
False
>>> analyze_tuple_1(('abd','1','3'))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    analyze_tuple_1(('abd','1','3'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 22, in analyze_tuple_1
    integer = integer+ isint
TypeError: can only concatenate str (not "bool") to str
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
FalseFalseFalse
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    analyze_tuple_1(('abd','1','3'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 25, in analyze_tuple_1
    print(integer)
KeyboardInterrupt
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> 
>>> analyze_tuple_1(('abd','1','3'))
FalseFalseFalse
(-1, None, None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
None
FalseFalseFalse
(-1, None, None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
None
FalseFalseFalse
(-1, None, None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
None
(-1, None, None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
FalseFalseFalse
None
(-1, None, None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
FalseFalseFalse
(-1, None, None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========

>>> analyze_tuple_1(('abd','1','3'))
FalseFalseFalse
(3, 'none', '')
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
FalseFalseFalse
(3, None, '')
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
>>> 
>>> analyze_tuple_1(('abd','1','3'))
FalseFalseFalse
(3, None, '')
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
FalseFalseFalse
<class 'str'>
(3, None, '')
>>> a = FalseFalseFalse
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a = FalseFalseFalse
NameError: name 'FalseFalseFalse' is not defined
>>> a = 'FalseFalseFalse'
>>> a in 'False'
False
>>> a in 'F;
SyntaxError: EOL while scanning string literal
>>> a in 'F'
False
>>> a in ('F','a')
False
>>> 'a' in 'F'
False
>>> "of" in "foobar"
False
>>> "shear" in "misheard"
True
>>> 'FalseFalseFalse' in 'False'
False
>>> 'FalseFalseFalse' is 'F'
False
>>> 'F' in 'FalseFalseFalse'
True
>>> 'False' in 'FalseFalseFalse'
True
>>> 'False' in 'TrueFalse'
True
>>> 'True' in 'FalseFalseTrueFalse'
True
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
FalseFalseFalse
(3, 'mixed', None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
FalseFalseFalse
(3, 'string', 'abd')
>>> analyze_tuple_1((1,2,3))
TrueTrueTrue
(3, 'integer', None)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((1,2,3))
(3, 'integer', 3)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1((1,2,3,12,22,32.2))
(6, 'mixed', None)
>>> analyze_tuple_1((1,2,3,1,121212121,343243,))
(6, 'integer', 121212121)
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    analyze_tuple_1(('abd','1','3'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 47, in analyze_tuple_1
    while newcounter < len(myTuple):
KeyboardInterrupt
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    analyze_tuple_1(('abd','1','3'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 49, in analyze_tuple_1
    if len(myTuple[newcounter]) > maxvalue :
KeyboardInterrupt
>>> analyze_tuple_1(('abd','1','3'))
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    analyze_tuple_1(('abd','1','3'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 47, in analyze_tuple_1
KeyboardInterrupt
>>> analyze_tuple_1(('abd','1','3'))
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    analyze_tuple_1(('abd','1','3'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 47, in analyze_tuple_1
KeyboardInterrupt
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> analyze_tuple_1(('abd','1','3'))
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    analyze_tuple_1(('abd','1','3'))
  File "/Users/janechoi/Documents/pa07-analyze_tuple_1.py", line 50, in analyze_tuple_1
    if len(myTuple[newcounter]) > maxvalue :
TypeError: '>' not supported between instances of 'int' and 'str'
>>> 
========= RESTART: /Users/janechoi/Documents/pa07-analyze_tuple_1.py =========
>>> 
>>> myTuple[newcounter]
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    myTuple[newcounter]
NameError: name 'myTuple' is not defined
>>> analyze_tuple_1(('abd','1','3'))
(3, 'string', 'abd')
>>> analyze_tuple_1(('abd','112','31'))
(3, 'string', 'abd')
>>> analyze_tuple_1(('abd','1121121','3'))
(3, 'string', '1121121')
>>> analyze_tuple_1(('abd','1','3','aaaaaa','bbbbbbbb'))
(5, 'string', 'bbbbbbbb')
>>> analyze_tuple_1('1234')
(-1, None, None)
>>> analyze_tuple_1(("jo", 3, "jack"))
(3, 'mixed', None)
>>> analyze_tuple_1(("jill", "jo", "jackie"))
(3, 'string', 'jackie')
>>> analyze_tuple_1((3, 4, 13094, -381734987139487194719471984 ))
(4, 'integer', 13094)
>>> 
============ RESTART: /Users/janechoi/Documents/pa07-functions.py ============
>>> contains_letter_2("ABC")
True
>>> contains_letter_2("65,537")
False
>>> contains_letter_2("$%#@!")
False
>>> contains_letter_2("π^2/6")
True
>>> 
============ RESTART: /Users/janechoi/Documents/pa07-functions.py ============
>>> contains_only_integers_2( (8, 4, "2", 1) )
False
>>> contains_only_integers_2( (2.0,4.0) )
False
>>> contains_only_integers_2( () )
True
>>> contains_only_integers_2( (-1,) )
True
>>> 
