# 2019-10-16 afternoon lecture
#
# tuple - data type, immutable(*), multiple values;
#         may be used to store any types/values
#         as tuple elements (multiple elements per tuple).
#         Tuples support indexing - referring to 1 element;
#         tuples support extracting 1 element at a time.
#         Tuples support slicing - referring to multiple
#         elements at a time.
#         (*) individual values in a tuple can be...
#         ...referred to, but not:
#         changed, delete, reordered.
#         Therefore, adding values to a tuple is only
#         possible by concatenation, which creates
#         a new tuple.

inventory = ( "water", "sunscreen", "flippers" )
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

# tuples cannot be indexed outside their range:
#  inventory[4]  <- Index error!
# tuples can't support changing individual elements:
#  inventory[0] = "lemonade" <- Type Error!
# tuples can't support changing slices of elements:
# inventory[0:2] = ("lemonade", "parasol" )
# tuples can't support deleting elements:
# del inventory[2] <- Type error!
