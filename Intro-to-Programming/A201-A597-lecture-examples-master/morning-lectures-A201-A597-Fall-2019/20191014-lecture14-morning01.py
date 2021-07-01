# strings are immutable!
# e.g.:
morning = "chilli"
# morning[5] = "y"   # <-- error: str does not support
                     #            item assignment...
# del morning[5]     # <-- error: ... nor deletion!


# a string is a *sequence*, for 2 reasons:
#
# (1) it has multiple elements, e.g.:
print(" morning has " + str(len(morning)) + " characters")
# (2) elements are in a specific order:
if (morning != "chilil") :
    print(" the two strings are different ")

# first example at lecture time of ... a tuple!

student1 = ("Jo", "Johnson", 22, "000-11-321")

# an empty tuple:

student2 = ()
student2 = student2 + ("Jill",)
student2 = student2 + ("Jilligan",)
student2 = student2 + (23,)
student2 = student2 + ("999-22-123",)

print("printing out student1 info:")
for element in student1:
    print("element = " + str(element))

def printStudentRecord1(r):
    """ prints a student1 record stored in a tuple
        side effect: printout

        r -> None"""
    lTuple = ("Name = ", "Last Name = ",   \
              "Age = ", "SSN = ")
    # lecture Task 2:
    # implement this function,
    # you *must* use a for loop!
    counter = 0
    for item in lTuple:
        print(item + str(r[counter]))
        counter = counter + 1
        
def printStudentRecord2(r):
    """ prints a student1 record stored in a tuple
        side effect: printout

        r -> None"""
    lTuple = ("Name = ", "Last Name = ",   \
              "Age = ", "SSN = ")
    # lecture Task 2:
    # implement this function,
    # you *must* use a for loop!
    indices = (0, 1, 2, 3)
    for index in indices:
        print(lTuple[index] + str(r[index]))
        

def printStudentRecord3(r):
    """ prints a student1 record stored in a tuple
        side effect: printout

        r -> None"""
    lTuple = ("Name = ", "Last Name = ",   \
              "Age = ", "SSN = ")
    # lecture Task 2:
    # implement this function,
    # you *must* use a for loop!
    for index in range(4)
        print(lTuple[index] + str(r[index]))
        
printStudentRecord3(student1)
printStudentRecord3(student2)




