# while loop demonstration on Wednesday morning
#

# decide on "sentinel" variable,
#    sometimes called "flag" variable
#
# the "sentinel" variable is used in the
#    boolean expression controlling the while loop:
#
# example: parent-child conversation
#          with a 2-year old
#
parentsAnswer = "no"
#
# the while loop simulates a 2-year old (jokingly)
#
while (not ( parentsAnswer == "yes")):
    # the above condition controls the while loop.
    #
    # the while loop repeats as long as the above
    #   condition is true
    print("may I have an ice cream?")
    #
    parentsAnswer = input("parent's answer: ")

print("thank you!")
