#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 09 part II", Jane Choi , janechoi



###A

# a *character record* is a dictionary where...
        #the single-character strings are keys
        #and the amount of the single character is the value.



def isInRecord(s,d):
    """Takes one character & one character record, returns True when character is listed in character record

    string, dict-> bool"""
    #if the character is in the dictionary, it will print True,
    #ifnot returns False 
    return s in d


def addToRecord(s,d):
    """Takes one character & one character record, and adds an occurrence of that character to the character record.

    string, dict -> dict"""

    if s in d:
        #if the character is in the dictionary, the amount of that character record increases 
        d[s] += 1
    else:
        #if not in the dictionary, a new key & value will be made
        d[s] =1

    #lastly returns the dictionary itself 
    return d 
                
    

def createRecord(s):
    """Takes any string, and returns out a new character record from that string

    str -> dict"""
    #make a empty dictionary 
    d = {}
    #for all the strings in the string  
    for strings in s:
        #if the string is in the dictionary 
        if strings in d:
            #the value of the string will increase 
            d[strings] += 1

        #if not in the dictionary,
        #a new key and value will be added 
        else:
            d[strings] = 1 
            
    return d 


def frequencies(s,d):
    """Takes one character & one character record, returns the frequency associated with that character in the given character record

    string, dict -> int"""
    #if the character is in the dictionary 
    if s in d:
        #the value is returned 
        return d[s]
    #if not returns 0 (since its not in the dictionary)
    
    else:
        return 0






    
