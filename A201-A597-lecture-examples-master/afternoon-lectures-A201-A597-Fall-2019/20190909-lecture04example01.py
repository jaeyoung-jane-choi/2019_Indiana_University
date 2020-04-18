# we're going to learn how to write
#     our own functions in Python,
#     and then use our own functions !!!

# we can not call a function before defining it:
#      gameStartingBanner()

# we use the keyword "def" (without quotes)
#    to start defining a function,
#    followed by the function's name,
#    parentheses, and ":" (without quotes) 
def gameStartingBanner():
    # the function's body is where we place
    #    all the Python code to be executed
    #    when our function is called.
    # the function's body needs to be indented
    #    typically by 4 spaces:
    print ("---------------------------------")
    print ("                                 ")
    print ("  colossal cave adventure game   ")
    print ("                                 ")
    print ("---------------------------------")

gameStartingBanner()
gameStartingBanner()

# defining the function "triplicate()" (without quotes)
#     this function accepts one parameter
#     named myInputParameter, it has numeric type
def triplicate(myInputParameter):
    # the triplicate() function takes
    #     one parameter named myInputParameter
    #     and it returns the parameter's value...
    #     ...triplicated!

    # any parameter can be used as a local var
    #     inside its function...
    #     ... it is local, i.e. it can only
    #     be used inside the function, and
    #     it disappears once the function
    #     has completed its running:
    return 3 * myInputParameter

# we can call triplicate() now that we defined it

thisIsTheOuputStorage = triplicate(42)

print("three times 42 is " + str(thisIsTheOuputStorage) )

print(" three times 3 is " + str( triplicate(3) ) )

# we want to define a function named tip()
# accepting two numeric parameters:
#   the bill amount,
#   the tip percentage
# the tip() function must return the total,
#   i.e. the bill + the tip, as from parameters
def tip(bill, percentage):
    # ...
    # ...













    
