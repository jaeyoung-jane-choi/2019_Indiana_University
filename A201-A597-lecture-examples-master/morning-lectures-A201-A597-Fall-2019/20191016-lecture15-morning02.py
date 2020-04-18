# lists - type, multiple values, mutable(*),
#         may be used to store any values/types
#         as list elements.
#         supports indexing - i.e. refer to 1 element
#         supports slicing - i.e. refer to multiple elements
#         (*) individual values can be referred to,
#             as well as changed, reordered, deleted, ...

# create a list by listing its values, in square brackets:
inventory = [ "water", "sunscreen", "flippers" ]
# indexing:
print("I can swim fast because I have "+str(inventory[2]))
# slicing:
print("I'm ready for the beach because I have " + \
      str( inventory[0:2]) )
# slicing, again, same slice, different indexing:
print("I'm ready for the beach because I have " + \
      str( inventory[:-1]) )
# lists do support changing individual elements:
inventory[0] = "lemonade" # <-- NO Error!

# lists do support changing individual elements, even to a different type!
inventory[2] = 42

# lists do not support assigning individual elements to non-existing positions:
# inventory[3] = 42   # <-- because the index is out of range, I get IndexError!

inventory = inventory + ["flippers"]  # <-- concatenation creates new list!
                                      #     (from the lists/elements that are concatenated)
                                      #     we then re-assign that new list to
                                      #     the name  inventory
                                    
inventory.append("flippers")        # <-- appending adds new element(s) to
                                    #     existing list, without copying, etc.


# lists do support changing slices of elements:
inventory[0:2] = ["lemonade", "parasol"] # <-- NO Error!

# print out list to see what's in it:
for i in range( len(inventory) ) :
    print(" at index " + str(i) + " there is " + str( inventory[i] ) )

print("DANGER: about to delete element 0 from inventory list")

# lists do support deleting elements:
del inventory[0]  # <-- NO Type Error!

# lists re-index after element deletion!
#  therefore, be CAREFUL about referring to the same elements at new indices!
#  also, element deletion is potentially slow, if lots of elements need re-indexing

# print out all elements in list, using:
#   for loop  - to loop throuh all the elements in the list
#   range of indices  - to generate all indices for that list
#         (this ranges uses len() to obtain lenght of list)
#   indexing  - uses index i to extract 1 element at a time from the list
for i in range( len(inventory) ) :
    print(" at index " + str(i) + " there is " + str( inventory[i] ) )

# print out all elements in list, without indexing, using instead:
#   for loop  - to loop throuh all the elements in the list
#               by extracting 1 element from the list at a time
for elem in inventory:
    print(" we have " + str(elem) )

