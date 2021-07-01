Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> aString = "chilli"
>>> aString[5]
'i'
>>> aString[5] = "y"
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    aString[5] = "y"
TypeError: 'str' object does not support item assignment
>>> del aString[5]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    del aString[5]
TypeError: 'str' object doesn't support item deletion
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have('water',)
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ('water', 'sunscreen')
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ('water', 'sunscreen', 'flippers')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ('water', 'sunscreen', 'flippers')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ('water', 'sunscreen', 'flippers')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
>>> let(inventory[0:100])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    let(inventory[0:100])
NameError: name 'let' is not defined
>>> len(inventory[0:100])
3
>>> inventory[100]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    inventory[100]
IndexError: tuple index out of range
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
Traceback (most recent call last):
  File "/Users/Shared/Desktop/afternoon01.py", line 33, in <module>
    inventory[4]
IndexError: tuple index out of range
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
Traceback (most recent call last):
  File "/Users/Shared/Desktop/afternoon01.py", line 34, in <module>
    inventory[0] = "lemonade"
TypeError: 'tuple' object does not support item assignment
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
Traceback (most recent call last):
  File "/Users/Shared/Desktop/afternoon01.py", line 36, in <module>
    inventory[0:2] = ("lemonade", "parasol" )
TypeError: 'tuple' object does not support item assignment
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon01.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
 I'm ready for some suntan, because I have ('water', 'sunscreen')
Traceback (most recent call last):
  File "/Users/Shared/Desktop/afternoon01.py", line 38, in <module>
    del inventory[2]
TypeError: 'tuple' object doesn't support item deletion
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
Traceback (most recent call last):
  File "/Users/Shared/Desktop/afternoon02.py", line 39, in <module>
    inventory[4]    #  <- Index error!
IndexError: list index out of range
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
after changing element 0: ['lemonade', 'sunscreen', 'flippers']
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
before changing anything: ['water', 'sunscreen', 'flippers']
after changing element 0: ['lemonade', 'sunscreen', 'flippers']
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
before changing anything: ['water', 'sunscreen', 'flippers']
after changing element 0: ['lemonade', 'sunscreen', 'flippers']
after changing slice [0:2] : ['lemonade', 'parasol', 'flippers']
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
before changing anything: ['water', 'sunscreen', 'flippers']
after changing element 0: ['lemonade', 'sunscreen', 'flippers']
after changing slice [0:2] : ['lemonade', 'parasol', 'flippers']
after deleting element 2 : ['lemonade', 'parasol']
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
before changing anything: ['water', 'sunscreen', 'flippers']
after changing element 0: ['lemonade', 'sunscreen', 'flippers']
after changing slice [0:2] : ['lemonade', 'parasol', 'flippers']
after deleting element 2 : ['lemonade', 'parasol']
Traceback (most recent call last):
  File "/Users/Shared/Desktop/afternoon02.py", line 58, in <module>
    inventory = inventory + "flippers"
TypeError: can only concatenate list (not "str") to list
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
before changing anything: ['water', 'sunscreen', 'flippers']
after changing element 0: ['lemonade', 'sunscreen', 'flippers']
after changing slice [0:2] : ['lemonade', 'parasol', 'flippers']
after deleting element 2 : ['lemonade', 'parasol']
>>> inventory
['lemonade', 'parasol', 'flippers']
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
before changing anything: ['water', 'sunscreen', 'flippers']
after changing element 0: ['lemonade', 'sunscreen', 'flippers']
after changing slice [0:2] : ['lemonade', 'parasol', 'flippers']
after deleting element 2 : ['lemonade', 'parasol']
after adding new element 2 : ['lemonade', 'parasol', 'lots of coffee']
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
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
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
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
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
before changing anything: ['water', 'sunscreen', 'flippers']
after changing element 0: ['lemonade', 'sunscreen', 'flippers']
after changing slice [0:2] : ['lemonade', 'parasol', 'flippers']
after deleting element 2 : ['lemonade', 'parasol']
after adding a new element 2 : ['lemonade', 'parasol', 'lots of coffee']
after adding a new last element : ['lemonade', 'parasol', 'lots of coffee', 'flippers']
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
before changing anything: ['water', 'sunscreen', 'flippers']
after changing element 0: ['lemonade', 'sunscreen', 'flippers']
after changing slice [0:2] : ['lemonade', 'parasol', 'flippers']
after deleting element 2 : ['lemonade', 'parasol']
after adding a new element 2 : ['lemonade', 'parasol', 'lots of coffee']
after adding a new last element : ['lemonade', 'parasol', 'lots of coffee', 'flippers']
 at index 0 there is lemonade
 at index 1 there is parasol
 at index 2 there is lots of coffee
 at index 3 there is flippers
>>> 
================ RESTART: /Users/Shared/Desktop/afternoon02.py ================
 I can swim fast, because I have flippers
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
 I'm ready for some suntan, because I have ['water', 'sunscreen']
before changing anything: ['water', 'sunscreen', 'flippers']
after changing element 0: ['lemonade', 'sunscreen', 'flippers']
after changing slice [0:2] : ['lemonade', 'parasol', 'flippers']
after deleting element 2 : ['lemonade', 'parasol']
after adding a new element 2 : ['lemonade', 'parasol', 'lots of coffee']
after adding a new last element : ['lemonade', 'parasol', 'lots of coffee', 'flippers']
 at index 0 there is lemonade
 at index 1 there is parasol
 at index 2 there is lots of coffee
 at index 3 there is flippers
 there is lemonade in the list
 there is parasol in the list
 there is lots of coffee in the list
 there is flippers in the list

>>> inventory
['lemonade', 'parasol', 'lots of coffee', 'flippers']
>>> del "parasol"
SyntaxError: can't delete literal
>>> inventory.remove("parasol")
>>> inventory
['lemonade', 'lots of coffee', 'flippers']
>>> inventory2 = ["a", "a", "b", "b", "c']
	      
SyntaxError: EOL while scanning string literal
>>> inventory2 = ["a", "a", "b", "b", "c"]
>>> inventory2.remove["b"]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    inventory2.remove["b"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> inventory2.remove("b")
>>> inventory2
['a', 'a', 'b', 'c']
>>> inventory2.remove("d")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    inventory2.remove("d")
ValueError: list.remove(x): x not in list
>>> 
