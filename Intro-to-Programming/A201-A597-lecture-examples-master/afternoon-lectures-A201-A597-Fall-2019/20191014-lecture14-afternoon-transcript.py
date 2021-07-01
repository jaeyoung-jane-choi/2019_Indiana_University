Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> afternoon = "sunny"
>>> afternoon
'sunny'
>>> type(afternoon)
<class 'str'>
>>> afternoon = "chilly"
>>> afternoon = 14
>>> afternoon = 16
>>> afternoon = "chilli"
>>> afternoon[5]
'i'
>>> afternoon[5] = "y"
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    afternoon[5] = "y"
TypeError: 'str' object does not support item assignment
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
Traceback (most recent call last):
  File "/Users/Shared/Desktop/oct14afternoon.py", line 4, in <module>
    morning[5] = "y"
TypeError: 'str' object does not support item assignment
>>> morning
'chilli'
>>> morning = "chilly"
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
>>> morning == afternoon
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    morning == afternoon
NameError: name 'afternoon' is not defined
>>> afternoon = "now"
>>> morning == afternoon
False
>>> morning
'chilly'
>>> morning
'chilly'
>>> afternoon = morning
>>> afternoon
'chilly'
>>> morning
'chilly'
>>> morning = None
>>> morning
>>> type(morning)
<class 'NoneType'>
>>> del morning
>>> morning
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    morning
NameError: name 'morning' is not defined
>>> del afternoon[0]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    del afternoon[0]
TypeError: 'str' object doesn't support item deletion
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
>>> 
>>> student1
('Pat', 'Petersen', 19, '987-65-4321')
>>> 987-65-4321
-3399
>>> "987-65-4321"
'987-65-4321'
>>> "first " + "second"
'first second'
>>> astring = "first " + "second"
>>> astring
'first second'
>>> astring = "a" + 2
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    astring = "a" + 2
TypeError: can only concatenate str (not "int") to str
>>> (1 + 2)
3
>>> (1 + 2,)
(3,)
>>> ("hello"),
('hello',)
>>> 2, 3, 4
(2, 3, 4)
>>> 2, 3 , 4 == "two"
(2, 3, False)
>>> (2, 3 , 4) == "two"
False
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
>>> student2
('Jill',)
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
>>> student1
('Pat', 'Petersen', 19, '987-65-4321')
>>> student2
('Jill', 'Jensen', 32, '123-45-6789')
>>> tuple("Jo")
('J', 'o')
>>> tuple( ("Jo") )
('J', 'o')
>>> tuple( ("Jo"),)
('J', 'o')
>>> student2
('Jill', 'Jensen', 32, '123-45-6789')
>>> student2[0]
'Jill'
>>> student2[0] = "Jo"
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    student2[0] = "Jo"
TypeError: 'tuple' object does not support item assignment
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
Traceback (most recent call last):
  File "/Users/Shared/Desktop/oct14afternoon.py", line 19, in <module>
    print("student2 includes element: " + element)
TypeError: can only concatenate str (not "int") to str
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>> printStudentRecord(student1)
('Pat', 'Petersen', 19, '987-65-4321')
('Pat', 'Petersen', 19, '987-65-4321')
('Pat', 'Petersen', 19, '987-65-4321')
('Pat', 'Petersen', 19, '987-65-4321')
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>> printStudentRecord(student1)
Pat
Petersen
19
987-65-4321
>>> printStudentRecord(student2)
Jill
Jensen
32
123-45-6789
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>> 
>>> printStudentRecord(student1)
something ... Pat
something ... Petersen
something ... 19
something ... 987-65-4321
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>> printStudentRecord(student1)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    printStudentRecord(student1)
  File "/Users/Shared/Desktop/oct14afternoon.py", line 39, in printStudentRecord
    print( prefix + str( element ) )
TypeError: can only concatenate tuple (not "str") to tuple
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>> printStudentRecord(student1)
('Name: ', 'Last Name: ', 'Age: ', 'SSN: ')Pat
('Name: ', 'Last Name: ', 'Age: ', 'SSN: ')Petersen
('Name: ', 'Last Name: ', 'Age: ', 'SSN: ')19
('Name: ', 'Last Name: ', 'Age: ', 'SSN: ')987-65-4321
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>> printStudentRecord(student1)
Name: Pat
Name: Petersen
Name: 19
Name: 987-65-4321
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>> printStudentRecord(student1)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    printStudentRecord(student1)
NameError: name 'printStudentRecord' is not defined
>>> printStudentRecord1(student2)
Name: Jill
Last Name: Jensen
Age: 32
SSN: 123-45-6789
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>> printStudentRecord2(student1)
Name: Pat
Last Name: Petersen
Age: 19
SSN: 987-65-4321
>>> range(4)
range(0, 4)
>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>> printStudentRecord2(student2)
Name: Jill
Last Name: Jensen
Age: 32
SSN: 123-45-6789
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

>>> 
============== RESTART: /Users/Shared/Desktop/oct14afternoon.py ==============
student2 includes element: Jill
student2 includes element: Jensen
student2 includes element: 32
student2 includes element: 123-45-6789
 the student's name is: Jill
 the student's last name is: Jensen
 the student's age is: 32
 the student's SSN is: 123-45-6789
>>>     for index in range(0, 4, 1):
KeyboardInterrupt
>>> printStudentRecord2(student1)
Name: Pat
Last Name: Petersen
Age: 19
SSN: 987-65-4321
>>> 
