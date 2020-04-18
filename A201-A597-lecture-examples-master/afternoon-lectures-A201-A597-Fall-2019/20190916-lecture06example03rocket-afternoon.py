def rocket_countdown(pCounter):
    """countdown to 0, using recursion.

    Int -> None"""
    print(" rocket_countdown starts with " + str(pCounter))
    # base case, i.e. where recursion stops:
    if (pCounter == 0):
        print("lauch rocket now!")
    else:
        print(" counter about to be decremented")
        # make a simpler version of yourself:
        pCounter = pCounter - 1
        print(" counter is now " + str(pCounter))
        # call yourself again:
        rocket_countdown(pCounter)
    # here the function returns.

#########################################
#   main program begins here
#########################################
print("today we learn about recursion")
print(" by launching a rocket! ")
# ask user: at what value to start countdown
startingCountdown = int(input("countdown start? "))
rocket_countdown( startingCountdown )
