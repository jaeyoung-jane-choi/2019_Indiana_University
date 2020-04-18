# print out the 10 x 10 multiplication table
#
# we don't want to "hard code" the output table as in:
# print("1 2 3 4 5 6 7 8 9 10")
# print("2 4 6 8 10 12 14 16 18 20")
#
# begin with a plan!
#   pseudocode or flow charts
# BEFORE writing ANY Python code.

# start of the algorithm: initialize variables
row = 1
column = 1

# repeat until row reaches 10 (included)
while ( row <= 10 ) :
    # repeat until column reaches 10 (included)
    while ( column <= 10 ) :

        n = row * column
        # print a number, spaced from the previous number,
        #      but don't go to new line afterwards:
        if (len(str(n)) == 1) :
            #  we're going to provide padding to shorter numbers:
            print( "  " + str(n), end="")
        else:
            print( " " + str(n), end="")            
        # we need to go to the next column:
        column = column + 1

    # end of all columns, print a "new line" character:
    print("\n")
    # go to the next row:
    row = row + 1
    # restart numbering columns from 1:
    column = 1
