# printing out a string, 1 char at a time,
#
#  version 1: using recursion
#

# defining function print_a_char() :

def print_a_char(i):
    """recursively print 1 char from myString global

    Int -> None"""

    if i == len(myString):
        # base case: end of string, just return
        print("debuggin base case ... now i = " + str(i))
        return
    else:
        print("debuggin recursion ... now i = " + str(i))
        # recursive case:
        #    print char at current index
        #    increment index,
        #    call itself recursively
        print( myString[i] )
        i = i + 1
        print_a_char(i)
        
    # end of function print_a_char()
    

#########################################
#   main program
#########################################

myString = "abcdefghijklmnopqrstuvwxyz"

print_a_char(0)
