# data types - advantages / disadvantages
#
#
contactsTuple = ( "Abby", "Berthold", "Cat" )
#


contactsList = [ "Abby", "Berthold", "Cat" ]
# operations on a list:
# add an element
# slice (i.e. extract a part of the list)
# delete an element (either .remove() or del)
# modify an element, e.g.:
contactsList[0] = "Ada"
# search for an element
#    worst-case scenario: check every element in list
#

# non-pythonic solution:
index = 0
name = "Bert"
found = False
while (index < len(contactsList)):
    if ( contactsList[index] == name ):
        print("found it!")
        found = True
        break
    index = index + 1
if ( found == False ) :
    contactsList.append(name)

# pythonic solution:
if name in contactsList:
    print("found it!")
else:
    contactsList.append(name)

contactsDict = { 1 : "Abby", 2 : "Berthold", 3 : "Cat" }








