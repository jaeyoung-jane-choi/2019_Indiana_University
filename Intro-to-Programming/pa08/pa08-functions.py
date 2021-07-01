
#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 08", Jane Choi, janechoi

#B

def middle(l):
    """takes a list and returns a copy of that list with the first, last items removed

    list-> list"""
    
    #a newlist is made(copied)
    newlist = l[1:len(l)-1]
    

    return newlist





########################################################################


#C

def chop(l):
    """takes a list and returns a modified list with the first, last items removed

    list-> list"""
    #delete the first element 
    del l[0]
    #delete the last element
    del l[len(l)-1]

    return l



########################################################################


#F


def get_user_input(l):
    """takes a list of strings and make user select one word from the list, and return that word


    list -> str """

    
    print('Please select one of the following:')

    #for all the values in l, we print the values out 
    for index in range(len(l)):
        print(l[index])

    #the user inputs something 
    user_input = input()


    #if the input is not in the l, 
    while user_input not in l:
        
        print("That wasn't a valid option. Please make a different choice.")
        #the user needs to input something new 
        user_input = input()

    #when selected something from the l, the value is returned 
    return user_input





 





