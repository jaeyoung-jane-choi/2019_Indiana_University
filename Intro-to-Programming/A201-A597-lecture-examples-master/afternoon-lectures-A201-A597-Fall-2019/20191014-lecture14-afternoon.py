# strings are sequences
#             immutable
morning = "chilli"
#  morning[5] = "y"  <-- individual element assignment
#                        won't work
morning = "chilly"

# first tuple example at lecture time:
student1 = ( "Pat", "Petersen", 19, "987-65-4321")

student2 = ()
student2 = student2 + ("Jill",)
student2 = student2 + ("Jensen",)
student2 = student2 + (32,)
student2 = student2 + ("123-45-6789",)

# we can use the for loop with tuples:
for element in student2:
    print("student2 includes element: " + str(element))

print(" the student's name is: " + str(student2[0]) )
print(" the student's last name is: " + str(student2[1]) )
print(" the student's age is: " + str(student2[2]) )
print(" the student's SSN is: " + str(student2[3]) )

def printStudentRecord1( r ):
    """ prints a student record r stored in a tuple
        one line at a time, with explanation for each line.
        Side effect: uses print() !

        tuple -> None"""
    # lecture 14 Task 2:
    #   implement this function.
    #   requirement: *must* use for loop!
    #   i.e. every iteration of the for loop prints one line.

    prefix = ("Name: ", "Last Name: ", "Age: ", "SSN: ")
    count = 0
    for element in r:
        print( str(prefix[count]) + str( element ) )
        count = count + 1

def printStudentRecord2( r ):
    """ prints a student record r stored in a tuple
        one line at a time, with explanation for each line.
        Side effect: uses print() !

        tuple -> None"""
    # lecture 14 Task 2:
    #   implement this function.
    #   requirement: *must* use for loop!
    #   i.e. every iteration of the for loop prints one line.

    prefix = ("Name: ", "Last Name: ", "Age: ", "SSN: ")
    indices = (0, 1, 2, 3)
    # create and update an index with the for loop:
    for index in indices:
        print( str(prefix[index]) + str( r[index] ) )



def printStudentRecord2( r ):
    """ prints a student record r stored in a tuple
        one line at a time, with explanation for each line.
        Side effect: uses print() !

        tuple -> None"""
    # lecture 14 Task 2:
    #   implement this function.
    #   requirement: *must* use for loop!
    #   i.e. every iteration of the for loop prints one line.

    prefix = ("Name: ", "Last Name: ", "Age: ", "SSN: ")
    # update an index with a range() in the for loop:
    # same as ...   for index in range(4):
    for index in range(0, 4, 1):
        print( str( prefix[index] ) + str( r[index] ) )























    
