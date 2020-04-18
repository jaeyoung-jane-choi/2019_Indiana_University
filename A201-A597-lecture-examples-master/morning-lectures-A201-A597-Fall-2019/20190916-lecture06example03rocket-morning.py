def rocket_countdown(pCounter):
    """countdown to 0, using recursion

    Int -> None"""

    # base case, i.e. where recursion stops:
    if (pCounter == 0) :
        print("launch rocket!")
    else:

        # make a simpler version of yourself:
        pCounter = pCounter - 1
        print(" counter = " + str(pCounter) )

        # call yourself again:
        rocket_countdown(pCounter)

    # here the function returns,
    # because there's no more code
    # in the function's body

##################################
# main program begins here...
##################################

print("today we're learning about recursion")
print(" and we are launching a rocket! ")

# ask the user: at what value should we start
#               the countdown?
maxCountdown = int(input("countdown starts at? "))

rocket_countdown( maxCountdown )


