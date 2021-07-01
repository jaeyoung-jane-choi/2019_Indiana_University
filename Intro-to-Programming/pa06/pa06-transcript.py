Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskA.py ==============
Enter a number (To end the program enter 'stop'):12
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskA.py", line 17, in <module>
    input_sum += int(user_input)
NameError: name 'input_sum' is not defined
2
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskA.py ==============
Enter a number (To end the program enter 'stop'):13
Enter a number (To end the program enter 'stop'):20
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskA.py", line 17, in <module>
    input_sum += int(user_input)
NameError: name 'input_sum' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskA.py ==============
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):12
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):8
Enter a number (To end the program enter 'stop'):8
Enter a number (To end the program enter 'stop'):stop
The sum is: 68
The max number is: 20
The min number is: 8
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskA.py ==============
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):30
Enter a number (To end the program enter 'stop'):40
Enter a number (To end the program enter 'stop'):50
Enter a number (To end the program enter 'stop'):stop
The sum is: 160
The max number is: 50
The min number is: 20
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskA.py ==============
Enter a number (To end the program enter 'stop'):10
Enter a number (To end the program enter 'stop'):9
Enter a number (To end the program enter 'stop'):8
Enter a number (To end the program enter 'stop'):7
Enter a number (To end the program enter 'stop'):7
Enter a number (To end the program enter 'stop'):6
Enter a number (To end the program enter 'stop'):1
Enter a number (To end the program enter 'stop'):1
Enter a number (To end the program enter 'stop'):stop
The sum is: 49
The max number is: 10
The min number is: 1
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskA.py ==============
Enter a number (To end the program enter 'stop'):12
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):stop
Enter a number (To end the program enter 'stop'):2
The sum is: 34
The max number is: 20
The min number is: 12
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskA.py ==============
Enter a number (To end the program enter 'stop'):12
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):30
Enter a number (To end the program enter 'stop'):12
Enter a number (To end the program enter 'stop'):10
Enter a number (To end the program enter 'stop'):10
Enter a number (To end the program enter 'stop'):9
Enter a number (To end the program enter 'stop'):9
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):30
Enter a number (To end the program enter 'stop'):33
Enter a number (To end the program enter 'stop'):33
Enter a number (To end the program enter 'stop'):stop
The sum is: 228
The max number is: 33
The min number is: 33
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskA.py ==============
Enter a number (To end the program enter 'stop'):12
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):30
Enter a number (To end the program enter 'stop'):30
Enter a number (To end the program enter 'stop'):12
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):stop
The sum is: 124
The max number is: 30
The min number is: 12
>>> '*'
'*'
>>> *
SyntaxError: invalid syntax
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name and integer (To end the program enter 'stop'):stop
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 22, in <module>
    user_input1,user_input2 = input("Enter a name and integer (To end the program enter 'stop'):").split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
'************'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
'************'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(11)
'***********'
>>> 'string'[0] not str
SyntaxError: invalid syntax
>>> 'string'[0]
's'
>>> '1string'[0]
'1'
>>> int('1string'[0] )
1
>>> int('1string'[0])
1
>>> int('string'[0] )
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int('string'[0] )
ValueError: invalid literal for int() with base 10: 's'
>>> int('1string'[0] ) = True
SyntaxError: can't assign to function call
>>> int('1string'[0] ) == True
True
>>> int('1string'[0] ) ==False
False
>>> int('string'[0] ) == True
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int('string'[0] ) == True
ValueError: invalid literal for int() with base 10: 's'
>>> 'string'[0]
's'
>>> type('1string'[0])
<class 'str'>
>>> len(12sta)
SyntaxError: invalid syntax
>>> len('12sta')
5
>>> '1string'[0] in '12345'
True
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> sum_all_digits('123bac')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    sum_all_digits('123bac')
  File "/Users/janechoi/Documents/pa06-functions.py", line 21, in sum_all_digits
    sum_digits += int(string)[n]
ValueError: invalid literal for int() with base 10: '123bac'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name and integer (To end the program enter 'stop'):stop
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 22, in <module>
    user_input1,user_input2 = input("Enter a name and integer (To end the program enter 'stop'):").split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
************
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
'************'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
'************'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
'result'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
'result'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
'************'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> "%s" %(result)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    "%s" %(result)
NameError: name 'result' is not defined
>>> printingstars(10)
**********
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    printingstars(10)
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 16, in printingstars
    return "%s" %(result)
NameError: name 'result' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(10)
'**********'
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> sum_all_digits('11s')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    sum_all_digits('11s')
  File "/Users/janechoi/Documents/pa06-functions.py", line 21, in sum_all_digits
    sum_digits += int(string)[n]
ValueError: invalid literal for int() with base 10: '11s'

>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> sum_all_digits('11s')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    sum_all_digits('11s')
  File "/Users/janechoi/Documents/pa06-functions.py", line 19, in sum_all_digits
    if str(string)[n] in ('1234567890') :
IndexError: string index out of range
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> sum_all_digits('11s')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    sum_all_digits('11s')
  File "/Users/janechoi/Documents/pa06-functions.py", line 19, in sum_all_digits
    if str(string)[n] in ('1234567890') :
IndexError: string index out of range
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> sum_all_digits('11s')
1
1
s
2
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> sum_all_digits('11s')
1
1
1
2
s
2
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> sum_all_digits('11s')
index is 1
index is 1
index is s
2
>>> sum_all_digits('11s1')
index is 1
index is 1
index is s
index is 1
3
>>> sum_all_digits('11s12s121gdadfs03d')
index is 1
index is 1
index is s
index is 1
index is 2
index is s
index is 1
index is 2
index is 1
index is g
index is d
index is a
index is d
index is f
index is s
index is 0
index is 3
index is d
12
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> a=10
>>> b=20
>>> a,b = swapTwoNumbers(a,b)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,b = swapTwoNumbers(a,b)
TypeError: cannot unpack non-iterable int object
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> a=10
>>> b=20
>>> a,b = swapTwoNumbers(a,b)
>>> print(a,b)
20 20
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> a=10
>>> b=20
>>> a,b = swapTwoNumbers(a,b)
>>> print(a,b)
20 10
>>> a=12
>>> b='a'
>>> a,b = swapTwoNumbers(a,b)
>>> print(a,b)
a 12
>>> a=12.32
>>> b='acb'
>>> a,b = swapTwoNumbers(a,b)
>>> print(a,b)
acb 12.32
>>> type*a,b)
SyntaxError: invalid syntax
>>> type(a,b)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    type(a,b)
TypeError: type() takes 1 or 3 arguments
>>> swapTwoNumbers(a,b)
(12.32, 'acb')
>>> type(a,b = swapTwoNumbers(a,b))
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    type(a,b = swapTwoNumbers(a,b))
TypeError: type() takes 1 or 3 arguments
>>> new = swapTwoNumbers(a,b)
>>> type(new)
<class 'tuple'>
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 19, in <module>
    print(("%s" %(stars)))
NameError: name 'stars' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
'************'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
'************'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
>>> printingstars(12)
'************'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name and integer (To end the program enter 'stop'):jane 12
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 28, in <module>
    star_num = printingstars(user_input2)
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 10, in printingstars
    stars = "*"*num
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name and integer (To end the program enter 'stop'):jane 12
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 38, in <module>
    print(type(user_input1,user_input2 ))
TypeError: type() takes 1 or 3 arguments
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name and integer (To end the program enter 'stop'):jane12
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 35, in <module>
    user_input1,user_input2 = input("Enter a name and integer (To end the program enter 'stop'):").split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name and integer (To end the program enter 'stop'):jane,12
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 35, in <module>
    user_input1,user_input2 = input("Enter a name and integer (To end the program enter 'stop'):").split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name and integer (To end the program enter 'stop'):jane 12
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 38, in <module>
    print(type(user_input1,user_input2 ))
TypeError: type() takes 1 or 3 arguments
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name and integer (To end the program enter 'stop'):jane 12
<class 'str'>
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name and integer (To end the program enter 'stop'):jane 12
<class 'tuple'>
>>> my_word = "programming"
>>> my_word[0]
'p'
>>> my_word[3]
'g'
>>> "my_word"[2]
'_'
>>> my_word[-2]
'n'
>>> 22 % 10
2
>>> a=''
>>> type(a)
<class 'str'>
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name and integer (To end the program enter 'stop'):jane 20
Enter a name and integer (To end the program enter 'stop'):stop
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 23, in <module>
    user_input1,user_input2 = input("Enter a name and integer (To end the program enter 'stop'):").split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane 20
Enter an integer (To end the program enter 'stop'):stop
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 30, in <module>
    star_num = printingstars(int(user_input2))
ValueError: invalid literal for int() with base 10: 'stop'
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer (To end the program enter 'stop'):20
Enter a name (To end the program enter 'stop'):stop
Enter an integer (To end the program enter 'stop'):stop
------------------------------------
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 42, in <module>
    print(user_input + str(star_num), end='')
NameError: name 'user_input' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer (To end the program enter 'stop'):20
Enter a name (To end the program enter 'stop'):stop
Enter an integer (To end the program enter 'stop'):
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 30, in <module>
    star_num = printingstars(int(user_input2))
ValueError: invalid literal for int() with base 10: ''
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):stop
Enter an integer (To end the program enter 'stop'):stop
------------------------------------
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa06-TaskB.py", line 42, in <module>
    print(user_input1 + str(star_num), end='')
NameError: name 'star_num' is not defined
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:20
Enter a name (To end the program enter 'stop'):stop
Enter an integer:
------------------------------------
stop********************------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:20
Enter a name (To end the program enter 'stop'):stop
------------------------------------
stop********************
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:12
Enter a name (To end the program enter 'stop'):stop
------------------------------------
stop************------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:1
Enter a name (To end the program enter 'stop'):stop
------------------------------------
stop*
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:10
Enter a name (To end the program enter 'stop'):stop
------------------------------------stop**********------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:10
Enter a name (To end the program enter 'stop'):stop
------------------------------------stop**********------------------------------------

>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:20
Enter a name (To end the program enter 'stop'):stop
------------------------------------
stop********************
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:11
Enter a name (To end the program enter 'stop'):stop
------------------------------------
stop      ***********
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:20
Enter a name (To end the program enter 'stop'):stop
------------------------------------
jane      ********************
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:20
Enter a name (To end the program enter 'stop'):bill
Enter an integer:10
Enter a name (To end the program enter 'stop'):stop
------------------------------------
bill      **********
------------------------------------
>>> info = str(name)+str(star_num)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    info = str(name)+str(star_num)
NameError: name 'name' is not defined
>>> name =''
>>> star_num = 12
>>> info = str(name)+str(star_num)
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:10
Enter a name (To end the program enter 'stop'):jess
Enter an integer:12
Enter a name (To end the program enter 'stop'):stop
------------------------------------
jess      ************
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:10
Enter a name (To end the program enter 'stop'):stop
------------------------------------
jane**********
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:10
Enter a name (To end the program enter 'stop'):jake
Enter an integer:20
Enter a name (To end the program enter 'stop'):stop
------------------------------------
jane**********jake********************
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):jane
Enter an integer:20
Enter a name (To end the program enter 'stop'):j
Enter an integer:10
Enter a name (To end the program enter 'stop'):stop
jane********************j**********
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):j
Enter an integer:10
Enter a name (To end the program enter 'stop'):k
Enter an integer:20
Enter a name (To end the program enter 'stop'):stop
------------------------------------

j**********
k********************
------------------------------------
j**********
k********************
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):j
Enter an integer:10
Enter a name (To end the program enter 'stop'):k
Enter an integer:22
Enter a name (To end the program enter 'stop'):l
Enter an integer:12
Enter a name (To end the program enter 'stop'):stop
------------------------------------

j**********
k**********************
l************
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):k
Enter an integer:1
Enter a name (To end the program enter 'stop'):j
Enter an integer:2
Enter a name (To end the program enter 'stop'):l10
Enter an integer:10
Enter a name (To end the program enter 'stop'):j
Enter an integer:39
Enter a name (To end the program enter 'stop'):stop
------------------------------------
    
k*    
j**    
l10**********    
j***************************************
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):j
Enter an integer:10
Enter a name (To end the program enter 'stop'):k
Enter an integer:20
Enter a name (To end the program enter 'stop'):ll
Enter an integer:10
Enter a name (To end the program enter 'stop'):stop
------------------------------------

j **********
k ********************
ll **********
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):j
Enter an integer:10
Enter a name (To end the program enter 'stop'):sl
Enter an integer:20
Enter a name (To end the program enter 'stop'):stop
------------------------------------


j **********sl ********************
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskB.py ==============
Enter a name (To end the program enter 'stop'):j
Enter an integer:10
Enter a name (To end the program enter 'stop'):k
Enter an integer:20
Enter a name (To end the program enter 'stop'):l
Enter an integer:21
Enter a name (To end the program enter 'stop'):stop
------------------------------------

j    **********
k    ********************
l    *********************
------------------------------------
>>> 
============== RESTART: /Users/janechoi/Documents/pa06-TaskA.py ==============
Enter a number (To end the program enter 'stop'):12
Enter a number (To end the program enter 'stop'):10
Enter a number (To end the program enter 'stop'):9
Enter a number (To end the program enter 'stop'):1
Enter a number (To end the program enter 'stop'):1
Enter a number (To end the program enter 'stop'):12
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):20
Enter a number (To end the program enter 'stop'):1
Enter a number (To end the program enter 'stop'):stop
The sum is: 86
The max number is: 20
The min number is: 1
>>> 
============ RESTART: /Users/janechoi/Documents/pa06-functions.py ============
>>> sum_all_digits('12absdicl2kkjlkj2')
7
>>> a=1-
SyntaxError: invalid syntax
>>> a='dkd'
>>> b=10
>>> a,b = swapTwoNumbers(a,b)
>>> print(a,b)
10 dkd
>>> 
