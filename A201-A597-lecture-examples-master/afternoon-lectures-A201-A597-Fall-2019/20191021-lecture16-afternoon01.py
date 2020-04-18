# nested sequences
#
# review: tuples and lists may contain any types as elements
# e.g. lists and tuples as elements of other lists and tuples

hiScores = [      #  a list of lists
    ["Alex", 20000],
    ["Bert", 9999],
    ["Cat", 200]
    ]

# example: print out hi-score list,
#          name & points, one per line

for item in hiScores:
    # item is 1 entry in the hiScores list,
    #    both name and points --- it's a list on its own.
    if ("Cat"==item[0]):
        print("Cat has at the moment: "+str(item[1]))

    # print one line per entry in the hi-score list:
    for element in item:
        print(str(element)+"\t", end="")
        
    # new line after printing one entry:
    print()

hiScores2 = [      #  a list of lists
    [["Alex","Anderson"], 20000],
    [["Bert","Brianson"], 9999],
    [["Cat","Caterson"], 200]
    ]

# change one item inside a nested list:
hiScores2[2][1] = 2000

# example: print out hi-score list,
#          name & points, one per line
print(" version 2 of nested nested lists ")
for item in hiScores2:
    # item is 1 entry in the hiScores list,
    #    both name and points --- it's a list on its own.

    # print one line per entry in the hi-score list:
    for element in item:
        # element may be a list itself...

        if isinstance(element, list):
            # if element is a list, iterate through it:
            for word in element:
                print(str(word)+"\t", end="")
        else:
            # if element isn't a list:
            print(element)


