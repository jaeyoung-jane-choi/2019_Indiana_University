




#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 07", Jane Choi, janechoi

##B


def contains_letter_2(string):
    """Takes a string returns True when the string has at least one alphabetic letter

    string -> bool"""


    #for all the single string in the string
    for strings in string:


        #if the single string has an alphabet letter you can stop checking
        #and return True 
        if strings.isalpha() :

            return True
        
        #if not check every single string
            #where there is no alphabet letter inside, returns false
        
    return False

        





#################################################################################

##C



def contains_only_integers_2(t):
    """Takes a tuple returns True if all items are integers

    tuple -> bool"""

    
    #for every item in t 
    for item in t:

        #if the item is not an int, we return false 
        if isinstance(item, int) == False:
            return False

    #if all items are int we return true 
    return True
            















    








        
