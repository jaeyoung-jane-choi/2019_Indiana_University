# demonstrating the 'if' statement:

userInput = input("are you happy today? ")

# syntax for if statement:
# if   CONDITION  :
#    ... block of code to execute
#        if the condition is True ...
# else :
#    ... block of code to execute
#        if the condition is False ...

if (userInput == "no") :
    # this part gets executed if the condition
    # is True:
    print("I'm sorry...")
else:
    # this part gets executed if the condition
    # is False:
    print("I'm glad!")
