Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
>>> hiScores
[['Jo', 10000], ['Jill', 8432], ['Jack', 100]]
>>> hiScores[0]
['Jo', 10000]
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
['Jo', 10000]
['Jill', 8432]
['Jack', 100]
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
['Jo', 10000]
Jo10000['Jill', 8432]
Jill8432['Jack', 100]
Jack100
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
element: Jo Traceback (most recent call last):
  File "/Users/Shared/Desktop/morning01.py", line 17, in <module>
    print(element + " ", end="")  # print, don't go to new line
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
element: Jo 10000 
element: Jill 8432 
element: Jack 100 
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
--> 
Jo	10000	
--> Jill	8432	
--> Jack	100	
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
--> Jo	10000	
--> Jill	8432	
--> Jack	100	
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
--> Joey	10000	
--> Jill	8432	
--> Jack	100	
>>> hiScores
[['Joey', 10000], ['Jill', 8432], ['Jack', 100]]
>>> hiScores[1]
['Jill', 8432]
>>> hiScores[1][1]
8432
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
--> Joey	10000	
--> Jill	8432	
--> Jack	100	
>>> hiScoresWithLastNames
[[['Joey', 'Smith'], 10000], [['Jill', 'Jackson'], 8432], [['Jack', 'Jones'], 100]]
>>> hiScoresWithLastNames[1]
[['Jill', 'Jackson'], 8432]
>>> hiScoresWithLastNames[1][0]
['Jill', 'Jackson']
>>> hiScoresWithLastNames[1][0][1]
'Jackson'
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
--> Joey	10000	
--> Jill	8432	
--> Jack	100	
--> ['Joey', 'Smith']	10000	
--> ['Jill', 'Jackson']	8432	
--> ['Jack', 'Jones']	100	
>>> help(isinstance)
Help on built-in function isinstance in module builtins:

isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.
    
    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.

>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
--> Joey	10000	
--> Jill	8432	
--> Jack	100	
--> Joey	Smith	10000	
--> Jill	Jackson	8432	
--> Jack	Jones	100	
>>> hiScoresWithLastNames[1][0]
['Jill', 'Jackson']
>>> hiScoresWithLastNames[1][0][0]
'Jill'
>>> hiScoresWithLastNames[1][0][1]
'Jackson'
>>> first = hiScoresWithLastNames[1][0][0]
>>> last = hiScoresWithLastNames[1][0][1]
>>> first
'Jill'
>>> last
'Jackson'
>>> hiScoresWithLastNames[1][0]
['Jill', 'Jackson']
>>> first, last = hiScoresWithLastNames[1][0]
>>> first
'Jill'
>>> last
'Jackson'
>>> (first, last) = hiScoresWithLastNames[1][0]
>>> first
'Jill'
>>> last
'Jackson'
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
--> Joey	10000	
--> Jill	8432	
--> Jack	100	
--> Joey Smith	10000	
--> Jill Jackson	8432	
--> Jack Jones	100	
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
--> Joey	10000	
--> Jill	8432	
--> Jack	100	
--> Joey Smith	10000	
--> Jill Aaaaa	8432	
--> Jack Jones	100	
>>> 
================= RESTART: /Users/Shared/Desktop/morning01.py =================
--> Joey	10000	
--> Jill	8432	
--> Jack	100	
--> Joey Smith	10000	
--> Jill Abcde	8432	
--> Jack Jones	100	
>>> hiScoresWithLastNames
[[['Joey', 'Smith'], 10000], [['Jill', 'Abcde'], 8432], [['Jack', 'Jones'], 100]]
>>> hiScoresWithLastNames.append( [['Zeno', 'Zener'], 9] )
>>> hiScoresWithLastNames
[[['Joey', 'Smith'], 10000], [['Jill', 'Abcde'], 8432], [['Jack', 'Jones'], 100], [['Zeno', 'Zener'], 9]]
>>> hiScoresWithLastNames[:1]
[[['Joey', 'Smith'], 10000]]
>>> firstPlayer = hiScoresWithLastNames[:1]
>>> firstPlayer
[[['Joey', 'Smith'], 10000]]
>>> hiScoresWithLastNames[0]
[['Joey', 'Smith'], 10000]
>>> firstTwoPlayers = hiScoresWithLastNames[0:2]
>>> firstTwoPlayers
[[['Joey', 'Smith'], 10000], [['Jill', 'Abcde'], 8432]]
>>> hiScoresWithLastNames
[[['Joey', 'Smith'], 10000], [['Jill', 'Abcde'], 8432], [['Jack', 'Jones'], 100], [['Zeno', 'Zener'], 9]]
>>> hiScoresWithLastNames[0][0][0] = "Jo
SyntaxError: EOL while scanning string literal
>>> hiScoresWithLastNames[0][0][0] = "Jo"
>>> hiScoresWithLastNames
[[['Jo', 'Smith'], 10000], [['Jill', 'Abcde'], 8432], [['Jack', 'Jones'], 100], [['Zeno', 'Zener'], 9]]
>>> firstTwoPlayers
[[['Jo', 'Smith'], 10000], [['Jill', 'Abcde'], 8432]]
>>> hiScoresWithLastNames[0][0][0]
'Jo'
>>> myHiScoreList = { 0 : [['Joey', 'Smith'], 10000], 1 : [['Jill', 'Abcde'], 8432], 2 : [['Jack', 'Jones'], 100], 3 : [['Zeno', 'Zener'], 9] }
>>> myHiScoreList
{0: [['Joey', 'Smith'], 10000], 1: [['Jill', 'Abcde'], 8432], 2: [['Jack', 'Jones'], 100], 3: [['Zeno', 'Zener'], 9]}
>>> myHiScoreList[0]
[['Joey', 'Smith'], 10000]
>>> myHiScoreList[1]
[['Jill', 'Abcde'], 8432]
>>> myHiScoreList = { "Jo" : [['Joey', 'Smith'], 10000] }, "Phantom" : [['Jill', 'Abcde'], 8432], "Vibe" : [['Jack', 'Jones'], 100] }
SyntaxError: invalid syntax
>>> myHiScoreList = { "Jo" : [['Joey', 'Smith'], 10000], "Phantom" : [['Jill', 'Abcde'], 8432], "Vibe" : [['Jack', 'Jones'], 100] }
>>> myHiScoreList["Phantom"]
[['Jill', 'Abcde'], 8432]
>>> myHiScoreList["Phantom"] = [['Pat', 'Patson'], 2222]
>>> myHiScoreList
{'Jo': [['Joey', 'Smith'], 10000], 'Phantom': [['Pat', 'Patson'], 2222], 'Vibe': [['Jack', 'Jones'], 100]}
>>> 
