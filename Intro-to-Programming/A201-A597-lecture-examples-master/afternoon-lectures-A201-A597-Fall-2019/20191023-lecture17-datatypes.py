# data types - advantages/disadvantages
#
#
contactsTuple = ( "Adam", "Bryan", "Chris" )
# operations on a tuple:
#  get an element by providing index
#  make a copy using slicing
#  create new tuple by concatenating existing tuples
#  compare tuples

# invalid operations on tuples:
#  modify elements
#  sort elements
#  delete, remove elements
#  append, insert, add to tuple


contactsList = [  "Adam", "Bryan", "Chris"  ]
# operations on a list:
#  get an element by providing index
#  make a copy using slicing
#  create new list by concatenating existing lists
#  compare lists
#  modify elements
#  sort elements
#  delete, remove elements
#  append, insert, add to tuple

# non-pythonic solution:
index = 0
name = "Chris"
found = False

# look through list elements, one at a time:
while (index < len(contactsList)):
    # compare current element to new name:

    # compare current element to new name thus:

    #   contactsList[index] < name

    #   contactsList[index] > name

    # use .insert(index, new_element) to insert in list
    
    
    if (contactsList[index] == name):
        
        print("already there!")
        # set flag variable to True:
        found = True
        break
    # look at next element in list:
    index = index + 1
    
if not found:
    contactsList.append( name )
    

# pythonic solution:
if name in contactsList:
    # the "in" keyword executes ~ same code as above
    print("already there!")
else:
    contactsList.append( name )

# argue whether the above "in" statement
#  takes about no more than 20 instructions working
#  with a list of 10000 elements?!?





# we need pairs to store them in dictionaries:
contactsDict = { 0 :"Adam", 1 :"Bryan", 2 :"Chris"}
