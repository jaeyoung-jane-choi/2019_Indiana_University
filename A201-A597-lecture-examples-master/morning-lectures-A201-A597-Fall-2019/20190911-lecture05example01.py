def square_this(pNumber):
    # function body begins here

    # pass - a handy statement that does nothing
    #        useful when we need to put some 
    #        placeholder code, which will be
    #        completed later. At least we can run it!

    # any variable defined within a function
    #    is a "local variable", i.e. it exists
    #    only within that function.
    #    In this case,  lResult  is a local variable:
    lResult = pNumber * pNumber

    return lResult
    # function body ends here

def twice_plus_10_percent(pNumeric):
    # this function takes 1 numeric value
    # and returns as result:
    # the input value, times itself,
    # plus 10 percent of input value,i.e.:
    # (pNumeric * pNumeric) + (pNumeric * 0.1)

    # here I'm using the square_this() function
    #   defined above, as a "helper function"
    lTotal = square_this(pNumeric) + (pNumeric * 0.1)
    return lTotal



###############################################
# the "main" part of this script begins here
###############################################

# first, get some input from the user:
userInput = input("please enter an integer: ")

# remember, user input is always a string!
# convert it to a number, if you need a number:
userNumber = int(userInput)

# second, compute square_this the value of user number:
doubleUserInput = square_this( userNumber )

# third, provide result in output to user
print("your number times itself is: " + str(doubleUserInput) )
