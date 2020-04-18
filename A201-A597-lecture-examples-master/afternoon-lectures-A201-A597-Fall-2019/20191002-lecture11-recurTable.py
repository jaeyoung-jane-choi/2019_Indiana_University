# using recursion to print
#   one row of the multiplication table


# define recursive function
def printRow( i, j ):

    # define base case recursion stops here:
    #     i.e. when end-of-line is reached
    if i > 10:
        # reached end of line, i.e.:
        print()
        return

    # define recursive case:
    else:
        # do work for one level of recursion:
        n = j * i
        print ( "\t" + str(n), end="" )
        # prepare recursive call:
        i += 1
        # call function recursively:
        printRow( i, j )

def printTable( j ):

    # define base case, i.e. when end-of-table is reached
    if j > 10:
        return
    else:
        # do work for 1 level of recursion:
        printRow( 1, j)
        j = j + 1
        # call recursion:
        printTable ( j )

