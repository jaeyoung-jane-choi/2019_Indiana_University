Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> morning = "sunny"
>>> morning
'sunny'
>>> morning = "chilly"
>>> morning
'chilly'
>>> morning = 14
>>> morning
14
>>> type(morning)
<class 'int'>
>>> midday = 12
>>> morning
14
>>> morning = None
>>> morning
>>> type(morning)
<class 'NoneType'>
>>> del morning
>>> morning
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    morning
NameError: name 'morning' is not defined
>>> # don't do the following unless you want mayhem
>>> del print
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    del print
NameError: name 'print' is not defined
>>> del print()
SyntaxError: can't delete function call
>>> print
<built-in function print>
>>> del True
SyntaxError: can't delete keyword
>>> del False
SyntaxError: can't delete keyword
>>> del print
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    del print
NameError: name 'print' is not defined
>>> morning = "chilli"
>>> morning[5] = "y"
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    morning[5] = "y"
TypeError: 'str' object does not support item assignment
>>> morning
'chilli'
>>> morning[5]
'i'
>>> morning[6]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    morning[6]
IndexError: string index out of range
>>> morning[6] = "e"
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    morning[6] = "e"
TypeError: 'str' object does not support item assignment
>>> del morning[5]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    del morning[5]
TypeError: 'str' object doesn't support item deletion
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
Traceback (most recent call last):
  File "/Users/Shared/Desktop/oct14morning01.py", line 4, in <module>
    morning[5] = "y"
TypeError: 'str' object does not support item assignment
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
Traceback (most recent call last):
  File "/Users/Shared/Desktop/oct14morning01.py", line 6, in <module>
    del morning[5]
TypeError: 'str' object doesn't support item deletion
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
>>> student
('Jo', 'Johnson', 22, -332)
>>> type(student)
<class 'tuple'>
>>> student[0]
'Jo'
>>> student[1]
'Johnson'
>>> student[-1]
-332
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
>>> student[-1]
'000-11-321'
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
>>> noStudent
()
>>> type(noStudent)
<class 'tuple'>
>>> morning
'chilli'
>>> morning = morning + "er"
>>> morning
'chillier'
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
Traceback (most recent call last):
  File "/Users/Shared/Desktop/oct14morning01.py", line 24, in <module>
    noStudent = noStudent + "Jo"
TypeError: can only concatenate tuple (not "str") to tuple
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
Traceback (most recent call last):
  File "/Users/Shared/Desktop/oct14morning01.py", line 24, in <module>
    noStudent = noStudent + ("Jo")
TypeError: can only concatenate tuple (not "str") to tuple
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
Traceback (most recent call last):
  File "/Users/Shared/Desktop/oct14morning01.py", line 24, in <module>
    noStudent = noStudent + ("Jo" + "e")
TypeError: can only concatenate tuple (not "str") to tuple
>>> ("Jo" + "e")
'Joe'
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
>>> noStudent
('Jo',)
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
>>> noStudent
('Jo', 'Johnson', 22, '000-11-321')
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
printing out student info:
element = Jo
element = Johnson
element = 22
element = 000-11-321
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
printing out student1 info:
element = Jo
element = Johnson
element = 22
element = 000-11-321
('Jo', 'Johnson', 22, '000-11-321')
('Jo', 'Johnson', 22, '000-11-321')
('Jo', 'Johnson', 22, '000-11-321')
('Jo', 'Johnson', 22, '000-11-321')
('Jill', 'Jilligan', 23, '999-22-123')
('Jill', 'Jilligan', 23, '999-22-123')
('Jill', 'Jilligan', 23, '999-22-123')
('Jill', 'Jilligan', 23, '999-22-123')
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
printing out student1 info:
element = Jo
element = Johnson
element = 22
element = 000-11-321
Jo
Johnson
22
000-11-321
Jill
Jilligan
23
999-22-123
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
printing out student1 info:
element = Jo
element = Johnson
element = 22
element = 000-11-321
Name = 
Last Name = 
Age = 
SSN = 
Name = 
Last Name = 
Age = 
SSN = 
>>> student1[3]
'000-11-321'
>>> student2[2]
23
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
printing out student1 info:
element = Jo
element = Johnson
element = 22
element = 000-11-321
Name = Jo
Last Name = Jo
Age = Jo
SSN = Jo
Name = Jill
Last Name = Jill
Age = Jill
SSN = Jill
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
printing out student1 info:
element = Jo
element = Johnson
element = 22
element = 000-11-321
Name = Jo
Last Name = Johnson
Traceback (most recent call last):
  File "/Users/Shared/Desktop/oct14morning01.py", line 49, in <module>
    printStudentRecord1(student1)
  File "/Users/Shared/Desktop/oct14morning01.py", line 45, in printStudentRecord1
    print(item + r[counter])
TypeError: can only concatenate str (not "int") to str
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
printing out student1 info:
element = Jo
element = Johnson
element = 22
element = 000-11-321
Name = Jo
Last Name = Johnson
Age = 22
SSN = 000-11-321
Name = Jill
Last Name = Jilligan
Age = 23
SSN = 999-22-123
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
printing out student1 info:
element = Jo
element = Johnson
element = 22
element = 000-11-321
Name = Jo
Last Name = Johnson
Age = 22
SSN = 000-11-321
Name = Jill
Last Name = Jilligan
Age = 23
SSN = 999-22-123
>>> range(10)
range(0, 10)
>>> 
============== RESTART: /Users/Shared/Desktop/oct14morning01.py ==============
 morning has 6 characters
 the two strings are different 
printing out student1 info:
element = Jo
element = Johnson
element = 22
element = 000-11-321
Name = Jo
Last Name = Johnson
Age = 22
SSN = 000-11-321
Name = Jill
Last Name = Jilligan
Age = 23
SSN = 999-22-123
>>> "Jo" in student1
True
>>> "Jo" in student2
False
>>> len(student1)
4
>>> student1[0:1]
('Jo',)
>>> student1[0:2]
('Jo', 'Johnson')
>>> student1[-2:-1]
(22,)
>>> student1[-2:]
(22, '000-11-321')
>>> student1[:]
('Jo', 'Johnson', 22, '000-11-321')
>>> student[0:3
	]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    student[0:3
NameError: name 'student' is not defined
>>> student1[0:3]
('Jo', 'Johnson', 22)
>>> student1[:2]
('Jo', 'Johnson')
>>> 
