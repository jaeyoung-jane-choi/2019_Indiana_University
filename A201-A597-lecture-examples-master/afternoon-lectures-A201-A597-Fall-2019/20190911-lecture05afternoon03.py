


# a program that asks how I'm doing today:

userResponse = input("are you happy today? ")

if (userResponse == 'no'):
    # this block of code gets executed
    # if the above logical condition is True
    print("I'm sorry...")
elif (userResponse == 'NO'):
    # this block of code gets executed
    # if the above logical condition is True
    print("I'm sorry...")
else:
    # this block of code gets executed
    # if the above logical condition is False
    print("That's great!")

#   today's lecture 05 Task A:
#
#   fix the above if-statement so that it
#   prints "I'm sorry..." in every 'no' case, i.e.:
#   'no' 'NO' 'nO' 'No'


#   today's lecture 05 Task B:
#
#   fix the above if-statement so that it
#   prints "I'm sorry..." even if
#   there are trailing or following spaces, e.g.:
#   '   no    ',  "NO     ",   "      nO" are all valid.




