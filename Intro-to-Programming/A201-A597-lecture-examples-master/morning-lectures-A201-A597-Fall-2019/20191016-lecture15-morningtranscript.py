Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
I can swim fast because I have flippers
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ('water', 'sunscreen')
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ('water', 'sunscreen')
I'm ready for the beach because I have ('water', 'sunscreen')
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ('water', 'sunscreen')
I'm ready for the beach because I have ('water', 'sunscreen')
Traceback (most recent call last):
  File "/Users/Shared/Desktop/morning01.py", line 19, in <module>
    inventory[0] = "lemonade"
TypeError: 'tuple' object does not support item assignment
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ('water', 'sunscreen')
I'm ready for the beach because I have ('water', 'sunscreen')
Traceback (most recent call last):
  File "/Users/Shared/Desktop/morning01.py", line 21, in <module>
    inventory[0:2] = ("lemonade", "parasol") # <-- Type Error!
TypeError: 'tuple' object does not support item assignment
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ('water', 'sunscreen')
I'm ready for the beach because I have ('water', 'sunscreen')
Traceback (most recent call last):
  File "/Users/Shared/Desktop/morning01.py", line 23, in <module>
    del inventory[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
>>> inventory
['lemonade', 'sunscreen', 'flippers']
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
>>> inventory
['lemonade', 'parasol', 'flippers']
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
>>> inventory
['parasol', 'flippers']
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
 at index 0 there is parasol
 at index 1 there is flippers
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers

I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
 at index 0 there is parasol
 at index 1 there is flippers
 we have parasol
 we have flippers
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
Traceback (most recent call last):
  File "/Users/Shared/Desktop/morning02.py", line 22, in <module>
    inventory[3] = 42
IndexError: list assignment index out of range
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
 at index 0 there is parasol
 at index 1 there is 42
 we have parasol
 we have 42
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
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
Traceback (most recent call last):
  File "/Users/Shared/Desktop/morning02.py", line 26, in <module>
    inventory[3] = 42   # <-- because the index is out of range, I get IndexError!
IndexError: list assignment index out of range
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
 at index 0 there is parasol
 at index 1 there is 42
 at index 2 there is flippers
 we have parasol
 we have 42
 we have flippers
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

>>> list()
[]
>>> list("for example a string")
['f', 'o', 'r', ' ', 'e', 'x', 'a', 'm', 'p', 'l', 'e', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']
>>> list( ("this", "was", "immutable") )
['this', 'was', 'immutable']
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
Traceback (most recent call last):
  File "/Users/Shared/Desktop/morning02.py", line 28, in <module>
    inventory = inventory + "flippers"  # <-- concatenation creates new list!
TypeError: can only concatenate list (not "str") to list
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
 at index 0 there is lemonade
 at index 1 there is parasol
 at index 2 there is 42
 at index 3 there is flippers
 at index 4 there is flippers
 about to delete element 0 from inventory list
 at index 0 there is parasol
 at index 1 there is 42
 at index 2 there is flippers
 at index 3 there is flippers
 we have parasol
 we have 42
 we have flippers
 we have flippers
>>> 
================= RESTART: /Users/Shared/Desktop/morning02.py =================
I can swim fast because I have flippers
I'm ready for the beach because I have ['water', 'sunscreen']
I'm ready for the beach because I have ['water', 'sunscreen']
 at index 0 there is lemonade
 at index 1 there is parasol
 at index 2 there is 42
 at index 3 there is flippers
 at index 4 there is flippers
DANGER: about to delete element 0 from inventory list
 at index 0 there is parasol
 at index 1 there is 42
 at index 2 there is flippers
 at index 3 there is flippers
 we have parasol
 we have 42
 we have flippers
 we have flippers
>>> inventory
['parasol', 42, 'flippers', 'flippers']
>>> del "parasol"
SyntaxError: can't delete literal
>>> del inventory["parasol"]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    del inventory["parasol"]
TypeError: list indices must be integers or slices, not str
>>> inventory.remove("parasol")
>>> inventory
[42, 'flippers', 'flippers']
>>> del inventory[24]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    del inventory[24]
IndexError: list assignment index out of range
>>> inventory.remove("water")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    inventory.remove("water")
ValueError: list.remove(x): x not in list
>>> 
