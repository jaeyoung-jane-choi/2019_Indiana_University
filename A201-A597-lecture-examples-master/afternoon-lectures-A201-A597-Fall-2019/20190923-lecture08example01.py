# we are going to talk about indices and strings and ...
# ... print out a string, one character at a time
#
# version 1 uses recursion

myString = "abcdefghijklmnopqrstuvwxyz"

# should not crash on empty strings e.g. myOtherString = ""

def print_a_char(i):
    """recursively print one char from myString global

    Int -> None"""

    # base case:
    if ( i == len (myString)  ) :
        # do nothing in the base case
        print("debugging base case... now i = " + str(i))
        return
    # recursion:
    else:
        print("debugging recursion... now i = " + str(i))
        print( myString[i] )
        i = i + 1
        print_a_char(i)

############################################

print_a_char(0)
