# we demonstrate for the first time in A201/A597
# the concept of functional programming!

def functionalExtreme():
    print("...to a point of no return.")

    functionalExtreme()

    # here the function functionalExtreme()
    #   is over... there's nothing more to do,
    #   so it can return to the main program,
    #   or to whatever called it.

#########################################
#   main program begins here
#########################################

print(" this is a great program. ")
functionalExtreme()
