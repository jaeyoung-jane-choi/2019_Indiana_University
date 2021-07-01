Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: /Users/janechoi/Documents/read05-transcript.py ==========
Simulation of a conversation with a candidate.
Will you vote for me?
no
Will you vote for me?
no
Will you vote for me?
nono
Will you vote for me?
no
Will you vote for me?
yeS
Will you vote for me?

Will you vote for me?
yes
Will you vote for me?
yes
Will you vote for me?
Yes
Thank you.
>>> 
========== RESTART: /Users/janechoi/Documents/read05-transcript.py ==========
Simulation of a conversation with a candidate.
Will you vote for me?
yes
Will you vote for me?

========== RESTART: /Users/janechoi/Documents/read05-transcript.py ==========
Simulation of a conversation with a candidate.
Will you vote for me?
yes
Will you vote for me?
yes
Will you vote for me?

========== RESTART: /Users/janechoi/Documents/read05-transcript.py ==========
Simulation of a conversation with a candidate.
Will you vote for me?
yes
Thank you.
>>> 
========== RESTART: /Users/janechoi/Documents/read05-transcript.py ==========
>>> clean_string(...A...Dkk..z?!)
SyntaxError: invalid syntax
>>> clean_string("...A...Dkk..z?!")
'a...dkk..z'
>>> 
========== RESTART: /Users/janechoi/Documents/read05-transcript.py ==========
Simulation of a conversation with a candidate.
Will you vote for me?
no
Will you vote for me?
....yES?
Thank you.
>>> 
========== RESTART: /Users/janechoi/Documents/read05-transcript.py ==========
>>> gauss(1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    gauss(1)
TypeError: gauss() takes 0 positional arguments but 1 was given
>>> gauss()
5050
>>> TRUE
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    TRUE
NameError: name 'TRUE' is not defined
>>> datatype(True)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    datatype(True)
NameError: name 'datatype' is not defined
>>> type(True)
<class 'bool'>
>>> 'type'.isalpha()
True
>>> '1type'[1].isalpha()
True
>>> '1type'[1]
't'
>>> '1type'[0].isalpha()
False
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_letter('121212a')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    contains_letter('121212a')
  File "/Users/janechoi/Documents/pa05-functions.py", line 17, in contains_letter
    final_result == print(True)
NameError: name 'final_result' is not defined
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> final_result('11a')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    final_result('11a')
NameError: name 'final_result' is not defined
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> final_result('aa')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    final_result('aa')
NameError: name 'final_result' is not defined
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> final_result('11a')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    final_result('11a')
NameError: name 'final_result' is not defined
>>> contains_letter('121212a')
True
>>> contains_letter('121212')
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_letter('121212a')
True
>>> contains_letter('121212')
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_letter('121212a')
False
False
False
False
False
False
True
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_letter('121212a')
False
False
False
False
False
False
True
>>> contains_letter('1a21212a')
False
True
False
False
False
False
False
True
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_letter('121212a')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    contains_letter('121212a')
  File "/Users/janechoi/Documents/pa05-functions.py", line 20, in contains_letter
    if result == T:
NameError: name 'T' is not defined
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_letter('121212a')

============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_letter('121212a')
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False

False
False
False
False

False
False
False

False
False
False
False
False
False

False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    contains_letter('121212a')
  File "/Users/janechoi/Documents/pa05-functions.py", line 22, in contains_letter
    print(True_result)
KeyboardInterrupt
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_letter('aaa111')
True
>>>  contains_letter('11')
SyntaxError: unexpected indent
>>> contains_letter('11')

============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_letter('11')
False
>>> contains_letter('11a')
True
>>> contains_letter('1a1')
True
>>> contains_letter('11aaa')
True
>>> contains_letter('11/')
False
>>> contains_letter('aaa')
True
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_only_digits('')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    contains_only_digits('')
  File "/Users/janechoi/Documents/pa05-functions.py", line 42, in contains_only_digits
    while (string[index]<len(string)):
IndexError: string index out of range
>>> contains_only_digits('12')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    contains_only_digits('12')
  File "/Users/janechoi/Documents/pa05-functions.py", line 42, in contains_only_digits
    while (string[index]<len(string)):
TypeError: '<' not supported between instances of 'str' and 'int'
>>> contains_only_digits('a')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    contains_only_digits('a')
  File "/Users/janechoi/Documents/pa05-functions.py", line 42, in contains_only_digits
    while (string[index]<len(string)):
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_only_digits('123')
True
>>> contains_only_digits('')
False
>>> contains_only_digits('one')
False
>>> contains_only_digits('12one')
True
>>> 'string' in '123'
False
>>> contains_only_digits('12,one')
True
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_only_digits('12one')
False
>>> contains_only_digits('12,one')
False
>>> contains_only_digits('12')
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_only_digits('12one')
False
>>> contains_only_digits('12')
True
>>> contains_only_digits('12, 12')
False
>>> contains_only_digits('')
True
>>> 'a' == 'b'
False
>>> 'a' > 'b'
False
>>> 'b'>'a'
True
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> 
================= RESTART: /Users/janechoi/Documents/adf.py =================
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:
>>> 
================= RESTART: /Users/janechoi/Documents/adf.py =================
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:
unspecified
>>> 
================= RESTART: /Users/janechoi/Documents/adf.py =================
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:
Should we add Anti-reflective Coating?:N
Should we add Polarized Filter Coating?:Y
Should we add Scratch Resistant Coating?:y
Should we add Mirror Coating?:n
unspecified
Coating(s):nPolarized Filter CoatingSratch Resistant Coatingn
>>> 
================= RESTART: /Users/janechoi/Documents/adf.py =================
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:
Should we add Anti-reflective Coating?:Y
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:N

Coating(s):Polarized Filter Coatingnn
>>> 
================= RESTART: /Users/janechoi/Documents/adf.py =================
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:
Should we add Anti-reflective Coating?:y
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:N

Coating(s):Anti-reflective CoatingPolarized Filter Coating
>>> 
================= RESTART: /Users/janechoi/Documents/adf.py =================
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:nd
Should we add Anti-reflective Coating?:y
Should we add Polarized Filter Coating?:Y
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:N
nd
Coating(s):
Anti-reflective Coating
Polarized Filter Coating


>>> 'heelo'.upper()
'HEELO'
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:hihihello
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:y
Should we add Polarized Filter Coating?:N
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:N
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?white
The tint color is not available. We'll make them Dark Gray.
Your order for sunglasses is ready:
--------------------------------------
Brand name:hihihello.
Coating(s):
Anti-reflective Coating



Tint color:dark gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:hello
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:N
Should we add Scratch Resistant Coating?:Y
Should we add Mirror Coating?:y
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?dark GRAY
Your order for sunglasses is ready:
--------------------------------------
Brand name:hello.
Coating(s):


Sratch Resistant Coating
Mirror Coating
Tint color:dark gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:ad
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:y
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:y
Should we add Mirror Coating?:y
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?TEal
Your order for sunglasses is ready:
--------------------------------------
Brand name:ad.
Coating(s):
Anti-reflective Coating

Sratch Resistant Coating
Mirror Coating
Tint color:teal.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:
Should we add Polarized Filter Coating?:
Should we add Scratch Resistant Coating?:
Should we add Mirror Coating?:
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?
The tint color is not available. We'll make them Dark Gray.
Your order for sunglasses is ready:
--------------------------------------
Brand name:unspecified.
Coating(s):




Tint color:dark gray.
--------------------------------------
>>> 
================= RESTART: /Users/janechoi/Documents/adf.py =================
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:
================= RESTART: /Users/janechoi/Documents/adf.py =================
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:y
Coating(s)
>>> 
================= RESTART: /Users/janechoi/Documents/adf.py =================
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:y
Should we add Mirror Coating?:n
Coating(s)
Traceback (most recent call last):
  File "/Users/janechoi/Documents/adf.py", line 22, in <module>
    print(user_input2 = 'Polarized Filter Coating')
TypeError: 'user_input2' is an invalid keyword argument for print()
>>> 
================= RESTART: /Users/janechoi/Documents/adf.py =================
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:y
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:y
Should we add Mirror Coating?:n
Coating(s)
Anti-reflective Coating
Sratch Resistant Coating
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name: hello
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:y
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:y
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?amBEr
Your order for sunglasses is ready:
--------------------------------------
Brand name: hello.
Coating(s)
Anti-reflective Coating
Mirror Coating
Tint color:amber.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:adf
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:n
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?hwil
The tint color is not available. We'll make them Dark Gray.
Your order for sunglasses is ready:
--------------------------------------
Brand name:adf.
Coating(s)
Tint color:dark gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:adf
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:N
Should we add Mirror Coating?:N
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?green
Your order for sunglasses is ready:
--------------------------------------
Brand name:adf.
Coating(s):
.
Tint color:green.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:m
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:y
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:y
Should we add Mirror Coating?:y
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?y
The tint color is not available. We'll make them Dark Gray.
Your order for sunglasses is ready:
--------------------------------------
Brand name:m.
Coating(s):
Anti-reflective Coating
Polarized Filter Coating
Sratch Resistant Coating
Mirror Coating
.
Tint color:dark gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:nws
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:n
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?green
Your order for sunglasses is ready:
--------------------------------------
Brand name:nws.
Coating(s):
Polarized Filter Coating
Tint color:green.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:ㅁㅇ
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:y
Should we add Mirror Coating?:y
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?n
The tint color is not available. We'll make them Dark Gray.
Your order for sunglasses is ready:
--------------------------------------
Brand name:ㅁㅇ.
Coating(s):
Polarized Filter Coating
Sratch Resistant Coating
Mirror Coating
No coating
Tint color:dark gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:adf
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:n
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?amber
Your order for sunglasses is ready:
--------------------------------------
Brand name:adf.
Coating(s):
Tint color:amber.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:n
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:n
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?teAl
Your order for sunglasses is ready:
--------------------------------------
Brand name:n.
Coating(s):
Tint color:teal.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:nan
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:n
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?green
Your order for sunglasses is ready:
--------------------------------------
Brand name:nan.
Coating(s):
No coating
Tint color:green.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:newbrand
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:y
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:y
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green? white
The tint color is not available. We'll make them Dark Gray.
Your order for sunglasses is ready:
--------------------------------------
Brand name:newbrand.
Coating(s):
Anti-reflective Coating
Polarized Filter Coating
Mirror Coating
Tint color:Dark Gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:new
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:y
Should we add Mirror Coating?:n
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?Teal
Your order for sunglasses is ready:
--------------------------------------
Brand name:new.
Coating(s):
Polarized Filter Coating
Sratch Resistant Coating
Tint color:teal.
--------------------------------------
>>> 'teal'[0].upper()
'T'
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name: ysl
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:y
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green? Dark GRAY
The tint color is not available. We'll make them Dark Gray.
Your order for sunglasses is ready:
--------------------------------------
Brand name: ysl.
Coating(s):
Polarized Filter Coating
Mirror Coating
Tint color:Dark Gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name: ysl
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:n
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?DarkGraY
The tint color is not available. We'll make them Dark Gray.
Your order for sunglasses is ready:
--------------------------------------
Brand name: ysl.
Coating(s):
No coating
Tint color:Dark Gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:ysl
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:y
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?darkGray
Your order for sunglasses is ready:
--------------------------------------
Brand name:ysl.
Coating(s):
Mirror Coating
Tint color:darkgray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:ysl
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:n
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?Dark Gray
Your order for sunglasses is ready:
--------------------------------------
Brand name:ysl.
Coating(s):
No coating
Tint color:dark gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:
	Mirror Coating
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:Should we add Polarized Filter Coating?:
Should we add Scratch Resistant Coating?:
Should we add Mirror Coating?:
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?
The tint color is not available. We'll make them Dark Gray.
Your order for sunglasses is ready:
--------------------------------------

Brand name:unspecified.
Coating(s):
Tint color:Dark Gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:y
Should we add Polarized Filter Coating?:y
Should we add Scratch Resistant Coating?:y
Should we add Mirror Coating?:y
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green? ambER
The tint color is not available. We'll make them Dark Gray.
Your order for sunglasses is ready:
--------------------------------------
Brand name:unspecified.
Coating(s):
Anti-reflective Coating
Polarized Filter Coating
Sratch Resistant Coating
Mirror Coating
Tint color:Dark Gray.
--------------------------------------
>>> 
========== RESTART: /Users/janechoi/Documents/pa05-orderglasses.py ==========
This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.
Brand name:
Please answer the following questions with Y for yes, N for no.
Should we add Anti-reflective Coating?:n
Should we add Polarized Filter Coating?:n
Should we add Scratch Resistant Coating?:n
Should we add Mirror Coating?:n
Please choose one of the following tint color for lenses:
Dark Gray, Teal, Amber or Green?AmBER
Your order for sunglasses is ready:
--------------------------------------
Brand name:unspecified.
Coating(s):
No coating
Tint color:amber.
--------------------------------------
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_only_digits('1,2,3')
False
>>> 
============ RESTART: /Users/janechoi/Documents/pa05-functions.py ============
>>> contains_letter('absdf1')
True
>>> contains_letter('1111')
False
>>> 
