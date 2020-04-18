Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
Line 1
This is line 2
That makes this line 3
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
L
ine
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
L
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
Line 1

>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
Line 1

This is line 2

That makes this line 3
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
['Line 1\n', 'This is line 2\n', 'That makes this line 3']
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
['Line 1\n', 'This is line 2\n', 'That makes this line 3']
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
['Line 1\n', 'This is line 2\n', 'That makes this line 3']
['Line 1', 'This is line 2', 'That makes this line 3']
>>> newlines[0]
'Line 1'
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
/Users/janechoi/Documents
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
enter a number: no
not a number!
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
>>> print(text)
<_io.TextIOWrapper name='output.txt' mode='w' encoding='UTF-8'>
>>> text
<_io.TextIOWrapper name='output.txt' mode='w' encoding='UTF-8'>
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
26
2
>>> text.open()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    text.open()
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
/Users/janechoi/Documents
>>> os.path.abspath('myFile.txt')
'/Users/janechoi/Documents/myFile.txt'
>>> os.path.isdir('/Users/janechoi')
True
>>> os.path.isfile('myFile.txt')
True
>>> os.listdir(cwd)
['My Tableau Repository', 'My Tableau Prep Repository', '.DS_Store', '.localized', '12:2.py', '.tmp.drivedownload', '__pycache__', 'nw.py', 'Adobe', '12:4.py', 'lab14-transcript.py', 'R 기초 강의.docx', 'myFile.txt', 'output.txt']
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
Something went wrong.
>>> s = '1 2\t 3\n 4'
>>> print(s)
1 2	 3
 4
>>> print(repr(s))
'1 2\t 3\n 4'
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
Line 1
This is line 2
That makes this line 3
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
>>> fh
<_io.TextIOWrapper name='example.txt' mode='w' encoding='UTF-8'>
>>> fh.readlines()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    fh.readlines()
ValueError: I/O operation on closed file.
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
Traceback (most recent call last):
  File "/Users/janechoi/Documents/nw.py", line 5, in <module>
    print(fh.readline(1))
io.UnsupportedOperation: not readable
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
Traceback (most recent call last):
  File "/Users/janechoi/Documents/nw.py", line 5, in <module>
    print(fh.readlines())
io.UnsupportedOperation: not readable
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
Traceback (most recent call last):
  File "/Users/janechoi/Documents/nw.py", line 11, in <module>
    print(myFile.readlines())
NameError: name 'myFile' is not defined
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
[]
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
[]
Traceback (most recent call last):
  File "/Users/janechoi/Documents/nw.py", line 12, in <module>
    print(fobj_out.readlines())
io.UnsupportedOperation: not readable
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
[]
Traceback (most recent call last):
  File "/Users/janechoi/Documents/nw.py", line 12, in <module>
    print(fobj_out.readlines())
io.UnsupportedOperation: not readable
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================
Line1
This is line2
Line2? Line3!
[]
Traceback (most recent call last):
  File "/Users/janechoi/Documents/nw.py", line 12, in <module>
    print(fobj_out.readlines())
io.UnsupportedOperation: not readable
>>> poem = open("myFile.txt").readlines()
>>> poem
['Line1\n', 'This is line2\n', 'Line2? Line3!']
>>> poem[0]
'Line1\n'
>>> poem = open("myFile.txt").read()
>>> poem
'Line1\nThis is line2\nLine2? Line3!'
>>> type(poem)
<class 'str'>
>>> poem2 = open("myFile.txt").readlines()
>>> type(poem2)
<class 'list'>
>>> fh = open("buck_mulligan.txt")
>>> fh.tell()
0
>>> fh.read(7)
'Stately'
>>> fh.read()
', plump Buck Mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed.'
>>> fh.tell()
121
>>> fh.seek(9)
9
>>> fh.read(5)
'plump'
>>> fh = open("buck_mulligan.txt")
>>> fh.read(15)
'Stately, plump '
>>> fh.seek(fh.tell(),-6)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    fh.seek(fh.tell(),-6)
ValueError: invalid whence (-6, should be 0, 1 or 2)
>>> fh.seek(fh.tell()-6)
9
>>> fh.read()
'plump Buck Mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed.'
>>> fh.seek(fh.tell()-10)
111
>>> fh = open('colours.txt', 'w+')
>>> fh.write('The colour brown')
16
>>> fh.seek(11)
11
>>> fh.read(5)
'brown'
>>> fh.tell()
16
>>> fh.seek(11)
11
>>> fh.write('green')
5
>>> fh.seek(0)
0
>>> fh.read()
'The colour green'
>>> 
================== RESTART: /Users/janechoi/Documents/nw.py ==================

Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> bisect(5)
2.5
>>> bisect(-24.6)
-12.3
>>> bisect(2+4j)
(1+2j)
>>> bisect('foobar')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    bisect('foobar')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 12, in bisect
    return pinput/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> bisect(2+4j)
(1+2j)
>>> bisect('foobar')
Traceback (most recent call last):
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 13, in bisect
    result = pinput/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    bisect('foobar')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 16, in bisect
    result
UnboundLocalError: local variable 'result' referenced before assignment
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> bisect(2+4j)
(1+2j)
>>> bisect('foobar')
'foobar'
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> bisect('foobar')
'foobar'
>>> num
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> bisect('foobar')
3.0
'foobar'
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> bisect('foobar')
3.0
'foobar'
>>> bisect((2,4,6,8,10))
2.5
(2, 4, 6, 8, 10)
>>> round(2.5)
2
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> bisect((2,4,6,8,10))
2
(2, 4)
>>> bisect('foobar')
3
'foo'
>>> bisect(["",".","..","...","....","....."])
3
['', '.', '..']
>>> bisect({"key1":"value1","key2":"value2","key3":"value3"})
2
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
>>> bisect(True)
0.5
>>> bisect(False)
0.0
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> bisect('food','bar')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    bisect('food','bar')
TypeError: bisect() takes 1 positional argument but 2 were given
>>> a= ('food','bar')
>>> bisect(a)
('food',)
>>> type(a)
<class 'tuple'>
>>> a[0]
'food'
>>> len(a)
2
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
<_io.TextIOWrapper name='hanlon.txt' mode='r' encoding='UTF-8'>
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
<_io.TextIOWrapper name='hanlon.txt' mode='r' encoding='UTF-8'>
['Never attribute to malice that which is adequately explained by stupidity.\n']
>>> print_trigrams("hi.txt")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print_trigrams("hi.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 36, in print_trigrams
    text = open(pname, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'hi.txt'
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Nev
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
<class '_io.TextIOWrapper'>
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
<class 'list'>
>>> len(text)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    len(text)
NameError: name 'text' is not defined
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 38, in print_trigrams
    print(len(text))
TypeError: object of type '_io.TextIOWrapper' has no len()
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 41, in print_trigrams
    newline += new
UnboundLocalError: local variable 'newline' referenced before assignment
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
N
Ne
Nev
Neve
Never
Never 
Never a
Never at
Never att
Never attr
Never attri
Never attrib
Never attribu
Never attribut
Never attribute
Never attribute 
Never attribute t
Never attribute to
Never attribute to 
Never attribute to m
Never attribute to ma
Never attribute to mal
Never attribute to mali
Never attribute to malic
Never attribute to malice
Never attribute to malice 
Never attribute to malice t
Never attribute to malice th
Never attribute to malice tha
Never attribute to malice that
Never attribute to malice that 
Never attribute to malice that w
Never attribute to malice that wh
Never attribute to malice that whi
Never attribute to malice that whic
Never attribute to malice that which
Never attribute to malice that which 
Never attribute to malice that which i
Never attribute to malice that which is
Never attribute to malice that which is 
Never attribute to malice that which is a
Never attribute to malice that which is ad
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 43, in print_trigrams
    print(newline)
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Never attribute to malice that which is adequately explained by stupidity.

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> text.read(3)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    text.read(3)
NameError: name 'text' is not defined
>>> print_trigrams("hanlon.txt")
<class '_io.TextIOWrapper'>
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> _io.TextIOWrapper
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    _io.TextIOWrapper
NameError: name '_io' is not defined
>>>  print_trigrams("hanlon.txt")
SyntaxError: unexpected indent
>>> print_trigrams("hanlon.txt")
Never attribute to malice that which is adequately explained by stupidity.

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 42, in print_trigrams
    text.close()
AttributeError: 'str' object has no attribute 'close'
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>>  print_trigrams("hanlon.txt")
SyntaxError: unexpected indent
>>> print_trigrams("hanlon.txt")
<class 'list'>
1
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
<class 'str'>
75
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
<class 'str'>
Never attribute to malice that which is adequately explained by stupidity.

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Never attribute to malice that which is adequately explained by stupidity.

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
N
e
v
e
r
 
a
t
t
r
i
b
u
t
e
 
t
o
 
m
a
l
i
c
e
 
t
h
a
t
 
w
h
i
c
h
 
i
s
 
a
d
e
q
u
aTraceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 43, in print_trigrams
    print(letter)
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Nev
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Nev
er 
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Nev
er 
att
rib
ute
 to
 ma
lic
e t
hat
 wh
ich
 is
 ad
equ
ate
ly 
exp
lai
ned
 by
 st
upi
dit
y.





























ç























Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 39, in print_trigrams
    print(text.read(3))
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Nev
er 
att
rib
ute
 to
 ma
lic
e t
hat
 wh
ich
 is
 ad
equ
ate
ly 
exp
lai
ned
 by
 st
upi
dit
y.





















Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 39, in print_trigrams
    print(text.read(3))
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Nev
3
er 
6
att
9
rib
12
ute
15
 to
18
 ma
21
lic
24
e t
27
hat
30
 wh
33
ich
36
 is
39
 ad
42
equ
45
ate
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 39, in print_trigrams
    print(text.read(3))
KeyboardInterrupt
>>> print_trigrams("hanlon.txt")
Nev
3
er 
6
att
9
rib
12
ute
15
 to
18
 ma
21
lic
24
e t
27
hat
30
 wh
33
ich
36
 is
39
 ad
42
equ
45
ate
48
ly 
51
exp
54
lai
57
ned
60
 by
63
 st
66
upi
69
dit
72
y.

76

76

76

76

76

76

76

76
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 39, in print_trigrams
    print(text.read(3))
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Nev
3
er 
6
att
9
rib
12
ute
15
 to
18
 ma
21
lic
24
e t
27
hat
30
 wh
33
ich
36
 is
39
 ad
42
equ
45
ate
48
ly 
51
exp
54
lai
57
ned
60
 by
63
 st
66
upi
69
dit
72
y.

76

76

76

76

76

76
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 41, in print_trigrams
    print(text.tell())
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> length
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    length
NameError: name 'length' is not defined
>>> print_trigrams("hanlon.txt")
75
Nev
3
er 
6
att
9
rib
12
ute
15
 to
18
 ma
21
lic
24
e t
27
hat
30
 wh
33
ich
36
 is
39
 ad
42
equ
45
ate
48Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print_trigrams("hanlon.txt")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 42, in print_trigrams
    print(text.tell())
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
75
Nev
3
er 
6
att
9
rib
12
ute
15
 to
18
 ma
21
lic
24
e t
27
hat
30
 wh
33
ich
36
 is
39
 ad
42
equ
45
ate
48
ly 
51
exp
54
lai
57
ned
60
 by
63
 st
66
upi
69
dit
72
y.

76
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_trigrams("hanlon.txt")
Nev
er 
att
rib
ute
 to
 ma
lic
e t
hat
 wh
ich
 is
 ad
equ
ate
ly 
exp
lai
ned
 by
 st
upi
dit
y.

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_ngrams("hanlon.txt",5)
Never
 attr
ibute
 to m
alice
 that
 whic
h is 
adequ
ately
 expl
ained
 by s
tupid
ity.

>>> print_ngrams("hanlon.txt",10)
Never attr
ibute to m
alice that
 which is 
adequately
 explained
 by stupid
ity.

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_ngrams("murphy.txt",7)
I'm sorry, but I could not find a file with that name.
>>> print_ngrams("hanlon.txt",10)
Never attr
ibute to m
alice that
 which is 
adequately
 explained
 by stupid
ity.

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> print_ngrams("hanlon.txt",10)
Never attr
<class 'str'>
alice that
<class 'str'>
adequately
<class 'str'>
 by stupid
<class 'str'>
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?2
What file should I display?hanlon's razor
There was an error working with that file. Please choose a different filename.
What file should I display?hanlon.txt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?7
What file should I display?hanlon
There was an error working with that file. Please choose a different filename.
What file should I display?hanlon.txt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?7
What file should I display?hanlond
There was an error working with that file. Please choose a different filename.
What file should I display?hanlon.txt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?7
What file should I display?hanlon.txt
There was an error working with that file. Please choose a different filename.
What file should I display?hanlon.txt
>>> user_input1
'7'
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?7
What file should I display?hanlon.txt
Never a
ttribut
e to ma
lice th
at whic
h is ad
equatel
y expla
ined by
 stupid
ity.

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?7
What file should I display?hanlon.txt
Never a
ttribut
e to ma
lice th
at whic
h is ad
equatel
y expla
ined by
 stupid
ity.

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?8
What file should I display?hanlon
There was an error working with that file. Please choose a different filename.
What file should I display?hhan
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?7
What file should I display?hanlon
Traceback (most recent call last):
  File "/Users/janechoi/Documents/lab14-printer_of_ngrams.py", line 15, in <module>
    text = open(user_input2, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'hanlon'
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?7
What file should I display?hanlon
There was an error working with that file. Please choose a different filename.
What file should I display?hanlon
There was an error working with that file. Please choose a different filename.
What file should I display?hanlon.txt
Never a
ttribut
e to ma
lice th
at whic
h is ad
equatel
y expla
ined by
 stupid
ity.

What file should I display?
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?7
What file should I display?hanlon
There was an error working with that file. Please choose a different filename.
What file should I display?hanllon
There was an error working with that file. Please choose a different filename.
What file should I display?hanlon.txt
Never a
ttribut
e to ma
lice th
at whic
h is ad
equatel
y expla
ined by
 stupid
ity.

Never a
ttribut
e to ma
lice th
at whic
h is ad
equatel
y expla
ined by
 stupid
ity.

Never a
ttribut
e to ma
lice th
at whic
h is ad
equatel
y expla
ined by
 stupid
ity.

Never a
ttribut
e to ma
lice th
at whic
h is ad
equatel
y expla
ined by
 stupid
ity.

Never a
ttribut
e to ma
lice th
There was an error working with that file. Please choose a different filename.
What file should I display?
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?2
What file should I display?hanlon.txt
Ne
ve
r 
at
tr
ib
ut
e 
to
 m
al
ic
e 
th
at
 w
hi
ch
 i
s 
ad
eq
ua
te
ly
 e
xp
la
in
ed
 b
y 
st
up
id
it
y.


>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?10
What file should I display?ha
There was an error working with that file. Please choose a different filename.
What file should I display?jd
There was an error working with that file. Please choose a different filename.
What file should I display?ha
There was an error working with that file. Please choose a different filename.
What file should I display?kl
There was an error working with that file. Please choose a different filename.
What file should I display?dhjls
There was an error working with that file. Please choose a different filename.
What file should I display?hals
There was an error working with that file. Please choose a different filename.
What file should I display?hanlon.txt
Never attr
ibute to m
alice that
 which is 
adequately
 explained
 by stupid
ity.

>>> a = ['a','b','c']
>>> b = ['b','c','a']
>>> a=b
>>> a==b
True
>>> a
['b', 'c', 'a']
>>> b
['b', 'c', 'a']
>>> a = ['a','b','c']
>>> a==b
False
>>> order(b)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    order(b)
NameError: name 'order' is not defined
>>> b.order()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    b.order()
AttributeError: 'list' object has no attribute 'order'
>>> b.sort()
>>> b
['a', 'b', 'c']
>>> a==b
True
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> is_anagram("Listen","Silent")
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    is_anagram("Listen","Silent")
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 80, in is_anagram
    letter1 += letters
UnboundLocalError: local variable 'letter1' referenced before assignment
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> is_anagram("Listen","Silent")
['L', 'i', 's', 't', 'e', 'n']
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> is_anagram("Listen","Silent")
True
>>> is_anagram("foobar","baffor")
True
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> is_anagram("foobar","baffor")
None
None
True
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> is_anagram("foobar","baffor")
['a', 'b', 'f', 'o', 'o', 'r']
['a', 'b', 'f', 'f', 'o', 'r']
False
>>> is_anagram("Listen","Silent")
['L', 'e', 'i', 'n', 's', 't']
['S', 'e', 'i', 'l', 'n', 't']
False
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> is_anagram("Listen","Silent")
['e', 'i', 'l', 'n', 's', 't']
['e', 'i', 'l', 'n', 's', 't']
True
>>> is_anagram("foobar","baffor")
['a', 'b', 'f', 'o', 'o', 'r']
['a', 'b', 'f', 'f', 'o', 'r']
False
>>> is_anagram("fool","loop")
['f', 'l', 'o', 'o']
['l', 'o', 'o', 'p']
False
>>> is_anagram("fOol","looF")
['f', 'l', 'o', 'o']
['f', 'l', 'o', 'o']
True
>>> is_anagram("LiSteN","SilEnt")
['e', 'i', 'l', 'n', 's', 't']
['e', 'i', 'l', 'n', 's', 't']
True
>>> is_anagram("PanDA","AndPa")
['a', 'a', 'd', 'n', 'p']
['a', 'a', 'd', 'n', 'p']
True
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams(ab)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    find_anagrams(ab)
NameError: name 'ab' is not defined
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

<class 'str'>
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

<class 'str'>
>>> find_anagrams(ab)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    find_anagrams(ab)
NameError: name 'ab' is not defined
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c
Traceback (most recent call last):
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 100, in <module>
    print(line)
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

Traceback (most recent call last):
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 101, in <module>
    print(line.tell())
AttributeError: 'str' object has no attribute 'tell'
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
Traceback (most recent call last):
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 99, in <module>
    print(len(text))
TypeError: object of type 'builtin_function_or_method' has no len()
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
3712691
&c

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
3712691
&c
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
3712691
&c

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c

&c
Traceback (most recent call last):
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 99, in <module>
    print(text.readline())
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c
'd
'em
'll
'm
'mid
'midst
'mongst
'prentice
're
's
'sblood
'sbodikins
'sdeath
'sfoot
'sheart
'shun
'slid
'slife
'slight
'snails
'strewth
't
'til
'tis
'twas
'tween
'twere
'twill
'twixt
Traceback (most recent call last):
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 99, in <module>
    print(line.rstrip())
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

'd

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&
c

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

3
'd

6
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

3
'd

6
>>> find_anagrams(ab)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    find_anagrams(ab)
NameError: name 'ab' is not defined
>>> find_anagrams('ab')
&c

['a', 'b']
['\n', '&', 'c']
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

3
'd

6
>>> find_anagrams('ab')
&c

['a', 'b']
['\n', '&', 'c']
>>> newlist
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    newlist
NameError: name 'newlist' is not defined
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
&c

3
'd

6
>>> find_anagrams('ab')
&c

['a', 'b']
['\n', '&', 'c']
[]
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams'n&c')
SyntaxError: invalid syntax
>>> find_anagrams('n&c')
&c

['&', 'c', 'n']
['\n', '&', 'c']
[]
>>> find_anagrams('\n&c')
&c

['\n', '&', 'c']
['\n', '&', 'c']
['&c\n']
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('n&c')
&c

['&', 'c', 'n']
['\n', '&', 'c']
[]
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('n&c')
&c
['&', 'c', 'n']
['&', 'c']
[]
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('&c')
&c
['&', 'c']
['&', 'c']
['&c']
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('&c')
&c
['&', 'c']
['&', 'c']
'd
['&', 'c']
["'", 'd']
'em
['&', 'c']
["'", 'e', 'm']
'll
['&', 'c']
["'", 'l', 'l']
'm
['&', 'c']
["'", 'm']
'mid
['&', 'c']
["'", 'd', 'i', 'm']
'midst
['&', 'c']
["'", 'd', 'i', 'm', 's', 't']
'mongst
['&', 'c']
["'", 'g', 'm', 'n', 'o', 's', 't']
'prentice
['&', 'c']
["'", 'c', 'e', 'e', 'i', 'n', 'p', 'r', 't']
're
['&', 'c']
["'", 'e', 'r']
's
['&', 'c']
["'", 's']
'sblood
['&', 'c']
["'", 'b', 'd', 'l', 'o', 'o', 's']
'sbodikins
['&', 'c']
["'", 'b', 'd', 'i', 'i', 'k', 'n', 'o', 's', 's']
'sdeath
['&', 'c']
["'", 'a', 'd', 'e', 'h', 's', 't']
'sfoot
['&', 'c']
["'", 'f', 'o', 'o', 's', 't']
'sheart
['&', 'c']
["'", 'a', 'e', 'h', 'r', 's', 't']
'shun
['&', 'c']
["'", 'h', 'n', 's', 'u']
'slid
['&', 'c']
["'", 'd', 'i', 'l', 's']
'slife
['&', 'c']
["'", 'e', 'f', 'i', 'l', 's']
'slight
['&', 'c']
["'", 'g', 'h', 'i', 'l', 's', 't']
'snails
['&', 'c']
["'", 'a', 'i', 'l', 'n', 's', 's']
'strewth
['&', 'c']
["'", 'e', 'h', 'r', 's', 't', 't', 'w']Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    find_anagrams('&c')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 112, in find_anagrams
    if is_anagram(str1, line) :
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 90, in is_anagram
    print(letter2)
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('and')
['a', 'd', 'n']
['&', 'c']
['a', 'd', 'n']
["'", 'd']
['a', 'd', 'n']
["'", 'e', 'm']
['a', 'd', 'n']
["'", 'l', 'l']
['a', 'd', 'n']
["'", 'm']
['a', 'd', 'n']
["'", 'd', 'i', 'm']
['a', 'd', 'n']
["'", 'd', 'i', 'm', 's', 't']
['a', 'd', 'n']
["'", 'g', 'm', 'n', 'o', 's', 't']
['a', 'd', 'n']
["'", 'c', 'e', 'e', 'i', 'n', 'p', 'r', 't']
['a', 'd', 'n']
["'", 'e', 'r']
['a', 'd', 'n']
["'", 's']
['a', 'd', 'n']
["'", 'b', 'd', 'l', 'o', 'o', 's']
['a', 'd', 'n']
["'", 'b', 'd', 'i', 'i', 'k', 'n', 'o', 's', 's']
['a', 'd', 'n']
["'", 'a', 'd', 'e', 'h', 's', 't']
['a', 'd', 'n']
["'", 'f', 'o', 'o', 's', 't']
['a', 'd', 'n']
["'", 'a', 'e', 'h', 'r', 's', 't']
['a', 'd', 'n']
["'", 'h', 'n', 's', 'u']
['a', 'd', 'n']
["'", 'd', 'i', 'l', 's']
['a', 'd', 'n']
["'", 'e', 'f', 'i', 'l', 's']
['a', 'd', 'n']
["'", 'g', 'h', 'i', 'l', 's', 't']
['a', 'd', 'n']Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    find_anagrams('and')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 112, in find_anagrams
    if is_anagram(str1, line) :
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 83, in is_anagram
    print(letter1)
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('&c')
&c
['&', 'c']
['&', 'c']
'd
['&', 'c']
["'", 'd']
'em
['&', 'c']
["'", 'e', 'm']
'll
['&', 'c']
["'", 'l', 'l']
'm
['&', 'c']
["'", 'm']
'mid
['&', 'c']
["'", 'd', 'i', 'm']
'midst
['&', 'c']
["'", 'd', 'i', 'm', 's', 't']
'mongst
['&', 'c']
["'", 'g', 'm', 'n', 'o', 's', 't']
'prentice
['&', 'c']
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    find_anagrams('&c')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 112, in find_anagrams
    if is_anagram(str1, line) :
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 83, in is_anagram
    print(letter1)
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('&c')
&c
['&', 'c']
['&', 'c']
['&c']
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('&c')
&c
'd
'em
'll
'm
'mid
'midst
'mongst
'prentice
're
's
'sblood
'sbodikins
'sdeath
'sfoot
'sheart
'shun
'slid
'slife
'slight
'snails
'strewth
't
'til
'tis
'twas
'tween
'twere
'twill
'twixt
'twould
'un
've
1080
10th
1st
2
2nd
3rd
4th
5th
6th
7th
8th
9th
a
a'
a's
a/c
a1
aa
aaa
aah
aahed
aahing
aahs
aal
aalii
aaliis
aals
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    find_anagrams('&c')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 110, in find_anagrams
    print(line)
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('nail')
&c
'd
'em
'll
'm
'mid
'midst
'mongst
'prentice
're
's
'sblood
'sbodikins
'sdeath
'sfoot
'sheart
'shun
'slid
'slife
'slight
'snails
'strewth
't
'til
'tis
'twas
'tween
'twere
'twill
'twixt
'twould
'un
've
1080
10th
1st
2
2nd
3rd
4th
5th
6th
7th
8th
9th
a
a'
a's
a/c
a1
aa
aaa
aah
aahed
aahing
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    find_anagrams('nail')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 110, in find_anagrams
    print(line)
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('&c')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    find_anagrams('&c')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 108, in find_anagrams
    line = text.readline()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/codecs.py", line 319, in decode
    def decode(self, input, final=False):
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('apple')
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    find_anagrams('apple')
NameError: name 'find_anagrams' is not defined
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('apple')
&c
'd
'em
'll
'm
'mid
'midst
'mongst
'prentice
're
's
'sblood
'sbodikins
'sdeath
'sfoot
'sheart
'shun
'slid
'slife
'slight
'snails
'strewth
't
'til
'tis
'twas
'tween
'twere
'twill
'twixt
'twould
'un
've
1080
10th
1st
2
2nd
3rd
4th
5th
6th
7th
8th
9th
a
a'
a's
a/c
a1
aa
aaa
aah
aahed
aahing
aahs
aal
aalii
aaliis
aals
aam
aardvark
aardvarks
aardwolf
aardwolves
aargh
aaron
aaronic
aarrgh
aarrghh
aas
aasvogel
aasvogels
ab
aba
abac
abaca
abacas
abacate
abacaxi
abacay
abaci
abacinate
abacination
abacisci
abaciscus
abacist
aback
abacli
abacot
abacterial
abactinal
abactinally
abaction
abactor
abaculi
abaculus
abacus
abacuses
abada
abaddon
abadejo
abadengo
abadia
abaff
abaft
abaisance
abaised
abaiser
abaisse
abaissed
abaka
abakas
abalation
abalienate
abalienated
abalienating
abalienation
abalone
abalones
abamp
abampere
abamperes
abamps
aband
abandon
abandonable
abandoned
abandonedly
abandonee
abandoner
abandoners
abandoning
abandonment
abandonments
abandons
abandum
abanet
abanga
abannition
abapical
abaptiston
abaptistum
abarthrosis
abarticular
abarticulation
abas
abase
abased
abasedly
abasedness
abasement
abasements
abaser
abasers
abases
abash
abashed
abashedly
abashedness
abashes
abashing
abashless
abashlessly
abashment
abashments
abasia
abasias
abasic
abasing
abasio
abask
abassi
abastard
abastardize
abastral
abatable
abatage
abate
abated
abatement
abatements
abater
abaters
abates
abatic
abating
abatis
abatised
abatises
abatjour
abatjours
abaton
abator
abators
abattage
abattis
abattised
abattises
abattoir
abattoirs
abattu
abattue
abature
abaue
abave
abaxial
abaxile
abay
abayah
abaze
abb
abba
abbacies
abbacomes
abbacy
abbandono
abbas
abbasi
abbasid
abbassi
abbate
abbatial
abbatical
abbatie
abbaye
abbe
abbes
abbess
abbesses
abbest
abbevillian
abbey
abbey's
abbeys
abbeystead
abbeystede
abboccato
abbogada
abbot
abbot's
abbotcies
abbotcy
abbotnullius
abbotric
abbots
abbotship
abbotships
abbott
abbozzo
abbr
abbrev
abbreviatable
abbreviate
abbreviated
abbreviately
abbreviates
abbreviating
abbreviation
abbreviations
abbreviator
abbreviators
abbreviatory
abbreviature
abbroachment
abby
abc
abcess
abcissa
abcoulomb
abd
abdal
abdali
abdaria
abdat
abdest
abdicable
abdicant
abdicate
abdicated
abdicates
abdicating
abdication
abdications
abdicative
abdicator
abditive
abditory
abdom
abdomen
abdomen's
abdomens
abdomina
abdominal
abdominales
abdominalia
abdominalian
abdominally
abdominals
abdominoanterior
abdominocardiac
abdominocentesis
abdominocystic
abdominogenital
abdominohysterectomy
abdominohysterotomy
abdominoposterior
abdominoscope
abdominoscopy
abdominothoracic
abdominous
abdominovaginal
abdominovesical
abduce
abduced
abducens
abducent
abducentes
abduces
abducing
abduct
abducted
abducting
abduction
abduction's
abductions
abductor
abductor's
abductores
abductors
abducts
abeam
abear
abearance
abecedaire
abecedaria
abecedarian
abecedarians
abecedaries
abecedarium
abecedarius
abecedary
abed
abede
abedge
abegge
abeigh
abel
abele
abeles
abelian
abelite
abelmosk
abelmosks
abelmusk
abeltree
abend
abends
abenteric
abepithymia
aberdavine
aberdeen
aberdevine
aberduvine
abernethy
aberr
aberrance
aberrancies
aberrancy
aberrant
aberrantly
aberrants
aberrate
aberrated
aberrating
aberration
aberrational
aberrations
aberrative
aberrator
aberrometer
aberroscope
aberuncate
aberuncator
abesse
abessive
abet
abetment
abetments
abets
abettal
abettals
abetted
abetter
abetters
abetting
abettor
abettors
abevacuation
abey
abeyance
abeyances
abeyancies
abeyancy
abeyant
abfarad
abfarads
abhenries
abhenry
abhenrys
abhinaya
abhiseka
abhominable
abhor
abhorred
abhorrence
abhorrences
abhorrency
abhorrent
abhorrently
abhorrer
abhorrers
abhorrible
abhorring
abhors
abib
abichite
abidal
abidance
abidances
abidden
abide
abided
abider
abiders
abides
abidi
abiding
abidingly
abidingness
abiegh
abience
abient
abietate
abietene
abietic
abietin
abietineous
abietinic
abietite
abigail
abigails
abigailship
abigeat
abigei
abigeus
abilao
abilene
abiliment
abilitable
abilities
ability
ability's
abilla
abilo
abime
abintestate
abiogeneses
abiogenesis
abiogenesist
abiogenetic
abiogenetical
abiogenetically
abiogenist
abiogenous
abiogeny
abiological
abiologically
abiology
abioses
abiosis
abiotic
abiotical
abiotically
abiotrophic
abiotrophy
abir
abirritant
abirritate
abirritated
abirritating
abirritation
abirritative
abiston
abit
abiuret
abject
abjectedness
abjection
abjections
abjective
abjectly
abjectness
abjoint
abjudge
abjudged
abjudging
abjudicate
abjudicated
abjudicating
abjudication
abjudicator
abjugate
abjunct
abjunction
abjunctive
abjuration
abjurations
abjuratory
abjure
abjured
abjurement
abjurer
abjurers
abjures
abjuring
abkar
abkari
abkary
abl
ablach
ablactate
ablactated
ablactating
ablactation
ablaqueate
ablare
ablastemic
ablastin
ablastous
ablate
ablated
ablates
ablating
ablation
ablations
ablatitious
ablatival
ablative
ablatively
ablatives
ablator
ablaut
ablauts
ablaze
able
ableeze
ablegate
ablegates
ablegation
ablend
ableness
ablepharia
ablepharon
ablepharous
ablepsia
ablepsy
ableptical
ableptically
abler
ables
ablesse
ablest
ablet
ablewhackets
ablings
ablins
ablock
abloom
ablow
ablude
abluent
abluents
ablush
ablute
abluted
ablution
ablutionary
ablutions
abluvion
ably
abmho
abmhos
abmodalities
abmodality
abn
abnegate
abnegated
abnegates
abnegating
abnegation
abnegations
abnegative
abnegator
abnegators
abner
abnerval
abnet
abneural
abnormal
abnormalcies
abnormalcy
abnormalise
abnormalised
abnormalising
abnormalism
abnormalist
abnormalities
abnormality
abnormalize
abnormalized
abnormalizing
abnormally
abnormalness
abnormals
abnormities
abnormity
abnormous
abnumerable
abo
aboard
aboardage
abococket
abodah
abode
abode's
aboded
abodement
abodes
aboding
abody
abogado
abogados
abohm
abohms
aboideau
aboideaus
aboideaux
aboil
aboiteau
aboiteaus
aboiteaux
abolete
abolish
abolishable
abolished
abolisher
abolishers
abolishes
abolishing
abolishment
abolishment's
abolishments
abolition
abolitionary
abolitionise
abolitionised
abolitionising
abolitionism
abolitionist
abolitionists
abolitionize
abolitionized
abolitionizing
abolla
abollae
aboma
abomas
abomasa
abomasal
abomasi
abomasum
abomasus
abomasusi
abominability
abominable
abominableness
abominably
abominate
abominated
abominates
abominating
abomination
abominations
abominator
abominators
abomine
abondance
abonne
abonnement
aboon
aborad
aboral
aborally
abord
aboriginal
aboriginality
aboriginally
aboriginals
aboriginary
aborigine
aborigine's
aborigines
aborning
aborsement
aborsive
abort
aborted
aborter
aborters
aborticide
abortient
abortifacient
abortin
aborting
abortion
abortion's
abortional
abortionist
abortionists
abortions
abortive
abortively
abortiveness
abortogenic
aborts
abortus
abortuses
abos
abote
abouchement
aboudikro
abought
aboulia
aboulias
aboulic
abound
abounded
abounder
abounding
aboundingly
abounds
about
abouts
above
aboveboard
abovedeck
aboveground
abovementioned
aboveproof
aboves
abovesaid
abovestairs
abow
abox
abp
abr
abracadabra
abrachia
abrachias
abradable
abradant
abradants
abrade
abraded
abrader
abraders
abrades
abrading
abraham
abraid
abranchial
abranchialism
abranchian
abranchiate
abranchious
abrasax
abrase
abrased
abraser
abrash
abrasing
abrasiometer
abrasion
abrasion's
abrasions
abrasive
abrasively
abrasiveness
abrasives
abrastol
abraum
abraxas
abray
abrazite
abrazitic
abrazo
abrazos
abreact
abreacted
abreacting
abreaction
abreactions
abreacts
abreast
abreed
abrege
abreid
abrenounce
abrenunciate
abrenunciation
abreption
abret
abreuvoir
abri
abrico
abricock
abricot
abridgable
abridge
abridgeable
abridged
abridgedly
abridgement
abridgements
abridger
abridgers
abridges
abridging
abridgment
abridgments
abrim
abrin
abrine
abris
abristle
abroach
abroad
abrocome
abrogable
abrogate
abrogated
abrogates
abrogating
abrogation
abrogations
abrogative
abrogator
abrogators
abronia
abrood
abrook
abrosia
abrosias
abrotanum
abrotin
abrotine
abrupt
abruptedly
abrupter
abruptest
abruptio
abruption
abruptiones
abruptly
abruptness
abs
absampere
absarokite
abscam
abscess
abscessed
abscesses
abscessing
abscession
abscessroot
abscind
abscise
abscised
abscises
abscising
abscisins
abscision
absciss
abscissa
abscissa's
abscissae
abscissas
abscisse
abscissin
abscission
abscissions
absconce
abscond
absconded
abscondedly
abscondence
absconder
absconders
absconding
absconds
absconsa
abscoulomb
abscound
absee
abseil
abseiled
abseiling
abseils
absence
absence's
absences
absent
absentation
absented
absentee
absentee's
absenteeism
absentees
absenteeship
absenter
absenters
absentia
absenting
absently
absentment
absentminded
absentmindedly
absentmindedness
absentness
absents
absey
absfarad
abshenry
absinth
absinthe
absinthes
absinthial
absinthian
absinthiate
absinthiated
absinthiating
absinthic
absinthiin
absinthin
absinthine
absinthism
absinthismic
absinthium
absinthol
absinthole
absinths
absis
absist
absistos
absit
absmho
absohm
absoil
absolent
absolute
absolutely
absoluteness
absoluter
absolutes
absolutest
absolution
absolutions
absolutism
absolutist
absolutista
absolutistic
absolutistically
absolutists
absolutive
absolutization
absolutize
absolutory
absolvable
absolvatory
absolve
absolved
absolvent
absolver
absolvers
absolves
absolving
absolvitor
absolvitory
absonant
absonous
absorb
absorbability
absorbable
absorbance
absorbancy
absorbant
absorbed
absorbedly
absorbedness
absorbefacient
absorbencies
absorbency
absorbent
absorbents
absorber
absorbers
absorbing
absorbingly
absorbition
absorbs
absorbtion
absorpt
absorptance
absorptiometer
absorptiometric
absorption
absorption's
absorptional
absorptions
absorptive
absorptively
absorptiveness
absorptivity
absquatulate
absquatulation
abstain
abstained
abstainer
abstainers
abstaining
abstainment
abstains
abstemious
abstemiously
abstemiousness
abstention
abstentionism
abstentionist
abstentions
abstentious
absterge
absterged
abstergent
absterges
absterging
absterse
abstersion
abstersive
abstersiveness
abstertion
abstinence
abstinency
abstinent
abstinential
abstinently
abstort
abstr
abstract
abstractable
abstracted
abstractedly
abstractedness
abstracter
abstracters
abstractest
abstracting
abstraction
abstraction's
abstractional
abstractionism
abstractionist
abstractionists
abstractions
abstractitious
abstractive
abstractively
abstractiveness
abstractly
abstractness
abstractor
abstractor's
abstractors
abstracts
abstrahent
abstrict
abstricted
abstricting
abstriction
abstricts
abstrude
abstruse
abstrusely
abstruseness
abstrusenesses
abstruser
abstrusest
abstrusion
abstrusities
abstrusity
absume
absumption
absurd
absurder
absurdest
absurdism
absurdist
absurdities
absurdity
absurdity's
absurdly
absurdness
absurds
absurdum
absvolt
abt
abterminal
abthain
abthainrie
abthainry
abthanage
abtruse
abu
abubble
abucco
abuilding
abuleia
abulia
abulias
abulic
abulomania
abulyeit
abumbral
abumbrellar
abuna
abundance
abundances
abundancy
abundant
abundantly
abune
abura
aburabozu
aburagiri
aburban
aburst
aburton
abusable
abusage
abuse
abused
abusedly
abusee
abuseful
abusefully
abusefulness
abuser
abusers
abuses
abush
abusing
abusion
abusious
abusive
abusively
abusiveness
abut
abutilon
abutilons
abutment
abutments
abuts
abuttal
abuttals
abutted
abutter
abutter's
abutters
abutting
abuzz
abv
abvolt
abvolts
abwab
abwatt
abwatts
aby
abye
abyes
abying
abys
abysm
abysmal
abysmally
abysms
abyss
abyss's
abyssa
abyssal
abysses
abyssinia
abyssinian
abyssinians
abyssobenthonic
abyssolith
abyssopelagic
abyssus
ac
acacatechin
acacatechol
acacetin
acacia
acacias
acaciin
acacin
acacine
acad
academe
academes
academia
academial
academian
academias
academic
academical
academically
academicals
academician
academicians
academicianship
academicism
academics
academie
academies
academise
academised
academising
academism
academist
academite
academization
academize
academized
academizing
academy
academy's
acadia
acadialite
acadian
acaena
acajou
acajous
acalculia
acale
acaleph
acalepha
acalephae
acalephan
acalephe
acalephes
acalephoid
acalephs
acalycal
acalycine
acalycinous
acalyculate
acalyptrate
acampsia
acana
acanaceous
acanonical
acanth
acantha
acanthaceous
acanthad
acanthi
acanthial
acanthin
acanthine
acanthion
acanthite
acanthocarpous
acanthocephalan
acanthocephalous
acanthocladous
acanthodean
acanthodian
acanthoid
acanthological
acanthology
acantholysis
acanthoma
acanthomas
acanthon
acanthophorous
acanthopod
acanthopodous
acanthopomatous
acanthopore
acanthopteran
acanthopterous
acanthopterygian
acanthoses
acanthosis
acanthotic
acanthous
acanthus
acanthuses
acanthuthi
acapnia
acapnial
acapnias
acappella
acapsular
acapu
acapulco
acara
acarari
acardia
acardiac
acardite
acari
acarian
acariasis
acariatre
acaricidal
acaricide
acarid
acaridae
acaridan
acaridans
acaridean
acaridomatia
acaridomatium
acarids
acariform
acarine
acarines
acarinosis
acarocecidia
acarocecidium
acarodermatitis
acaroid
acarol
acarologist
acarology
acarophilous
acarophobia
acarotoxic
acarpellous
acarpelous
acarpous
acarus
acast
acatalectic
acatalepsia
acatalepsy
acataleptic
acatallactic
acatamathesia
acataphasia
acataposis
acatastasia
acatastatic
acate
acategorical
acater
acatery
acates
acatharsia
acatharsy
acatholic
acaudal
acaudate
acaudelescent
acaulescence
acaulescent
acauline
acaulose
acaulous
acc
acca
accable
accademia
accadian
acce
accede
acceded
accedence
acceder
acceders
accedes
acceding
accel
accelerable
accelerando
accelerant
accelerate
accelerated
acceleratedly
accelerates
accelerating
acceleratingly
acceleration
accelerations
accelerative
accelerator
acceleratorh
accelerators
acceleratory
accelerograph
accelerometer
accelerometer's
accelerometers
accend
accendibility
accendible
accensed
accension
accensor
accent
accented
accenting
accentless
accentor
accentors
accents
accentuable
accentual
accentuality
accentually
accentuate
accentuated
accentuates
accentuating
accentuation
accentuator
accentus
accept
acceptability
acceptable
acceptableness
acceptably
acceptance
acceptance's
acceptances
acceptancies
acceptancy
acceptant
acceptation
acceptavit
accepted
acceptedly
acceptee
acceptees
accepter
accepters
acceptilate
acceptilated
acceptilating
acceptilation
accepting
acceptingly
acceptingness
acception
acceptive
acceptor
acceptor's
acceptors
acceptress
accepts
accerse
accersition
accersitor
access
accessability
accessable
accessaries
accessarily
accessariness
accessary
accessaryship
accessed
accesses
accessibility
accessible
accessibleness
accessibly
accessing
accession
accession's
accessional
accessioned
accessioner
accessioning
accessions
accessit
accessive
accessively
accessless
accessor
accessor's
accessorial
accessories
accessorii
accessorily
accessoriness
accessorius
accessoriusorii
accessorize
accessorized
accessorizing
accessors
accessory
accessory's
acciaccatura
acciaccaturas
acciaccature
accidence
accidencies
accidency
accident
accidental
accidentalism
accidentalist
accidentality
accidentally
accidentalness
accidentals
accidentarily
accidentary
accidented
accidential
accidentiality
accidently
accidents
accidia
accidie
accidies
accinge
accinged
accinging
accipenser
accipient
accipiter
accipitral
accipitrary
accipitrine
accipter
accise
accismus
accite
acclaim
acclaimable
acclaimed
acclaimer
acclaimers
acclaiming
acclaims
acclamation
acclamations
acclamator
acclamatory
acclimatable
acclimatation
acclimate
acclimated
acclimatement
acclimates
acclimating
acclimation
acclimatisable
acclimatisation
acclimatise
acclimatised
acclimatiser
acclimatising
acclimatizable
acclimatization
acclimatize
acclimatized
acclimatizer
acclimatizes
acclimatizing
acclimature
acclinal
acclinate
acclivities
acclivitous
acclivity
acclivous
accloy
accoast
accoil
accolade
accoladed
accolades
accolated
accolent
accoll
accolle
accolled
accollee
accombination
accommodable
accommodableness
accommodate
accommodated
accommodately
accommodateness
accommodates
accommodating
accommodatingly
accommodatingness
accommodation
accommodational
accommodationist
accommodations
accommodative
accommodatively
accommodativeness
accommodator
accommodators
accomodate
accompanable
accompanied
accompanier
accompanies
accompaniment
accompaniment's
accompanimental
accompaniments
accompanist
accompanist's
accompanists
accompany
accompanying
accompanyist
accomplement
accompletive
accompli
accomplice
accomplices
accompliceship
accomplicity
accomplis
accomplish
accomplishable
accomplished
accomplisher
accomplishers
accomplishes
accomplishing
accomplishment
accomplishment's
accomplishments
accomplisht
accompt
accord
accordable
accordance
accordances
accordancy
accordant
accordantly
accordatura
accordaturas
accordature
accorded
accorder
accorders
according
accordingly
accordion
accordion's
accordionist
accordionists
accordions
accords
accorporate
accorporation
accost
accostable
accosted
accosting
accosts
accouche
accouchement
accouchements
accoucheur
accoucheurs
accoucheuse
accoucheuses
accounsel
account
accountability
accountable
accountableness
accountably
accountancy
accountant
accountant's
accountants
accountantship
accounted
accounter
accounters
accounting
accountment
accountrement
accounts
accouple
accouplement
accourage
accourt
accouter
accoutered
accoutering
accouterment
accouterments
accouters
accoutre
accoutred
accoutrement
accoutrements
accoutres
accoutring
accoy
accoyed
accoying
accra
accrease
accredit
accreditable
accreditate
accreditation
accreditations
accredited
accreditee
accrediting
accreditment
accredits
accrementitial
accrementition
accresce
accrescence
accrescendi
accrescendo
accrescent
accretal
accrete
accreted
accretes
accreting
accretion
accretion's
accretionary
accretions
accretive
accriminate
accroach
accroached
accroaching
accroachment
accroides
accruable
accrual
accruals
accrue
accrued
accruement
accruer
accrues
accruing
acct
accts
accubation
accubita
accubitum
accubitus
accueil
accultural
acculturate
acculturated
acculturates
acculturating
acculturation
acculturational
acculturationist
acculturative
acculturize
acculturized
acculturizing
accum
accumb
accumbency
accumbent
accumber
accumulable
accumulate
accumulated
accumulates
accumulating
accumulation
accumulations
accumulativ
accumulative
accumulatively
accumulativeness
accumulator
accumulator's
accumulators
accupy
accur
accuracies
accuracy
accurate
accurately
accurateness
accurre
accurse
accursed
accursedly
accursedness
accursing
accurst
accurtation
accus
accusable
accusably
accusal
accusals
accusant
accusants
accusation
accusation's
accusations
accusatival
accusative
accusatively
accusativeness
accusatives
accusator
accusatorial
accusatorially
accusatory
accusatrix
accusatrixes
accuse
accused
accuser
accusers
accuses
accusing
accusingly
accusive
accusor
accustom
accustomation
accustomed
accustomedly
accustomedness
accustoming
accustomize
accustomized
accustomizing
accustoms
ace
ace's
aceacenaphthene
aceanthrene
aceanthrenequinone
acecaffin
acecaffine
aceconitic
aced
acedia
acediamin
acediamine
acedias
acediast
acedy
aceite
aceituna
aceldama
aceldamas
acellular
acemila
acenaphthene
acenaphthenyl
acenaphthylene
acenesthesia
acensuada
acensuador
acentric
acentrous
aceologic
aceology
acephal
acephala
acephalan
acephali
acephalia
acephaline
acephalism
acephalist
acephalocyst
acephalous
acephalus
acepots
acequia
acequiador
acequias
aceraceous
acerate
acerated
acerathere
aceratosis
acerb
acerbate
acerbated
acerbates
acerbating
acerber
acerbest
acerbic
acerbically
acerbities
acerbitude
acerbity
acerbityacerose
acerbly
acerbophobia
acerdol
aceric
acerin
acerli
acerola
acerolas
acerose
acerous
acerra
acertannin
acerval
acervate
acervately
acervatim
acervation
acervative
acervose
acervuli
acervuline
acervulus
aces
acescence
acescency
acescent
acescents
aceship
acesodyne
acesodynous
acestoma
aceta
acetable
acetabula
acetabular
acetabularia
acetabuliferous
acetabuliform
acetabulous
acetabulum
acetabulums
acetacetic
acetal
acetaldehydase
acetaldehyde
acetaldehydrase
acetaldol
acetalization
acetalize
acetals
acetamid
acetamide
acetamidin
acetamidine
acetamido
acetamids
acetaminol
acetaminophen
acetanilid
acetanilide
acetanion
acetaniside
acetanisidide
acetanisidine
acetannin
acetarious
acetars
acetarsone
acetary
acetate
acetated
acetates
acetation
acetazolamide
acetbromamide
acetenyl
acethydrazide
acetiam
acetic
acetification
acetified
acetifier
acetifies
acetify
acetifying
acetimeter
acetimetric
acetimetry
acetin
acetine
acetins
acetite
acetize
acetla
acetmethylanilide
acetnaphthalide
acetoacetanilide
acetoacetate
acetoacetic
acetoamidophenol
acetoarsenite
acetobacter
acetobenzoic
acetobromanilide
acetochloral
acetocinnamene
acetoin
acetol
acetolysis
acetolytic
acetometer
acetometric
acetometrical
acetometrically
acetometry
acetomorphin
acetomorphine
acetonaemia
acetonaemic
acetonaphthone
acetonate
acetonation
acetone
acetonemia
acetonemic
acetones
acetonic
acetonitrile
acetonization
acetonize
acetonuria
acetonurometer
acetonyl
acetonylacetone
acetonylidene
acetophenetide
acetophenetidin
acetophenetidine
acetophenin
acetophenine
acetophenone
acetopiperone
acetopyrin
acetopyrine
acetosalicylic
acetose
acetosity
acetosoluble
acetostearin
acetothienone
acetotoluid
acetotoluide
acetotoluidine
acetous
acetoveratrone
acetoxim
acetoxime
acetoxyl
acetoxyls
acetoxyphthalide
acetphenetid
acetphenetidin
acetract
acettoluide
acetum
aceturic
acetyl
acetylacetonates
acetylacetone
acetylamine
acetylaminobenzene
acetylaniline
acetylasalicylic
acetylate
acetylated
acetylating
acetylation
acetylative
acetylator
acetylbenzene
acetylbenzoate
acetylbenzoic
acetylbiuret
acetylcarbazole
acetylcellulose
acetylcholine
acetylcholinesterase
acetylcholinic
acetylcyanide
acetylenation
acetylene
acetylenediurein
acetylenic
acetylenogen
acetylenyl
acetylfluoride
acetylglycin
acetylglycine
acetylhydrazine
acetylic
acetylid
acetylide
acetyliodide
acetylizable
acetylization
acetylize
acetylized
acetylizer
acetylizing
acetylmethylcarbinol
acetylperoxide
acetylphenol
acetylphenylhydrazine
acetylrosaniline
acetyls
acetylsalicylate
acetylsalicylic
acetylsalol
acetyltannin
acetylthymol
acetyltropeine
acetylurea
ach
achaenocarp
achaetous
achafe
achage
achalasia
achape
achaque
achar
acharne
acharnement
acharya
achate
achates
achatour
ache
acheat
achech
acheck
ached
acheer
acheilary
acheilia
acheilous
acheiria
acheirous
acheirus
achene
achenes
achenia
achenial
achenium
achenocarp
achenodia
achenodium
acher
acheron
acheronian
acherontic
aches
achesoun
achete
acheulean
acheweed
achier
achiest
achievability
achievable
achieve
achieved
achievement
achievement's
achievements
achiever
achievers
achieves
achieving
achigan
achilary
achill
achillea
achillean
achilleas
achillein
achilleine
achilles
achillize
achillobursitis
achillodynia
achilous
achime
achimenes
achiness
achinesses
aching
achingly
achiote
achiotes
achira
achirite
achkan
achlamydate
achlamydeous
achlorhydria
achlorhydric
achlorophyllous
achloropsia
achluophobia
achoke
acholia
acholias
acholic
acholous
acholuria
acholuric
achondrite
achondritic
achondroplasia
achondroplastic
achoo
achor
achordal
achordate
achras
achree
achroacyte
achrodextrin
achrodextrinase
achroglobin
achroiocythaemia
achroiocythemia
achroite
achroma
achromacyte
achromasia
achromat
achromate
achromatic
achromatically
achromaticity
achromatin
achromatinic
achromatisation
achromatise
achromatised
achromatising
achromatism
achromatizable
achromatization
achromatize
achromatized
achromatizing
achromatocyte
achromatolysis
achromatope
achromatophil
achromatophile
achromatophilia
achromatophilic
achromatopia
achromatopsia
achromatopsy
achromatosis
achromatous
achromats
achromaturia
achromia
achromic
achromobacter
achromoderma
achromophilous
achromotrichia
achromous
achronical
achronism
achronychous
achroodextrin
achroodextrinase
achroous
achropsia
achtehalber
achtel
achtelthaler
achter
achterveld
achuete
achy
achylia
achylous
achymia
achymous
acichlorid
acichloride
acicula
aciculae
acicular
acicularity
acicularly
aciculas
aciculate
aciculated
aciculum
aciculums
acid
acidaemia
acidanthera
acidemia
acidemias
acider
acidhead
acidheads
acidic
acidiferous
acidifiable
acidifiant
acidific
acidification
acidified
acidifier
acidifiers
acidifies
acidify
acidifying
acidimeter
acidimetric
acidimetrical
acidimetrically
acidimetry
acidite
acidities
acidity
acidize
acidized
acidizing
acidly
acidness
acidnesses
acidogenic
acidoid
acidology
acidolysis
acidometer
acidometry
acidophil
acidophile
acidophilic
acidophilous
acidophilus
acidoproteolytic
acidoses
acidosis
acidosteophyte
acidotic
acidproof
acids
acidulant
acidulate
acidulated
acidulates
acidulating
acidulation
acidulent
acidulous
acidulously
acidulousness
aciduria
acidurias
aciduric
acidy
acidyl
acier
acierage
acierate
acierated
acierates
acierating
acieration
acies
aciform
aciliate
aciliated
acinaceous
acinaces
acinacifoliate
acinacifolious
acinaciform
acinacious
acinacity
acinar
acinarious
acinary
acinetae
acinetan
acinetarian
acinetic
acinetiform
acinetinan
acing
acini
acinic
aciniform
acinose
acinotubular
acinous
acinuni
acinus
acipenser
acipenserid
acipenserine
acipenseroid
aciurgy
ack
ackee
ackees
acker
ackey
ackeys
ackman
ackmen
acknew
acknow
acknowing
acknowledge
acknowledgeable
acknowledged
acknowledgedly
acknowledgement
acknowledgements
acknowledger
acknowledgers
acknowledges
acknowledging
acknowledgment
acknowledgment's
acknowledgments
acknown
ackton
aclastic
acle
acleidian
acleistocardia
acleistous
aclidian
aclinal
aclinic
acloud
aclu
aclydes
aclys
acmaesthesia
acmatic
acme
acmes
acmesthesia
acmic
acmite
acne
acned
acneform
acneiform
acnemia
acnes
acnodal
acnode
acnodes
acoasm
acoasma
acocantherin
acock
acockbill
acocotl
acoelomate
acoelomatous
acoelomous
acoelous
acoenaesthesia
acoin
acoine
acold
acologic
acology
acolous
acoluthic
acolyctine
acolyte
acolytes
acolyth
acolythate
acolytus
acoma
acomia
acomous
aconative
acondylose
acondylous
acone
aconelline
aconic
aconin
aconine
aconital
aconite
aconites
aconitia
aconitic
aconitin
aconitine
aconitum
aconitums
acontia
acontium
aconuresis
acool
acop
acopic
acopon
acopyrin
acopyrine
acor
acorea
acoria
acorn
acorn's
acorned
acorns
acorus
acosmic
acosmism
acosmist
acosmistic
acost
acotyledon
acotyledonous
acouasm
acouchi
acouchy
acoumeter
acoumetry
acounter
acouometer
acouophonia
acoup
acoupa
acoupe
acousma
acousmas
acousmata
acousmatic
acoustic
acoustical
acoustically
acoustician
acousticolateral
acousticophobia
acoustics
acoustoelectric
acpt
acquaint
acquaintance
acquaintance's
acquaintances
acquaintanceship
acquaintanceships
acquaintancy
acquaintant
acquainted
acquaintedness
acquainting
acquaints
acquent
acquereur
acquest
acquests
acquiesce
acquiesced
acquiescement
acquiescence
acquiescency
acquiescent
acquiescently
acquiescer
acquiesces
acquiescing
acquiescingly
acquiesence
acquiet
acquirability
acquirable
acquire
acquired
acquirement
acquirements
acquirenda
acquirer
acquirers
acquires
acquiring
acquisible
acquisita
acquisite
acquisited
acquisition
acquisition's
acquisitional
acquisitions
acquisitive
acquisitively
acquisitiveness
acquisitor
acquisitum
acquist
acquit
acquital
acquitment
acquits
acquittal
acquittals
acquittance
acquitted
acquitter
acquitting
acquophonia
acracy
acraein
acraldehyde
acrania
acranial
acraniate
acrasia
acrasias
acrasin
acrasins
acraspedote
acrasy
acratia
acraturesis
acrawl
acraze
acre
acre's
acreable
acreage
acreages
acreak
acream
acred
acreman
acremen
acres
acrestaff
acrid
acridan
acridane
acrider
acridest
acridian
acridic
acridid
acridin
acridine
acridines
acridinic
acridinium
acridities
acridity
acridly
acridness
acridone
acridonium
acridophagus
acridyl
acriflavin
acriflavine
acrimonies
acrimonious
acrimoniously
acrimoniousness
acrimony
acrindolin
acrindoline
acrinyl
acrisia
acrisy
acrita
acritan
acrite
acritical
acritochromacy
acritol
acritude
acrity
acroaesthesia
acroama
acroamata
acroamatic
acroamatical
acroamatics
acroanesthesia
acroarthritis
acroasis
acroasphyxia
acroataxia
acroatic
acrobacies
acrobacy
acrobat
acrobat's
acrobatholithic
acrobatic
acrobatical
acrobatically
acrobatics
acrobatism
acrobats
acroblast
acrobryous
acrobystitis
acrocarpous
acrocentric
acrocephalia
acrocephalic
acrocephalous
acrocephaly
acrochordon
acrock
acroconidium
acrocontracture
acrocoracoid
acrocyanosis
acrocyst
acrodactyla
acrodactylum
acrodermatitis
acrodont
acrodontism
acrodonts
acrodrome
acrodromous
acrodynia
acroesthesia
acrogamous
acrogamy
acrogen
acrogenic
acrogenous
acrogenously
acrogens
acrography
acrogynae
acrogynous
acrolein
acroleins
acrolith
acrolithan
acrolithic
acroliths
acrologic
acrologically
acrologies
acrologism
acrologue
acrology
acromania
acromastitis
acromegalia
acromegalic
acromegalies
acromegaly
acromelalgia
acrometer
acromia
acromial
acromicria
acromimia
acromioclavicular
acromiocoracoid
acromiodeltoid
acromiohumeral
acromiohyoid
acromion
acromioscapular
acromiosternal
acromiothoracic
acromonogrammatic
acromphalus
acromyodian
acromyodic
acromyodous
acromyotonia
acromyotonus
acron
acronal
acronarcotic
acroneurosis
acronic
acronical
acronically
acronichal
acronichally
acronomy
acronyc
acronycal
acronycally
acronych
acronychal
acronychally
acronychous
acronyctous
acronym
acronym's
acronymic
acronymically
acronymize
acronymized
acronymizing
acronymous
acronyms
acronyx
acrook
acroparalysis
acroparesthesia
acropathology
acropathy
acropetal
acropetally
acrophobia
acrophonetic
acrophonic
acrophonically
acrophonies
acrophony
acropodia
acropodium
acropoleis
acropolis
acropolises
acropolitan
acropore
acrorhagus
acrorrheuma
acrosarc
acrosarca
acrosarcum
acroscleriasis
acroscleroderma
acroscopic
acrose
acrosome
acrosomes
acrosphacelus
acrospire
acrospired
acrospiring
acrospore
acrosporous
across
acrostic
acrostical
acrostically
acrostichal
acrostichic
acrostichoid
acrosticism
acrostics
acrostolia
acrostolion
acrostolium
acrotarsial
acrotarsium
acroteleutic
acroter
acroteral
acroteria
acroterial
acroteric
acroterion
acroterium
acroterteria
acrotic
acrotism
acrotisms
acrotomous
acrotrophic
acrotrophoneurosis
acryl
acrylaldehyde
acrylate
acrylates
acrylic
acrylics
acrylonitrile
acrylyl
act
acta
actability
actable
actaeon
acted
actg
actification
actifier
actify
actin
actinal
actinally
actinautographic
actinautography
actine
actinenchyma
acting
actings
actinia
actiniae
actinian
actinians
actiniarian
actinias
actinic
actinical
actinically
actinide
actinides
actiniferous
actiniform
actinine
actiniochrome
actiniohematin
actinism
actinisms
actinium
actiniums
actinobaccilli
actinobacilli
actinobacillosis
actinobacillotic
actinobacillus
actinoblast
actinobranch
actinobranchia
actinocarp
actinocarpic
actinocarpous
actinochemical
actinochemistry
actinocrinid
actinocrinite
actinocutitis
actinodermatitis
actinodielectric
actinodrome
actinodromous
actinoelectric
actinoelectrically
actinoelectricity
actinogonidiate
actinogram
actinograph
actinographic
actinography
actinoid
actinoids
actinolite
actinolitic
actinologous
actinologue
actinology
actinomere
actinomeric
actinometer
actinometers
actinometric
actinometrical
actinometricy
actinometry
actinomorphic
actinomorphous
actinomorphy
actinomyces
actinomycese
actinomycesous
actinomycestal
actinomycetal
actinomycete
actinomycetous
actinomycin
actinomycoma
actinomycosis
actinomycosistic
actinomycotic
actinon
actinoneuritis
actinons
actinophone
actinophonic
actinophore
actinophorous
actinophryan
actinopod
actinopraxis
actinopteran
actinopterous
actinopterygian
actinopterygious
actinoscopy
actinosoma
actinosome
actinost
actinostereoscopy
actinostomal
actinostome
actinotherapeutic
actinotherapeutics
actinotherapy
actinotoxemia
actinotrichium
actinotrocha
actinouranium
actinozoal
actinozoan
actinozoon
actins
actinula
actinulae
action
action's
actionability
actionable
actionably
actional
actionary
actioner
actiones
actionist
actionize
actionized
actionizing
actionless
actions
actious
activable
activate
activated
activates
activating
activation
activations
activator
activator's
activators
active
actively
activeness
actives
activin
activism
activisms
activist
activist's
activistic
activists
activital
activities
activity
activity's
activize
activized
activizing
actless
actomyosin
acton
actor
actor's
actorish
actors
actorship
actory
actos
actress
actress's
actresses
actressy
acts
actu
actual
actualisation
actualise
actualised
actualising
actualism
actualist
actualistic
actualities
actuality
actualization
actualize
actualized
actualizes
actualizing
actually
actualness
actuals
actuarial
actuarially
actuarian
actuaries
actuary
actuaryship
actuate
actuated
actuates
actuating
actuation
actuator
actuator's
actuators
actuose
acture
acturience
actus
actutate
acuaesthesia
acuate
acuating
acuation
acuchi
acuclosure
acuductor
acuerdo
acuerdos
acuesthesia
acuities
acuity
aculea
aculeae
aculeate
aculeated
aculei
aculeiform
aculeolate
aculeolus
aculeus
acumble
acumen
acumens
acuminate
acuminated
acuminating
acumination
acuminose
acuminous
acuminulate
acupress
acupressure
acupunctuate
acupunctuation
acupuncturation
acupuncturator
acupuncture
acupunctured
acupuncturing
acupuncturist
acupuncturists
acurative
acus
acusection
acusector
acushla
acustom
acutance
acutances
acutangular
acutate
acute
acutely
acutenaculum
acuteness
acuter
acutes
acutest
acutiator
acutifoliate
acutilingual
acutilobate
acutiplantar
acutish
acutograve
acutonodose
acutorsion
acxoyatl
acy
acyanoblepsia
acyanopsia
acyclic
acyclically
acyesis
acyetic
acyl
acylal
acylamido
acylamidobenzene
acylamino
acylase
acylate
acylated
acylates
acylating
acylation
acylogen
acyloin
acyloins
acyloxy
acyloxymethane
acyls
acyrological
acyrology
acystia
ad
adactyl
adactylia
adactylism
adactylous
adad
adage
adages
adagial
adagietto
adagiettos
adagio
adagios
adagissimo
adagy
adalat
adalid
adam
adamance
adamances
adamancies
adamancy
adamant
adamantean
adamantine
adamantinoma
adamantly
adamantness
adamantoblast
adamantoblastoma
adamantoid
adamantoma
adamants
adamas
adambulacral
adamellite
adamine
adamite
adams
adamsite
adamsites
adance
adangle
adansonia
adapid
adapt
adaptability
adaptable
adaptableness
adaptably
adaptation
adaptation's
adaptational
adaptationally
adaptations
adaptative
adapted
adaptedness
adapter
adapters
adapting
adaption
adaptional
adaptionism
adaptions
adaptitude
adaptive
adaptively
adaptiveness
adaptivity
adaptometer
adaptor
adaptorial
adaptors
adapts
adar
adarbitrium
adarme
adarticulation
adat
adati
adatis
adatom
adaty
adaunt
adaw
adawe
adawlut
adawn
adaxial
aday
adays
adazzle
adc
adcon
adcons
adcraft
add
adda
addability
addable
addax
addaxes
addda
addebted
added
addedly
addeem
addend
addenda
addends
addendum
addendums
adder
adderbolt
adderfish
adders
adderspit
adderwort
addibility
addible
addice
addicent
addict
addicted
addictedness
addicting
addiction
addiction's
addictions
addictive
addictively
addictiveness
addictives
addicts
addiment
adding
addio
addis
addison
addita
additament
additamentary
additiment
addition
addition's
additional
additionally
additionary
additionist
additions
addititious
additive
additive's
additively
additives
additivity
additory
additum
additur
addle
addlebrain
addlebrained
addled
addlehead
addleheaded
addleheadedly
addleheadedness
addlement
addleness
addlepate
addlepated
addlepatedness
addleplot
addles
addling
addlings
addlins
addn
addnl
addoom
addorsed
addossed
addr
address
addressability
addressable
addressed
addressee
addressee's
addressees
addresser
addressers
addresses
addressful
addressing
addressor
addrest
adds
adduce
adduceable
adduced
adducent
adducer
adducers
adduces
adducible
adducing
adduct
adducted
adducting
adduction
adductive
adductor
adductors
adducts
addulce
ade
adead
adeem
adeemed
adeeming
adeems
adeep
adelantado
adelantados
adelante
adelarthrosomatous
adelaster
adeling
adelite
adelocerous
adelocodonic
adelomorphic
adelomorphous
adelopod
adelphic
adelphogamy
adelpholite
adelphophagy
adelphous
ademonist
adempt
adempted
ademption
aden
adenalgia
adenalgy
adenase
adenasthenia
adendric
adendritic
adenectomies
adenectomy
adenectopia
adenectopic
adenemphractic
adenemphraxis
adenia
adeniform
adenin
adenine
adenines
adenitis
adenitises
adenization
adenoacanthoma
adenoblast
adenocancroid
adenocarcinoma
adenocarcinomas
adenocarcinomata
adenocarcinomatous
adenocele
adenocellulitis
adenochondroma
adenochondrosarcoma
adenochrome
adenocyst
adenocystoma
adenocystomatous
adenodermia
adenodiastasis
adenodynia
adenofibroma
adenofibrosis
adenogenesis
adenogenous
adenographer
adenographic
adenographical
adenography
adenohypersthenia
adenohypophyseal
adenohypophysial
adenohypophysis
adenoid
adenoidal
adenoidectomies
adenoidectomy
adenoidism
adenoiditis
adenoids
adenoliomyofibroma
adenolipoma
adenolipomatosis
adenologaditis
adenological
adenology
adenolymphocele
adenolymphoma
adenoma
adenomalacia
adenomas
adenomata
adenomatome
adenomatous
adenomeningeal
adenometritis
adenomycosis
adenomyofibroma
adenomyoma
adenomyxoma
adenomyxosarcoma
adenoncus
adenoneural
adenoneure
adenopathy
adenopharyngeal
adenopharyngitis
adenophlegmon
adenophore
adenophoreus
adenophorous
adenophthalmia
adenophyllous
adenophyma
adenopodous
adenosarcoma
adenosarcomas
adenosarcomata
adenosclerosis
adenose
adenoses
adenosine
adenosis
adenostemonous
adenotome
adenotomic
adenotomy
adenotyphoid
adenotyphus
adenous
adenoviral
adenovirus
adenoviruses
adenyl
adenylic
adenylpyrophosphate
adenyls
adephaga
adephagan
adephagia
adephagous
adeps
adept
adepter
adeptest
adeption
adeptly
adeptness
adepts
adeptship
adequacies
adequacy
adequate
adequately
adequateness
adequation
adequative
adermia
adermin
adermine
adesmy
adespota
adespoton
adessenarian
adessive
adeste
adet
adeuism
adevism
adfected
adffroze
adffrozen
adfiliate
adfix
adfluxion
adfreeze
adfreezing
adfroze
adfrozen
adglutinate
adhaka
adhamant
adharma
adherant
adhere
adhered
adherence
adherences
adherency
adherend
adherends
adherent
adherent's
adherently
adherents
adherer
adherers
adheres
adherescence
adherescent
adhering
adhesion
adhesional
adhesions
adhesive
adhesive's
adhesively
adhesivemeter
adhesiveness
adhesives
adhibit
adhibited
adhibiting
adhibition
adhibits
adhocracy
adhort
adiabat
adiabatic
adiabatically
adiabolist
adiactinic
adiadochokinesia
adiadochokinesis
adiadokokinesi
adiadokokinesia
adiagnostic
adiamorphic
adiamorphism
adiantiform
adiantum
adiaphanous
adiaphanousness
adiaphon
adiaphonon
adiaphora
adiaphoral
adiaphoresis
adiaphoretic
adiaphorism
adiaphorist
adiaphoristic
adiaphorite
adiaphoron
adiaphorous
adiaphory
adiapneustia
adiate
adiated
adiathermal
adiathermancy
adiathermanous
adiathermic
adiathetic
adiating
adiation
adibasi
adicity
adience
adient
adieu
adieus
adieux
adighe
adight
adigranth
adinidan
adinole
adinvention
adion
adios
adipate
adipescent
adiphenine
adipic
adipinic
adipocele
adipocellulose
adipocere
adipoceriform
adipocerite
adipocerous
adipocyte
adipofibroma
adipogenic
adipogenous
adipoid
adipolysis
adipolytic
adipoma
adipomata
adipomatous
adipometer
adiponitrile
adipopectic
adipopexia
adipopexic
adipopexis
adipose
adiposeness
adiposes
adiposis
adiposities
adiposity
adiposogenital
adiposuria
adipous
adipsia
adipsic
adipsous
adipsy
adipyl
adit
adital
aditio
adits
aditus
adj
adjacence
adjacencies
adjacency
adjacent
adjacently
adjag
adject
adjection
adjectional
adjectitious
adjectival
adjectivally
adjective
adjective's
adjectively
adjectives
adjectivism
adjectivitis
adjiga
adjiger
adjoin
adjoinant
adjoined
adjoinedly
adjoiner
adjoining
adjoiningness
adjoins
adjoint
adjoints
adjourn
adjournal
adjourned
adjourning
adjournment
adjournments
adjourns
adjoust
adjt
adjudge
adjudgeable
adjudged
adjudger
adjudges
adjudging
adjudgment
adjudicata
adjudicate
adjudicated
adjudicates
adjudicating
adjudication
adjudication's
adjudications
adjudicative
adjudicator
adjudicators
adjudicatory
adjudicature
adjugate
adjument
adjunct
adjunct's
adjunction
adjunctive
adjunctively
adjunctly
adjuncts
adjuration
adjurations
adjuratory
adjure
adjured
adjurer
adjurers
adjuresç
adjuring
adjuror
adjurors
adjust
adjustability
adjustable
adjustably
adjustage
adjustation
adjusted
adjuster
adjusters
adjusting
adjustive
adjustment
adjustment's
adjustmental
adjustments
adjustor
adjustor's
adjustores
adjustoring
adjustors
adjusts
adjutage
adjutancies
adjutancy
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    find_anagrams('apple')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 110, in find_anagrams
    print(line)
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('apple')
&c
'd
'em
'll
'm
'mid
'midst
'mongst
'prentice
're
's
'sblood
'sbodikins
'sdeath
'sfoot
'sheart
'shun
'slid
'slife
'slight
'snails
'strewth
't
'til
'tis
'twas
'tween
'twere
'twill
'twixt
'twould
'un
've
1080
10th
1st
2
2nd
3rd
4th
5th
6th
7th
8th
9th
a
a'
a's
a/c
a1
aa
aaa
aah
aahed
aahing
aahs
aal
aalii
aaliis
aals
aam
aardvark
aardvarks
aardwolf
aardwolves
aargh
aaron
aaronic
aarrgh
aarrghh
aas
aasvogel
aasvogels
ab
aba
abac
abaca
abacas
abacate
abacaxi
abacay
abaci
abacinate
abacination
abacisci
abaciscus
abacist
aback
abacli
abacot
abacterial
abactinal
abactinally
abaction
abactor
abaculi
abaculus
abacus
abacuses
abada










































Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    find_anagrams('apple')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 110, in find_anagrams
    print(line)
KeyboardInterrupt
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams(str1)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    find_anagrams(str1)
NameError: name 'str1' is not defined
>>> find_anagrams('apple')
&c
[]
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('apple')
&c
'd
'em
'll
'm
'mid
'midst
'mongst
'prentice
're
's
'sblood
'sbodikins
'sdeath
'sfoot
'sheart
'shun
'slid
'slife
'slight
'snails
'strewth
't
'til
'tis
'twas
'tween
'twere
'twill
'twixt
'twould
'un
've
1080
10th
1st
2
2nd
3rd
4th
5th
6th
7th
8th
9th
a
a'
a's
a/c
a1
aa
aaa
aah
aahed
aahing
aahs
aal
aalii
aaliis
aals
aam
aardvark
aardvarks
aardwolf
aardwolves
aargh
aaron
aaronic
aarrgh
aarrghh
aas
aasvogel
aasvogels
ab
aba
abac
abaca
abacas
abacate
abacaxi
abacay
abaci
abacinate
abacination
abacisci
abaciscus
abacist
aback
abacli
abacot
abacterial
abactinal
abactinally
abaction
abactor
abaculi
abaculus
abacus
abacuses
abada
[]
>>> find_anagrams('abada')
&c
'd
'em
'll
'm
'mid
'midst
'mongst
'prentice
're
's
'sblood
'sbodikins
'sdeath
'sfoot
'sheart
'shun
'slid
'slife
'slight
'snails
'strewth
't
'til
'tis
'twas
'tween
'twere
'twill
'twixt
'twould
'un
've
1080
10th
1st
2
2nd
3rd
4th
5th
6th
7th
8th
9th
a
a'
a's
a/c
a1
aa
aaa
aah
aahed
aahing
aahs
aal
aalii
aaliis
aals
aam
aardvark
aardvarks
aardwolf
aardwolves
aargh
aaron
aaronic
aarrgh
aarrghh
aas
aasvogel
aasvogels
ab
aba
abac
abaca
abacas
abacate
abacaxi
abacay
abaci
abacinate
abacination
abacisci
abaciscus
abacist
aback
abacli
abacot
abacterial
abactinal
abactinally
abaction
abactor
abaculi
abaculus
abacus
abacuses
abada
['abada']
>>> find_anagrams('cabuas')
&c
'd
'em
'll
'm
'mid
'midst
'mongst
'prentice
're
's
'sblood
'sbodikins
'sdeath
'sfoot
'sheart
'shun
'slid
'slife
'slight
'snails
'strewth
't
'til
'tis
'twas
'tween
'twere
'twill
'twixt
'twould
'un
've
1080
10th
1st
2
2nd
3rd
4th
5th
6th
7th
8th
9th
a
a'
a's
a/c
a1
aa
aaa
aah
aahed
aahing
aahs
aal
aalii
aaliis
aals
aam
aardvark
aardvarks
aardwolf
aardwolves
aargh
aaron
aaronic
aarrgh
aarrghh
aas
aasvogel
aasvogels
ab
aba
abac
abaca
abacas
abacate
abacaxi
abacay
abaci
abacinate
abacination
abacisci
abaciscus
abacist
aback
abacli
abacot
abacterial
abactinal
abactinally
abaction
abactor
abaculi
abaculus
abacus
abacuses
abada
['abacus']
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('apple')
['appel', 'apple', 'pepla']
>>> find_anagrams('bada')
[]
>>> find_anagrams('hello')
['hello']
>>> find_anagrams('silent')
['enlist', 'inlets', 'listen', 'silent', 'slinte', 'tinsel']
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('happy')
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    find_anagrams('happy')
  File "/Users/janechoi/Documents/lab14-mostOfTheFunctions.py", line 108, in find_anagrams
    text2.close()
AttributeError: 'str' object has no attribute 'close'
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('silent')
['enlist', 'inlets', 'listen', 'silent', 'slinte', 'tinsel']
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> find_anagrams('happy')
['happy']
>>> find_anagrams('child')
['child']
>>> find_anagrams('chil')
['chil', 'lich']
>>> find_anagrams('like')
['kiel', 'like']
>>> 
======= RESTART: /Users/janechoi/Documents/lab14-printer_of_ngrams.py =======
How many characters should I display at a time?3
What file should I display?h
There was an error working with that file. Please choose a different filename.
What file should I display?ra
There was an error working with that file. Please choose a different filename.
What file should I display?ls
There was an error working with that file. Please choose a different filename.
What file should I display?lal'
There was an error working with that file. Please choose a different filename.
What file should I display?ldkf
There was an error working with that file. Please choose a different filename.
What file should I display?hanlon.txt
Nev
er 
att
rib
ute
 to
 ma
lic
e t
hat
 wh
ich
 is
 ad
equ
ate
ly 
exp
lai
ned
 by
 st
upi
dit
y.

>>> 
======= RESTART: /Users/janechoi/Documents/lab14-mostOfTheFunctions.py =======
>>> 

