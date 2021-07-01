# printout the 10 x 10 multiplication table
#
# we do not want a "hard-coded" table such as:
# print(" 1  2  3  4  5  6  7  8  9  10")
# print(" 2  4  6  8 10 12 14 16 18  20")
# ...

# always start with a plan, e.g. pseudocode
#     or flow charts, etc.
# BEFORE you start writing any Python code.

# we notice there's repetition in the table,
#   both vertically as well as horisontally
#

# repeat for every line in the table:
#     repeat incrementing a number:
#     within each line, repeat:
#         printing out  n

# initialize variables for row and column:
row = 1
column = 1

while (row < 11) :
# as long as the row is < 11, we'll repeat...

    while (column < 11):
    # as long as the column is < 11, we'll repeat...
    
        n = row * column

        # to align the table,
        #    always put a " " in front of numbers < 10
        if (n < 10) :
            print(" ", end="")
            
        # print number, but don't go to new line:
        #   we modify print()'s behavior by changing
        #   its  end  argument, i.e. don't go to new line!
        # we add a space after each number
        print (str(n) + " ", end="")
        column += 1
        
    # prepare new row:
    row += 1
    # restart from column 1 for the new row:
    column = 1
    # print to go to new line:
    print()





