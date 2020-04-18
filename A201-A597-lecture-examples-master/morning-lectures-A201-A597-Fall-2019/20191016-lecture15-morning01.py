# tuple - type, multiple values, immutable(*),
#         may be used to store any values/types
#         as tuple elements.
#         supports indexing - i.e. refer to 1 element
#         supports slicing - i.e. refer to multiple elements
#         (*) individual values can be referred to,
#             but can not be changed, reordered, deleted

inventory = ( "water", "sunscreen", "flippers" )
# indexing:
print("I can swim fast because I have "+str(inventory[2]))
# slicing:
print("I'm ready for the beach because I have " + \
      str( inventory[0:2]) )
# slicing, again, same slice, different indexing:
print("I'm ready for the beach because I have " + \
      str( inventory[:-1]) )
# tuples can't support changing individual elements:
# inventory[0] = "lemonade" <-- Type Error!
# tuples can't support changing slices of elements:
# inventory[0:2] = ("lemonade", "parasol") # <-- Type Error!
# tuples can't support deleting elements:
# del inventory[0]  # <-- Type Error!

