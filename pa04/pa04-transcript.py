Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> alphabet[3]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    alphabet[3]
NameError: name 'alphabet' is not defined
>>> alphabet = "abcdefghijklmnopqrstuvwxyz"
>>> alphabet[11]
'l'
>>> alphabet[1]
'b'
>>> alphabet[0]
'a'
>>> alphabet[22]
'w'
>>> alphabet[26]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    alphabet[26]
IndexError: string index out of range
>>> alphabet[25]
'z'
>>> alphabet[-1]
'z'
>>> alphabet[2.5]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    alphabet[2.5]
TypeError: string indices must be integers
>>> 'string'.lower()
'string'
>>> STRING.lower()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    STRING.lower()
NameError: name 'STRING' is not defined
>>> 'STRinG'.lower()
'string'
>>> 'STRinG'.lower().count()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    'STRinG'.lower().count()
TypeError: count() takes at least 1 argument (0 given)
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> how_many_vocals('Aeiou!',2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    how_many_vocals('Aeiou!',2)
  File "/Users/janechoi/Documents/pa04-functions.py", line 6, in how_many_vocals
    lower.case = s.lower()
NameError: name 'lower' is not defined
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> how_many_vocals('Aeiou!')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    how_many_vocals('Aeiou!')
  File "/Users/janechoi/Documents/pa04-functions.py", line 6, in how_many_vocals
    lower.case = s.lower()
NameError: name 'lower' is not defined
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> how_many_vocals('Ai')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    how_many_vocals('Ai')
  File "/Users/janechoi/Documents/pa04-functions.py", line 8, in how_many_vocals
    result = lower.case.count('a', 'e' , 'i' , 'o' , 'u')
NameError: name 'lower' is not defined
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> how_many_vocals('Aeiou!')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    how_many_vocals('Aeiou!')
  File "/Users/janechoi/Documents/pa04-functions.py", line 8, in how_many_vocals
    result = word.count('a', 'e' , 'i' , 'o' , 'u')
TypeError: count() takes at most 3 arguments (5 given)
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> how_many_vocals('Aeiou!')
1
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> how_many_vocals('Aeiou!')
1
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> how_many_vocals('Aeiou!')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    how_many_vocals('Aeiou!')
  File "/Users/janechoi/Documents/pa04-functions.py", line 8, in how_many_vocals
    result = word.count(vocal)
TypeError: must be str, not tuple
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> how_many_vocals('Aeiou!')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    how_many_vocals('Aeiou!')
  File "/Users/janechoi/Documents/pa04-functions.py", line 8, in how_many_vocals
    result = word.count(vocal)
TypeError: must be str, not list
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> how_many_vocals('Aeiou!')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    how_many_vocals('Aeiou!')
  File "/Users/janechoi/Documents/pa04-functions.py", line 13, in how_many_vocals
    total.result = result1 +result2+result3+result4+result5
NameError: name 'total' is not defined
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> how_many_vocals('Aeiou!')
5
>>> how_many_vocals("Tessellated?")
4
>>> 
=========== RESTART: /Users/janechoi/Documents/pa04-temperature.py ===========
Please enter a temperature: 32
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa04-temperature.py", line 6, in <module>
    str(user_input1) + 'Celsius ->' + str(user_input1/ 9/5 +32 )+ 'Fahrenheit')
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
=========== RESTART: /Users/janechoi/Documents/pa04-temperature.py ===========
Please enter a temperature: 32
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa04-temperature.py", line 6, in <module>
    str(user_input1) + 'Celsius ->' + str(user_input1* 9/5 + 32 )+ 'Fahrenheit')
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
=========== RESTART: /Users/janechoi/Documents/pa04-temperature.py ===========
Please enter a temperature: 32
The converted temperature is:' +
      str(user_input1) + 'Fahrenheit ->' + str( (user_input1-32)* 5/9 )+ 'Celsius'+
      str(user_input1) + 'Celsius ->' + str(user_input1* 9/5 + 32 )+ 'Fahrenheit
>>> 
=========== RESTART: /Users/janechoi/Documents/pa04-temperature.py ===========
Please enter a temperature: 32
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa04-temperature.py", line 6, in <module>
    str(user_input1) + 'Celsius ->' + str(float(user_input1)* 9/5 + 32 )+ 'Fahrenheit')
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
=========== RESTART: /Users/janechoi/Documents/pa04-temperature.py ===========
Please enter a temperature: 32
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa04-temperature.py", line 4, in <module>
    print('The converted temperature is:' +str(user_input1) + 'Fahrenheit ->' + str((float(user_input1-32))* 5/9)+ 'Celsius'+str(user_input1) + 'Celsius ->' + str(float(user_input1)* 9/5 + 32 )+ 'Fahrenheit')
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
=========== RESTART: /Users/janechoi/Documents/pa04-temperature.py ===========
Please enter a temperature: 32
Traceback (most recent call last):
  File "/Users/janechoi/Documents/pa04-temperature.py", line 10, in <module>
    str(user_input1) + 'Celsius ->' + str((user_input1* 9/5) + 32 )+ 'Fahrenheit')
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
=========== RESTART: /Users/janechoi/Documents/pa04-temperature.py ===========
Please enter a temperature: 32
The converted temperature is:32Fahrenheit ->0.0Celsius32Celsius ->89.6Fahrenheit
>>> 
=========== RESTART: /Users/janechoi/Documents/pa04-temperature.py ===========
Please enter a temperature: 32
The converted temperature is:32Fahrenheit ->0.0Celsius32Celsius ->89.6Fahrenheit
>>> 
=========== RESTART: /Users/janechoi/Documents/pa04-temperature.py ===========
Please enter a temperature: 32
The converted temperature is:
32Fahrenheit ->0.0Celsius
32Celsius ->89.6Fahrenheit
>>> 
=========== RESTART: /Users/janechoi/Documents/pa04-temperature.py ===========
Please enter a temperature: 32
The converted temperature is:
32Fahrenheit ->0.0Celsius
32Celsius ->89.6Fahrenheit
>>> 
======== RESTART: /Users/janechoi/Documents/pa04-tempWithFunctions.py ========
>>> fromCtoF(32)
89.6
>>> fromFtoC(32)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    fromFtoC(32)
  File "/Users/janechoi/Documents/pa04-tempWithFunctions.py", line 26, in fromFtoC
    result = (user_input1-32)* 5/9 #recieves a number and calculates to result
NameError: name 'user_input1' is not defined
>>> 
======== RESTART: /Users/janechoi/Documents/pa04-tempWithFunctions.py ========
>>> fromFtoC(32)
0.0
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> 
============ RESTART: /Users/janechoi/Documents/pa04-functions.py ============
>>> 
