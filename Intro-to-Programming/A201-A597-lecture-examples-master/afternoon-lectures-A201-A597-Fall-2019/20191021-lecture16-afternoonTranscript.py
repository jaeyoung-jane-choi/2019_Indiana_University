Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
>>> hiScores
[['Alex', 20000], ['Bert', 9999], ['Cat', 200]]
>>> hiScores[0]
['Alex', 20000]
>>> hiScores[:1]
[['Alex', 20000]]
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
['Alex', 20000]
['Bert', 9999]
['Cat', 200]
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex
20000
Bert
9999
Cat
200
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex20000Bert9999Cat200
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex20000
Bert9999
Cat200
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	Traceback (most recent call last):
  File "/Users/Shared/Desktop/afternoon01.py", line 21, in <module>
    print(element+"\t", end="")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex20000
Bert9999
Cat200
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat	200	
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
>>> hiScores[2]
['Cat', 200]
>>> hiScores[2][1]
200
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
>>> hiScores2
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    hiScores2
NameError: name 'hiScores2' is not defined
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 200]]
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
['Alex', 'Anderson']	20000	
['Bert', 'Brianson']	9999	
['Cat', 'Caterson']	200	
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
Alex	Anderson	Traceback (most recent call last):
  File "/Users/Shared/Desktop/afternoon01.py", line 45, in <module>
    for word in element:
TypeError: 'int' object is not iterable
>>> help(isinstance)
Help on built-in function isinstance in module builtins:

isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.
    
    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.

>>> type(element)
<class 'int'>
>>> type(element) == int
True
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
Alex	Anderson	20000
Bert	Brianson	9999
Cat	Caterson	200
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
 version 2 of nested nested lists 
Alex	Anderson	20000
Bert	Brianson	9999
Cat	Caterson	200
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
 version 2 of nested nested lists 
Alex	Anderson	20000
Bert	Brianson	9999
Cat	Caterson	2000
>>> first = hiScores2[1][0][0]
>>> first
'Bert'
>>> last = hiScores2[1][0][1]
>>> last
'Brianson'
>>> first, last = hiScores2[1][0]
>>> first
'Bert'
>>> last
'Brianson'
>>> first, last = hiScores2[2][0]
>>> first
'Cat'
>>> last
'Caterson'
>>> (first, last) = hiScores2[2][0]
>>> first
'Cat'
>>> last
'Caterson'
>>> hiScores2[2].append(1000)
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000, 1000]]
>>> hiScores2[2].remove(1000)
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000]]
>>> hiScores2[2].append(1000)
>>> del hiScores2[2]
>>> hiScores2[2]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    hiScores2[2]
IndexError: list index out of range
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999]]
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
Alex	20000	
Bert	9999	
Cat has at the moment: 200
Cat	200	
 version 2 of nested nested lists 
Alex	Anderson	20000
Bert	Brianson	9999
Cat	Caterson	2000
>>> hiScores2[2].append(1000)
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000, 1000]]
>>> del hiScores2[2][2]
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000]]
>>> a = 10
>>> b = 1
>>> b = a
>>> c = a
>>> a
10
>>> b
10
>>> c
10
>>> a = -10
>>> b
10
>>> c
10
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000]]
>>> s = hiScores2
>>> s
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000]]
>>> hiScores2.append(1000)
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000], 1000]
>>> s
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000], 1000]
>>> s
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000], 1000]
>>> s
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000], 1000]
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000], 1000]
>>> third = hiScores2[:]
>>> third
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000], 1000]
>>> del third[3]
>>> third
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000]]
>>> s
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000], 1000]
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000], 1000]
>>> del s[3]
>>> hiScores2
[[['Alex', 'Anderson'], 20000], [['Bert', 'Brianson'], 9999], [['Cat', 'Caterson'], 2000]]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> dict1 = { 0: "Alex", 1: "Bert", 2: "Cat", 3 : "Dirk" }
>>> dict1[0]
'Alex'
>>> dict1[1]
'Bert'
>>> dict1[2]
'Cat'
>>> dict2[3]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    dict2[3]
NameError: name 'dict2' is not defined
>>> dict1[3]
'Dirk'
>>> dict2 = { "Killer Frost" : "Alex", "Quake" : "Bert", "Dog" : "Cat", "Gently" : "Dirk" }
>>> dict2["Alex"]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    dict2["Alex"]
KeyError: 'Alex'
>>> dict2["Killer Frost"]
'Alex'
>>> dict2 = { True: "today it rains", False: "today it's sunny" }
>>> dict2[True]
'today it rains'
>>> dict2[False]
"today it's sunny"
>>> dict4 = dict()
>>> dict4["Mommy"] = 45
>>> dict4
{'Mommy': 45}
>>> 
