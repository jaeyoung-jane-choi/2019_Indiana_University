# nested sequences
#
# review: tuples and lists may contain any types as elements:
#  
# if a sequence's element is itself a sequence,
#    you may loop through it, index it, etc.

hiScores = [
    ["Joey", 10000],
    ["Jill", 8432],
    ["Jack", 100]
    ]
# example: print out hi-score list, name & number:
for item in hiScores:
    # print (item)   # item is 1 element from hiScores

    print ("--> ", end="")
    # since every element is a list, I can loop throuh it:
    for element in item:
        print(str(element) + "\t", end="")  # print, don't go to new line
    print ()
    

hiScoresWithLastNames = [
    [["Joey","Smith"], 10000],
    [["Jill","Abcde"], 8432],
    [["Jack","Jones"], 100]
    ]

# example: print out hi-score list, name, last name & number:
for item in hiScoresWithLastNames:
    # print (item)   # item is 1 element from hiScores
                     # item is an "internal" list

    print ("--> ", end="")
    # since every element is a list, I can loop throuh it:
    for element in item:

        # now element may also be a list!
        #  so let's test if element is a list,
        #  in which case loop through it:
        if (isinstance(element, list)):

            # element is a list containing two strings,
            #  i.e. first and last name:
            first, last = element

            print(first + " " + last + "\t", end="")
            # we could loop through it,
            #   but it isn't necessary for just 2 items
            #  for word in element:
                # in this case, word is either the first or tha last name:
                
                # print(str(word) + "\t", end="")  # print, don't go to new line
        else:
            # it isn't a list, so don't loop through it:
            print(str(element) + "\t", end="")  # print, don't go to new line
        
    print ()












