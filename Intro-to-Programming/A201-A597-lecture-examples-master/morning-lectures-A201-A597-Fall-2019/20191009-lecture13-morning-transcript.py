Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> len()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
>>> 
================ RESTART: /Users/Shared/Desktop/practicalA.py ================
Please enter a word (enter 'done' when done):
done
You have entered 0 letters.
>>> 
================ RESTART: /Users/Shared/Desktop/practicalA.py ================
Please enter a word (enter 'done' when done):
done
You have entered 4 letters.
>>> 
================ RESTART: /Users/Shared/Desktop/practicalA.py ================
Please enter a word (enter 'done' when done):
duck
Traceback (most recent call last):
  File "/Users/Shared/Desktop/practicalA.py", line 16, in <module>
    pass
KeyboardInterrupt
>>> 
================ RESTART: /Users/Shared/Desktop/practicalA.py ================
Please enter a word (enter 'done' when done):
duck
Please enter a word (enter 'done' when done):
elephant
Please enter a word (enter 'done' when done):
mouse
Please enter a word (enter 'done' when done):
done
You have entered 21 letters.
>>> 
================ RESTART: /Users/Shared/Desktop/practicalA.py ================
Please enter a word (enter 'done' when done):
one
Please enter a word (enter 'done' when done):
two
Please enter a word (enter 'done' when done):
three
Please enter a word (enter 'done' when done):
four
Please enter a word (enter 'done' when done):
five
Please enter a word (enter 'done' when done):
six
Please enter a word (enter 'done' when done):
seven
Please enter a word (enter 'done' when done):
eight
Please enter a word (enter 'done' when done):
done
You have entered 36 letters.
>>> 
================ RESTART: /Users/Shared/Desktop/practicalA.py ================
Please enter a word (enter 'done' when done):
one
Please enter a word (enter 'done' when done):
two
Please enter a word (enter 'done' when done):
three
Please enter a word (enter 'done' when done):
four
Please enter a word (enter 'done' when done):
five
You have entered 19 letters.
>>> 
================ RESTART: /Users/Shared/Desktop/practicalA.py ================
Please enter a word (enter 'done' when done):
one
Please enter a word (enter 'done' when done):
two
Please enter a word (enter 'done' when done):
three
Please enter a word (enter 'done' when done):
four
Please enter a word (enter 'done' when done):
five
You have entered 19 letters.
>>> 
================ RESTART: /Users/Shared/Desktop/practicalB1.py ================
>>> functionB1("hey","hoy","hello")
'heyhoyhello'
>>> 
================ RESTART: /Users/Shared/Desktop/practicalB1.py ================
>>> functionB1("a","b","c")
abc
>>> _
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    _
NameError: name '_' is not defined
>>> 3 * 2
6
>>> _
6
>>> a = functionB1("1","2","x")
12x
>>> a
>>> type(a)
<class 'NoneType'>
>>> 
================ RESTART: /Users/Shared/Desktop/practicalB3.py ================
>>> b = functioB3(22)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b = functioB3(22)
NameError: name 'functioB3' is not defined
>>> b = functionB3(22)
>>> b
True
>>> b = functionB3(43)
>>> b
False
>>> 
================ RESTART: /Users/Shared/Desktop/practicalB3.py ================
>>> functionB3(12)
True
>>> functionB3(-21)
False
>>> 
