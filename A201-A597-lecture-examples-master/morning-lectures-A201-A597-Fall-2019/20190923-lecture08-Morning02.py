# printing out a string, 1 char at a time,
#
#  version 1: using recursion
#

# introducing the "while" keyword in Python

# "while" works like this:

# while  (logical argument)  :
    
    # run this part if argument is True
    # then check the logical argument again

# continue here, when the logical argument is False


#########################################
#   main program
#########################################

myString = "abcčdefghijklmnopqrsštuvwxyzž"

myIndex = 0

print("debugging: myIndex = " + str(myIndex) )

# set up while loop, checking for end of string:
while ( myIndex < len(myString) ):


    print("debugging before printing: myIndex = " + str(myIndex) )
    
    # print out one character from myString:
    print( myString[myIndex] )


    print("debugging after printing : myIndex = " + str(myIndex) )

    # go to the next character,
    #  i.e. increment myIndex
    myIndex = myIndex - 1

    print("debugging after incrementing : myIndex = " + str(myIndex) )




