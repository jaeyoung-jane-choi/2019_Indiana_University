# 2019-10-16 afternoon lecture
#
# list  - data type, mutable(*), multiple values;
#         may be used to store any types/values
#         as list elements (multiple elements per list).
#         Lists support indexing - referring to 1 element;
#         lists support extracting 1 element at a time.
#         Lists support slicing - referring to multiple
#         elements at a time.
#         (*) individual values in a list can be...
#         ...referred to, as well as:
#         changed, delete, reordered!
#         Therefore, adding values to a list is possible
#         not only by concatenation, which creates
#         a new list, but also by adding new values to
#         the list without creating a new one!

# our inventory is now going to be implemented as a list:
inventory = [ "water", "sunscreen", "flippers" ]
# Note: the above is a list (and not a tuple) because
#       it is defined using "[" and "]"


# indexing:
print(" I can swim fast, because I have " + str(inventory[2]) )
# slicing:
print(" I'm ready for some suntan, because I have " + \
      str(inventory[0:2]) )
# slicing, again, same slice, different indexing:
print(" I'm ready for some suntan, because I have " + \
      str(inventory[:(len(inventory)-1)]) )
# slicing, again, same slice, yet another indexing:
print(" I'm ready for some suntan, because I have " + \
      str(inventory[:-1]) )

# error-causing statements:

# lists cannot be indexed outside their range:
# inventory[4]    #  <- Index error!

print("before changing anything: " + str(inventory))

# lists do support changing individual elements:
inventory[0] = "lemonade" # <- NO Type Error!
print("after changing element 0: " + str(inventory))

# lists do support changing slices of elements:
inventory[0:2] = ("lemonade", "parasol" )
print("after changing slice [0:2] : " + str(inventory))


# tuples can't support deleting elements:
del inventory[2] # <- NO Type error!
print("after deleting element 2 : " + str(inventory))


# adding elements to a list by concatenation:
inventory = inventory + ["lots of coffee"]
print("after adding a new element 2 : " + str(inventory))

# adding elements to a list by using its methods...:

inventory.append("flippers")
print("after adding a new last element : " + str(inventory))

# print out all elements in list, using:
#   for loop - to iterate through all elements in list
#   len() - to obtain the lenght of the list
#   range() of indices - generates all indices for that list
#   indexing - uses index i to extract 1 element at a time
for i in range( len( inventory ) ) :
    print(" at index " + str(i) + " there is " + \
          str( inventory[i] ) )
    
#

for elem in inventory:
    print(" there is " + elem + " in the list")
    
