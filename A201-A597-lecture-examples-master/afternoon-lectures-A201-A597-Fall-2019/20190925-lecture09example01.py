# demonstration of while loop
# with an unknown-in-advance n. of repetitions

# (1) decide on "sentinel" variable,
#   sometimes called "flag" variable

# the "sentinel" variable is going to be used
#   in the boolean expression
#   that controls the while loop

# example: parent-child conversation
#          with a 2-year old
#
parentAnswer = "no"
counter = 0

while not  ( parentAnswer.lower() == "yes" )  :
    # the above condition controls the while loop

    print("may I have an ice cream?")

    parentAnswer = input ("parent's answer: ")

    counter = counter + 1

print("thank you!")
print("we had to endure " + str(counter) + " questions")
