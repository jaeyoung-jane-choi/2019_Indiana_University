
# defining a function:
def cubify( pNumber ) :
    #
    #  number -> number
    #
    # function body begins here
    
    # function parameters behave like
    #   'local' variables within a function:
    lTotal = pNumber * pNumber * pNumber

    return lTotal
    # function body ends here

# defining a new function that also uses cubify() as a helper:
def cubifyPlusTip( pNumerical ):

    # ( pNumerical cube ) + ( 10% of pNumerical )
    
    # here we reuse our function cubify() as defined above:
    #
    lResult = cubify(pNumerical) + ( pNumerical * 0.1 )
    return lResult

##############################################
# the main program in this script begins here:
##############################################

# any function parameters or local variables
#       (from within function definitions)
#  cannot be used outside of their functions,
#  e.g. the following line won't work,
#  because  pNumber exists only
#     within its function i.e. within cubify()
# print(pNumber)

aStringContainingANumber = input("please enter a number: ")
# remember: the input() function always returns a string!
#  it's up to you to convert it if necessary:
aNumber = int(aStringContainingANumber)

result = cubify( aNumber )
print("triple your number is... " + str(result) )





