# lecture 04... we talk about defining functions




# note to self:
# we can't call a function before it's defined
#   banner()   <--- this would cause an error



# we define a function in Python by simply
#      writing 'def' (without quotes),
#      and the function's name (which must be unique),
#      followed by a ":" (also without quotes)
def banner():
    print("--------------------------------")
    print("|                              |")
    print("|    colossal cave adventure   |")
    print("|                              |")
    print("--------------------------------")

# we can then call our own functions the same way
#      as we call built-in Python functions... just
#      place '()' (without quotes) after its name:
banner()
banner()
banner()
banner()

# we're going to define a function named twice()
# that returns its input * 2
#
# (here begins the function definition...)
def twice(inputNumber): # <--- function's parameter follows camelCase naming convention
    # (here begins the function's "body")
    # the function twice() has 1 parameter named inputNumber,
    #      of numeric type, or string type
    
    # inside the function, we can use the function's parameter(s)
    #      as a variable that is local to the function:
    return inputNumber * 2

    print("this print() statement never gets executed")
    # (here ends the function's "body")



myNumber = 33

print("my number is " + str(myNumber))
print("twice my number is " + str( twice(myNumber) ) )





# lecture 04 task B:
#     implement the following function:
def a_function_with_two_parameters(firstParam, secondParam):
    # write a function that computes a tip:
    #     firstParam is the bill amount,
    #     secondParam is the % of the tip (e.g. 10, 15, 20, etc.)

    pass
    # note: the above 'pass' statement (without quotes)
    #       does absolutely nothing. Why do we need it here?
    #       We use the 'pass' statement here as placeholder,
    #       until we write the actual "body" of this function.
    #       Namely, Python does not allow defining
    #       functions that have nothing in their body.
    









