Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> middle([1,2,3,4,5])
[2, 3, 4, 5]
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> middle([1,2,3,4,5])
[2, 3, 4, 5]
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> middle([1,2,3,4,5])
[2, 3]
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> middle([1,2,3,4,5])
[2, 3, 4]
>>> middle([1,2,3,4,5,1,2,3,4,5])
[2, 3, 4, 5, 1, 2, 3, 4]
>>> a=middle([1,2,3,4,5])
>>> a
[2, 3, 4]
>>> type(a)
<class 'list'>
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> chop([1,2,3,4,5])
[2, 3, 4]
>>> chop([1,2,3,4,1,1,2,3,,5])
SyntaxError: invalid syntax
>>> chop([1,2,3,4,2,5,2,1,1,1,1,5])
[2, 3, 4, 2, 5, 2, 1, 1, 1, 1]
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> chop([1,2,3,4,5])
[2, 3, 4]
>>> l
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> chop([1,2,3,4,5])
[2, 3, 4]
>>> 
============= RESTART: /Users/janechoi/Documents/pa08-basket1.py =============
Add as many items to the basket as you want. When you're done, enter 'nothing'.
What do you want to put into the basket now?a sandwich
Okay.
What do you want to put into the basket now?some napkins
Okay.
What do you want to put into the basket now?nothing
Okay.
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa08-basket1.py", line 24, in <module>
    print(' There are '+ str(len(basket)) + ' items in the basket: ' +basket )
TypeError: can only concatenate str (not "list") to str
>>> 
============= RESTART: /Users/janechoi/Documents/pa08-basket1.py =============
Add as many items to the basket as you want. When you're done, enter 'nothing'.
What do you want to put into the basket now?a sandwich
Okay.
What do you want to put into the basket now?some napkins
Okay.
What do you want to put into the basket now?nothing
Okay.
 There are 3 items in the basket: ['a sandwich', 'some napkins', 'nothing']
>>> 
============= RESTART: /Users/janechoi/Documents/pa08-basket1.py =============
Add as many items to the basket as you want. When you're done, enter 'nothing'.
What do you want to put into the basket now?a sandwich
Okay.
What do you want to put into the basket now?some napkins
Okay.
What do you want to put into the basket now?two bottles of K
Okay.
What do you want to put into the basket now?nothing
Okay.
There are 4 items in the basket: ['a sandwich', 'some napkins', 'two bottles of K', 'nothing']
>>> 
============= RESTART: /Users/janechoi/Documents/pa08-basket1.py =============
Add as many items to the basket as you want. When you're done, enter 'nothing'.
What do you want to put into the basket now?a sandwich
Okay.
What do you want to put into the basket now?some napkins
Okay.
What do you want to put into the basket now?nothing
Okay.
There are 2 items in the basket: ['a sandwich', 'some napkins']
>>> 
============= RESTART: /Users/janechoi/Documents/pa08-basket2.py =============
Add as many items to the basket as you want. When you're done, enter 'nothing'.
What do you want to put into the basket now?a sandwich
Okay.
What do you want to put into the basket now?some napkins
Okay.
What do you want to put into the basket now?nothing
Okay.
There are 2 items in the basket: ['a sandwich', 'some napkins']
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa08-basket2.py", line 41, in <module>
    print('Item'+ index + ':' + basket[index])
TypeError: can only concatenate str (not "int") to str
>>> 
============= RESTART: /Users/janechoi/Documents/pa08-basket2.py =============
Add as many items to the basket as you want. When you're done, enter 'nothing'.
What do you want to put into the basket now?a sandwich
Okay.
What do you want to put into the basket now?some napkins
Okay.
What do you want to put into the basket now?nothing
Okay.
There are 2 items in the basket: ['a sandwich', 'some napkins']
Item0:a sandwich
Item1:some napkins
>>> 
============= RESTART: /Users/janechoi/Documents/pa08-basket2.py =============
Add as many items to the basket as you want. When you're done, enter 'nothing'.
What do you want to put into the basket now?a sandwich
Okay.
What do you want to put into the basket now?some napkins
Okay.
What do you want to put into the basket now?two bottles of lemonade
Okay.
What do you want to put into the basket now?nothing
Okay.
There are 3 items in the basket: ['a sandwich', 'some napkins', 'two bottles of lemonade']
Item1:a sandwich
Item2:some napkins
Item3:two bottles of lemonade
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> x = get_user_input(["yes","no","maybe"]
yes
		       
SyntaxError: invalid syntax
>>> x = get_user_input(["yes","no","maybe"])
		       
Please select one of the following:
yes
no
maybe
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> x = get_user_input(["yes","no","maybe"]
		       )
		       
Please select one of the following:
yes
no
maybe
no
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> 
		       
>>> x = get_user_input(["yes","no","maybe"])
		       
Please select one of the following:
yes
no
maybe

>>> no
		       
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    no
NameError: name 'no' is not defined
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
		       
>>> 
>>> x = get_user_input(["yes","no","maybe"])
		       
Please select one of the following:
yes
no
maybe
You select...no
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> x = get_user_input(["yes","no","maybe"])
		       
Please select one of the following:
yes
no
maybe
You select...o
o
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> x = get_user_input(["yes","no","maybe"])
		       
Please select one of the following:
yes
no
maybe
You select...k
That wasn't a valid option. Please make a different choice.
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> x = get_user_input(["yes","no","maybe"])
		       
Please select one of the following:
yes
no
maybe
You select...k
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
That wasn't a valid option. Please make a different choice.
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x = get_user_input(["yes","no","maybe"])
  File "/Users/janechoi/Documents/pa08-functions.py", line 60, in get_user_input
    print("That wasn't a valid option. Please make a different choice.")
KeyboardInterrupt
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> user_input = input('You select...')
		       
You select...no
>>> x = get_user_input(["yes","no","maybe"])
		       
Please select one of the following:
yes
no
maybe
That wasn't a valid option. Please make a different choice.
You select...
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============

============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> x = get_user_input(["yes","no","maybe"])
		       
Please select one of the following:
yes
no
maybe
You select...l
That wasn't a valid option. Please make a different choice.
You select...l
That wasn't a valid option. Please make a different choice.
You select...d
That wasn't a valid option. Please make a different choice.
You select...no
That wasn't a valid option. Please make a different choice.
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> x = get_user_input(["yes","no","maybe"])
		       
Please select one of the following:
yes
no
maybe
You select...k
That wasn't a valid option. Please make a different choice.
You select...s
That wasn't a valid option. Please make a different choice.
You select...ql
That wasn't a valid option. Please make a different choice.
You select...no
>>> print(x)
		       
no
>>> print(x)
		       
no
>>> type(x)
		       
<class 'str'>
>>> y = get_user_input(["1","2","3","4","5"])
		       
Please select one of the following:
1
2
3
4
5
You select...4
>>> print(x)
		       
no
>>> print(y)
		       
4
>>> x
		       
'no'
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> y = get_user_input(["1","2","3","4","5"])
		       
Please select one of the following:
1
2
3
4
5
You select...1
>>> y
		       
'1'
>>> type(y)
		       
<class 'str'>
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> y = get_user_input(["1","2","3","4","5"])
		       
Please select one of the following:
1
2
3
4
5
0
That wasn't a valid option. Please make a different choice.
You select...1
>>> y
		       
'1'
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> y = get_user_input(["1","2","3","4","5"])
		       
Please select one of the following:
1
2
3
4
5
1
>>> y
		       
'1'
>>> y = get_user_input(["1","2","3","4","5"])
		       
Please select one of the following:
1
2
3
4
5
2
>>> y = get_user_input(["1","2","3","4","5"])
		       
Please select one of the following:
1
2
3
4
5
0
That wasn't a valid option. Please make a different choice.
0
That wasn't a valid option. Please make a different choice.
0
That wasn't a valid option. Please make a different choice.
0
That wasn't a valid option. Please make a different choice.
2
>>> y = get_user_input(["1","2","3","4","5"])
		       
Please select one of the following:
1
2
3
4
5
0
That wasn't a valid option. Please make a different choice.
0
That wasn't a valid option. Please make a different choice.
9
That wasn't a valid option. Please make a different choice.
1
>>> y
		       
'1'
>>> type(y)
		       
<class 'str'>
>>> 
============ RESTART: /Users/janechoi/Documents/pa08-functions.py ============
>>> y = get_user_input(["1","2","3","4","5"])
		       
Please select one of the following:
1
2
3
4
5
2
>>> y
		       
'2'
>>> x = get_user_input(["yes","no","maybe"])
		       
Please select one of the following:
yes
no
maybe
d
That wasn't a valid option. Please make a different choice.
d
That wasn't a valid option. Please make a different choice.
no
>>> x
		       
'no'
>>> print(x)
		       
no
>>> listX = ['S', 'h', 'a', 'r', 'e', 'd']
listY = listX
listZ = ['S', 'h', 'a', 'r', 'e', 'd']
listX.append('!')
del listY[2]
listZ.remove('d')

SyntaxError: multiple statements found while compiling a single statement
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> listX
		       
['S', 'h', 'r', 'e', 'd', '!']
>>> listZ
		       
['S', 'h', 'a', 'r', 'e']
>>> listY
		       
['S', 'h', 'r', 'e', 'd', '!']
>>> 
================= RESTART: /Users/janechoi/Documents/new.py =================
>>> listX
		       
[2, 0, 1, 8, 10, 18]
>>> listY
		       
['S', 'h', 'r', 'e', 'd', '!']
>>> id(listX)
		       
4469789576
>>> id(listY)
		       
4435834888
>>> listX[4:] = [0,0]
		       
>>> listX
		       
[2, 0, 1, 8, 0, 0]
>>> listY.clear()
		       
>>> listY
		       
[]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-sharedReferences.py ========
>>> dList
		       
['h', 'a', 'r']
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> isInRecord(o,[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    isInRecord(o,[['K',1],['o',3],['k',1],['m',1],['?',1]])
NameError: name 'o' is not defined
>>> isInRecord('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
False
>>> a= [['K',1],['o',3],['k',1],['m',1],['?',1]]
		       
>>> a[0][0]
		       
'K'
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> isInRecord(o,[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    isInRecord(o,[['K',1],['o',3],['k',1],['m',1],['?',1]])
NameError: name 'o' is not defined
>>> isInRecord('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
False
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> isInRecord('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
False
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> l[index][0]
		       
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    l[index][0]
NameError: name 'l' is not defined
>>> isInRecord('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
True
>>> isInRecord('r',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
False
>>> isInRecord('l',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
False
>>> isInRecord('K',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
True
>>> isInRecord('m',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
True
>>> isInRecord('?',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
True
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> myCharRecord = [['K',1],['o',3],['k',1],['m',1],['?',1]]
		       
>>> addToRecord('o',myCharRecord)
		       
4
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('o',myCharRecord)
		       
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    addToRecord('o',myCharRecord)
NameError: name 'myCharRecord' is not defined
>>> myCharRecord = [['K',1],['o',3],['k',1],['m',1],['?',1]]
		       
>>> addToRecord('o',myCharRecord)
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('o',myCharRecord)
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
>>> newlist
		       
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    newlist
NameError: name 'newlist' is not defined
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========

>>> addToRecord('o',myCharRecord)
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('o',myCharRecord)
		       
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    addToRecord('o',myCharRecord)
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 51, in addToRecord
    print(newlist)
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('o',myCharRecord)
		       
5
[['K', 1], ['o', 4], ['k', 1], ['m', 1], ['?', 1]]
[['K', 1], ['o', 4], ['k', 1], ['m', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('o',myCharRecord)
		       
[['K', 1], ['o', 4], ['k', 1], ['m', 1], ['?', 1]]
>>> addToRecord('r',myCharRecord)
		       
[['K', 1], ['o', 4], ['k', 1], ['m', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('r',myCharRecord)
		       
>>> 
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('r',myCharRecord)
		       
>>> 
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('r',myCharRecord)
		       
>>> 
		       
>>> 
KeyboardInterrupt
>>> myCharRecord = [['K',1],['o',3],['k',1],['m',1],['?',1]]

>>> myCharRecord
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
>>> myCharRecord.append(['r',1])
		       
>>> myCharRecord
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1], ['r', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>>  addToRecord('r',myCharRecord)
		       
SyntaxError: unexpected indent
>>> addToRecord('r',myCharRecord)
		       
>>>  addToRecord('r',myCharRecord)
		       
SyntaxError: unexpected indent
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>>  addToRecord('r',myCharRecord)
		       
SyntaxError: unexpected indent
>>> addToRecord('r',myCharRecord)
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> newlist.append([s,1])
		       
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    newlist.append([s,1])
NameError: name 'newlist' is not defined
>>> addToRecord('r',myCharRecord)
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1], ['r', 1]]
>>> addToRecord('o',myCharRecord)
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1], ['o', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('r',myCharRecord)
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1], ['r', 1]]
>>> addToRecord('o',myCharRecord)
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1], ['o', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('r',myCharRecord)
		       
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1], ['r', 1]]
>>> addToRecord('k',myCharRecord)
		       
[['K', 1], ['o', 3], ['k', 2], ['m', 1], ['?', 1]]
>>> addToRecord('o',myCharRecord)
		       
[['K', 1], ['o', 4], ['k', 2], ['m', 1], ['?', 1]]
>>> addToRecord('?',myCharRecord)
		       
[['K', 1], ['o', 4], ['k', 2], ['m', 1], ['?', 2]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> 
		       
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 73, in createRecord
    if s[index] in l[index][0]:
NameError: name 'l' is not defined
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>>  createRecord('Kokomo?')
		       
SyntaxError: unexpected indent
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 73, in createRecord
    if s[index] in recordlist[index][0]:
IndexError: list index out of range
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 73, in createRecord
    if s[index] in recordlist[index][0]:
IndexError: list index out of range
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 73, in createRecord
    if s[index] in recordlist[index][0]:
IndexError: list index out of range
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 73, in createRecord
    if s[index] in recordlist[index][0]:
IndexError: list index out of range
>>> rec = []
		       
>>> rec = [][]
		       
SyntaxError: invalid syntax
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 73, in createRecord
    if s[index] in recordlist[index][0]:
IndexError: list index out of range
>>> rec = [[]]
		       
>>> rec
		       
[[]]
>>> type(rec)
		       
<class 'list'>
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 2]]
[['K', 3]]
[['K', 4]]
[['K', 5]]
[['K', 6]]
[['K', 7]]
[['K', 8]]
[['K', 9]]
[['K', 10]]
[['K', 11]]
[['K', 12]]
[['K', 13]]
[['K', 14]]
[['K', 15]]
[['K', 16]]
[['K', 17]]
[['K', 18]]
[['K', 19]]
[['K', 20]]
[['K', 21]]
[['K', 22]]
[['K', 23]]
[['K', 24]]
[['K', 25]]
[['K', 26]]
[['K', 27]]
[['K', 28]]
[['K', 29]]
[['K', 30]]
[['K', 31]]ƒ
ç[['K', 32]]
[['K', 33]]
[['K', 34]]
[['K', 35]]
[['K', 36]]
[['K', 37]]
[['K', 38]]
[['K', 39]]
[['K', 40]]
ç[['K', 41]]
[['K', 42]]
[['K', 43]]
[['K', 44]]ç
[['K', 45]]
[['K', 46]]
[['K', 47]]
[['K', 48]]
[['K', 49]]
[['K', 50]]
[['K', 51]]
[['K', 52]]
[['K', 53]]
[['K', 54]]
[['K', 55]]
[['K', 56]]
[['K', 57]]
[['K', 58]]
[['K', 59]]
[['K', 60]]
[['K', 61]]
[['K', 62]]
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 76, in createRecord
    print(recordlist)
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 72, in createRecord
    while index < len(s):
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 74, in createRecord
    if s[index] in recordlist[index][0]:
IndexError: list index out of range
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1]]
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 76, in createRecord
    if s[index] in recordlist[index][0]:
IndexError: list index out of range
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 79, in createRecord
    if s[index] in recordlist[newindex][0]:
TypeError: list indices must be integers or slices, not list
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 77, in createRecord
    for newindex in range(recordlist):
TypeError: 'list' object cannot be interpreted as an integer
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 77, in createRecord
    for newindex in len(recordlist):
TypeError: 'int' object is not iterable
>>> recordlist = [[1],[2]]
		       
>>> len(recordlist)
		       
2
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 79, in createRecord
    if s[index] in recordlist[newindex][0]:
IndexError: list index out of range
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========

>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1], ['k', 1], ['k', 2], ['o', 1], ['o', 2], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
0
0
1
0
1
2
3
0
1
2
3
4
5
6
0
1
2
3
4
5
6
7
8
9
10
11
12
13
0
1
2
3
4
5
6
7
8
9
10
11
12
13
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 78, in createRecord
    print(newindex)
KeyboardInterrupt
>>> recordlist = [['o',3],['k',1],['m',1],['?',1]]
		       
>>> range(len(recordlist))
		       
range(0, 4)
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 78, in createRecord
    for newindex in range(len(recordlist)):
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 76, in createRecord
    while s[index] not in recordlist:
IndexError: string index out of range
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> 
		       
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 78, in createRecord
    if s[index] in recordlist[newindex][0]:
IndexError: string index out of range
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1]]
[['K', 1], ['o', 1], ['k', 1], ['k', 1]]
[['K', 1], ['o', 1], ['k', 1], ['k', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 87, in createRecord
    print(recordlist)
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1]]
[['K', 1], ['o', 1], ['k', 1], ['k', 1]]
[['K', 1], ['o', 1], ['k', 1], ['k', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1]]ç
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 88, in createRecord
    print(recordlist)
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> recordlist.append([s[index],1])
		       
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    recordlist.append([s[index],1])
NameError: name 'recordlist' is not defined
>>> createRecord('Kokomo?')
		       
[['K', 1]]
[['K', 1]]
[['K', 1]]
[['K', 1]]
[['K', 1]]
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
1
2
2
3
3
4
4
5
5
6
6
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
1
1
1
1
1
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> newindex
		       
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    newindex
NameError: name 'newindex' is not defined
>>> createRecord('Kokomo?')
		       
1
1
1
1
1
1
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
1
1
1
1
1
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
1
1
1
1
1
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
1
1
1
1
1
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
1
1
1
1
1
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
1
1
1
1
1
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
2
1
3
1
4
1
5
1
6
1
7
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
2
[['K', 1]]
1
3
[['K', 1]]
1
4
[['K', 1]]
1
5
[['K', 1]]
1
6
[['K', 1]]
1
7
[['K', 1]]
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
2
[['K', 1], ['o', 1]]
2
3
[['K', 1], ['o', 1], ['k', 1]]
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 82, in createRecord
    recordlist[newindex][1] = recordlist[newindex][1]  + 1
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
0
1
2
[['K', 1], ['o', 1]]
0
1
2
3
[['K', 1], ['o', 1], ['k', 1]]
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 79, in createRecord
    print(newindex)
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
0
1
2
[['K', 1], ['o', 1]]
0
1
2
3
[['K', 1], ['o', 1], ['k', 1]]
0
1
2
3
4
[['K', 1], ['o', 2], ['k', 1], ['o', 1]]
0
1
2
3
4
5
[['K', 1], ['o', 2], ['k', 1], ['o', 1], ['m', 1]]
0
1
2
3
4
5
6
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1]]
0
1
2
3
4
5
6
7
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
0
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
10
10
11
11
12
12
13
13
14
14
15
15
16
16
17
17
18
18
19
19
20
20
21
21
22
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 88, in createRecord
    print(newindex)
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
0
1
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26ç
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 79, in createRecord
    print(newindex)
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 90, in createRecord
    recordlist.append([s[index],1])
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
0
1
2
[['K', 1]]
0
1
3
[['K', 1]]
0
1
4
[['K', 1]]
0
1
5
[['K', 1]]
0
1
6
[['K', 1]]
0
1
7
[['K', 1]]
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> print(newindex)
		       
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    print(newindex)
NameError: name 'newindex' is not defined
>>> createRecord('Kokomo?')
		       
0
1
2
[['K', 1]]
0
1
3
[['K', 1]]
0
1
4
[['K', 1]]
0
1
5
[['K', 1]]
0
1
6
[['K', 1]]
0
1
7
[['K', 1]]
[['K', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
0
1
1
2
2
[['K', 1], ['o', 2]]
0
1
1
2
2
3
3
4
3
[['K', 1], ['o', 2], ['k', 2], ['k', 2]]
0
1
1
2
2
3
3
4
4
5
5
6
6
7
4
[['K', 1], ['o', 3], ['k', 2], ['k', 2], ['o', 2], ['o', 2], ['o', 2]]
0
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
10
10
11
11
12
12
13
13
14
5
[['K', 1], ['o', 3], ['k', 2], ['k', 2], ['o', 2], ['o', 2], ['o', 2], ['m', 2], ['m', 2], ['m', 2], ['m', 2], ['m', 2], ['m', 2], ['m', 2]]
0
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
10
10
11
11
12
12
13
13
14
14
15
15
16
16
17
17
18
18
19
19
20
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 93, in createRecord
    print(newindex)
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> addToRecord('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
[['K', 1], ['o', 4], ['k', 1], ['m', 1], ['?', 1]]
>>> createRecord('string')
		       
[['s', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('string')
		       
[['s', 1], ['t', 1], ['r', 1], ['r', 1], ['i', 1], ['i', 1], ['i', 1], ['i', 1], ['n', 1], ['n', 1], ['n', 1], ['n', 1], ['n', 1], ['n', 1], ['n', 1], ['n', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1], ['g', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('string')
		       
[['s', 1], ['t', 1], ['r', 1], ['i', 1], ['n', 1], ['g', 1]]
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
2
3
4
5
6
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
[['K', 1], ['o', 1]]
2
[['K', 1], ['o', 1], ['k', 1]]
3
[['K', 1], ['o', 1], ['k', 1], ['o', 1]]
4
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1]]
5
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1]]
6
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
[['K', 1], ['o', 1]]
2
[['K', 1], ['o', 1], ['k', 1]]
3
[['K', 1], ['o', 2], ['k', 1], ['o', 1]]
4
[['K', 1], ['o', 2], ['k', 1], ['o', 1], ['m', 1]]
5
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1]]
6
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> s[index] in recordlist[newindex]
		       
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    s[index] in recordlist[newindex]
NameError: name 's' is not defined
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 89, in createRecord
    if s[index]  not in recordlist[newindex]:
IndexError: list index out of range
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1]]
[['K', 1], ['o', 2], ['k', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['o', 1], ['m', 1]]
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1]]
[['K', 1], ['o', 2], ['k', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['o', 1], ['m', 1]]
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> addToRecords('s', [['K',1],['o',4],['k',1],['m',1],['?',1],['X',1]])
		       
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    addToRecords('s', [['K',1],['o',4],['k',1],['m',1],['?',1],['X',1]])
NameError: name 'addToRecords' is not defined
>>> addToRecord('s', [['K',1],['o',4],['k',1],['m',1],['?',1],['X',1]])
		       
[['K', 1], ['o', 4], ['k', 1], ['m', 1], ['?', 1], ['X', 1], ['s', 1]]
>>> addToRecord('p', [['K',1],['o',4],['k',1],['m',1],['?',1],['X',1]])
		       
[['K', 1], ['o', 4], ['k', 1], ['m', 1], ['?', 1], ['X', 1], ['p', 1]]
>>> addToRecord('K', [['K',1],['o',4],['k',1],['m',1],['?',1],['X',1]])
		       
[['K', 2], ['o', 4], ['k', 1], ['m', 1], ['?', 1], ['X', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1], ['k', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1], ['k', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 92, in createRecord
    if s[index] != recordlist[i][0]:
TypeError: list indices must be integers or slices, not list
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 90, in createRecord
    newlist.append([s[index],1])
NameError: name 'newlist' is not defined
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1]]
[['K', 1], ['o', 1], ['k', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1]]
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 97, in createRecord
    print(newlist)
NameError: name 'newlist' is not defined
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1], ['k', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1], ['k', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 1]]
[['K', 1], ['o', 1], ['k', 1]]
[['K', 1], ['o', 1], ['k', 1], ['k', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 2], ['k', 1], ['k', 1], ['o', 1], ['o', 1], ['o', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    createRecord('Kokomo?')
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 92, in createRecord
    if s[index] != recordlist[l]:
TypeError: list indices must be integers or slices, not list
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['k', 1], ['o', 2], ['o', 2], ['o', 2], ['o', 2], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['m', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['o', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>>  createRecord('Kokomo?')
		       
SyntaxError: unexpected indent
>>> createRecord('Kokomo?')
		       
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
1
0
2
0
1
3
0
1
2
4
0
1
2
3
5
0
1
2
3
4
6
0
1
2
3
4
5
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
KeyboardInterrupt
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Check index: 1
Check newindex:  0
Check index: 2
Check newindex:  0
Check newindex:  1
Check index: 3
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check index: 4
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check newindex:  3
Check index: 5
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check newindex:  3
Check newindex:  4
Check index: 6
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check newindex:  3
Check newindex:  4
Check newindex:  5
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Check index: 1
Check newindex:  0
Check index: 2
Check newindex:  0
Check newindex:  1
Check index: 3
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check index: 4
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check newindex:  3
Check index: 5
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check newindex:  3
Check newindex:  4
Check index: 6
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check newindex:  3
Check newindex:  4
Check newindex:  5
[['K', 1], ['o', 3], ['k', 1], ['o', 2], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Check index: 1
Check newindex:  0
Check index: 2
Check newindex:  0
Check newindex:  1
Check index: 3
Check newindex:  0
Check newindex:  1
Check index: 4
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check newindex:  3
Check index: 5
Check newindex:  0
Check newindex:  1
Check index: 6
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check newindex:  3
Check newindex:  4
Check newindex:  5
[['K', 1], ['o', 3], ['k', 1], ['o', 1], ['m', 1], ['o', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> createRecord('Kokomo?')
		       
Check index: 1
Check newindex:  0
Check index: 2
Check newindex:  0
Check newindex:  1
Check index: 3
Check newindex:  0
Check newindex:  1
Check index: 4
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check index: 5
Check newindex:  0
Check newindex:  1
Check index: 6
Check newindex:  0
Check newindex:  1
Check newindex:  2
Check newindex:  3
[['K', 1], ['o', 3], ['k', 1], ['m', 1], ['?', 1]]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 121, in frequencies
    if s[string] in l[lists]:
TypeError: string indices must be integers
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 119, in frequencies
    if s in l[lists]:
TypeError: list indices must be integers or slices, not list
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
['K', 1]
['o', 3]
['k', 1]
['m', 1]
['?', 1]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
['K', 1]
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
  File "/Users/janechoi/Documents/pa08-characterRecords.py", line 120, in frequencies
    if s in l[lists][0]:
TypeError: list indices must be integers or slices, not list
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
['K', 1]
0
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
['K', 1]
['o', 3]
['k', 1]
['m', 1]
['?', 1]
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
['K', 1]
K
['o', 3]
o
['k', 1]
k
['m', 1]
m
['?', 1]
?
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
['K', 1]
0
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
['K', 1]
['o', 3]
3
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
['K', 1]
['o', 3]
3
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========
>>> frequencies('o',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
3
>>> 
======== RESTART: /Users/janechoi/Documents/pa08-characterRecords.py ========

>>> frequencies('m',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
1
>>> frequencies('r',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
0
>>> frequencies('k',[['K',1],['o',3],['k',1],['m',1],['?',1]])
		       
1
>>> listX = ['S', 'h', 'a', 'r', 'e', 'd']
listY = listX
listZ = ['S', 'h', 'a', 'r', 'e', 'd']
listX.append('!')
		       
SyntaxError: multiple statements found while compiling a single statement
>>> listX = ['S', 'h', 'a', 'r', 'e', 'd']
		       
>>> listY = listX
		       
>>> listZ = ['S', 'h', 'a', 'r', 'e', 'd']
		       
>>> listX.append('!')
		       
>>> listX
		       
['S', 'h', 'a', 'r', 'e', 'd', '!']
>>> listY
		       
['S', 'h', 'a', 'r', 'e', 'd', '!']
>>> listZ
		       
['S', 'h', 'a', 'r', 'e', 'd']
>>> del listY[2]
		       
>>> listX
		       
['S', 'h', 'r', 'e', 'd', '!']
>>> listZ
		       
['S', 'h', 'a', 'r', 'e', 'd']
>>> listZ.remove('d')
		       
>>> listX
		       
['S', 'h', 'r', 'e', 'd', '!']
>>> listZ
		       
['S', 'h', 'a', 'r', 'e']
>>> listX = [2,0,1,8,10,18]
		       
>>> listX
		       
[2, 0, 1, 8, 10, 18]
>>> listY
		       
['S', 'h', 'r', 'e', 'd', '!']
>>> listX[4:] = [0,0]
		       
>>> listX
		       
[2, 0, 1, 8, 0, 0]
>>> listY.clear()
		       
>>> listY
		       
[]
>>> 
