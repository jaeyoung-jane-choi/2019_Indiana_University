#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 09 part II", Jane Choi , janechoi



###C

#functions from B 
def inHistogram(s,d):
    """Takes one character & one character record, returns True when character is listed in character record

    string, dict-> bool"""
    #if the character is in the dictionary, it will print True,
    #ifnot returns False 
    return s in d


def addToHistogram(s,d):
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
                


def makeHistogram(s):
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


def getFrequency(s,d):
    """Takes one character & one character record, returns the frequency associated with that character in the given character record

    string, dict -> int"""
    #if the character is in the dictionary 
    if s in d:
        #the value is returned 
        return d[s]
    #if not returns 0 (since its not in the dictionary)
    
    else:
        return 0
    
######################functions for C
#1


def histoprint1(d):
    """Takes a dictionary representing a histogram, and prints out a representation of the histogram

    dict -> None"""
    copy = d.copy()

    #for the keys in the dictionary d: 
    for keys in d:
        #make the copy for d , with new values of #
        copy[keys] = '#'* d[keys]

        #print out the key and value
        print(keys+' : '+ copy[keys])
    
####################################
#2

def histoprint2(d):
    """Takes a dictionary representing a histogram, and prints out a representation of the histogram

    dict -> None"""
    copy = d.copy()

    #for the sorted dictionary d 
    for keys in sorted(d):
        #make the copy for d, with new values of # 
        copy[keys] = '#'* d[keys]
        
        print(keys +' : ' +copy[keys])




####################################
#3

def histoprint3(d,i):
    """Takes a dictionary representing a histogram,an integer representing a scaling factor

    dict, int -> none """
    copy = d.copy()

    #for the keys in d: 
    for keys in d:
        #make the copy of d with #values. 
        copy[keys] = '#'* d[keys]

        #if the values for key is larger than the i 
        if d[keys] >= i :
            #print out the copy values for the keys
            print(keys+' : '+ copy[keys])
            #if not, print out the keys
            #making just keys printed out with nothing else 
        else:
            print(keys)

        



####################################
#4


def histoprint4(h):
    """takes a histogram and automatically scales the output, to be able to represent larger amount of data within a limited-width printout.

    dict->none"""

    #get the max value 
    num = 0
    #for all the values in the histogram 
    for values in h.values():
        #if the value is larger than the number :
        if num < values:
            #the value becomes the number 
            num = values
    #now the num is the largest value 
        
    for keys in h:
        #make the values in h, scaled by the largest number *10 
        h[keys] = int((h[keys]/num)*10)
        #make the values into #s 
        h[keys] = '#'* h[keys]
        #print out the key and value
        print( keys + ' : '+ h[keys])
    
    

   
