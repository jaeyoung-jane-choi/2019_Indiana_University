#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Lab Task 07", Jane Choi, janechoi

#A



def contains_only_integers(t):
    """Takes a tuple, returns True when all items in the tuple are integers

    tuple -> bool"""
    
    #counter is the index of the tuple
    counter = 0
    
    #so when the counter is smaller than the length of the tuple,
    #the while loop continues
    #(the counter should be smaller since it starts at 0
    while counter < len(t):

        #isinstance is a function that checks the variable if its the type
        #so the tuple counter sees if its a integer. 
        result = isinstance(t[counter] , int)

        #if the result is True : meaning that the t[counter] is an integer 
        if result == True :

            #the counter is increased 
            counter = counter + 1
        #if it is False, you can stop seeing other values and break the while loop
        else: break 

    #the def returns the result of bool
    return result




###########################################################################

#B

def analyze_tuple_0(pTuple):
    """Takes a tuple and returns the number of items in the tuple, when not tuple returns -1 

    tuple -> int"""


    #when the pTuple is not a tuple returns number -1
    if isinstance(pTuple, tuple) == False :

        return -1

    #when it is a tuple:
    else:
        
        #it returns the length of the tuple(number of items in the tuple)
        return len(pTuple)
        
    



###########################################################################




