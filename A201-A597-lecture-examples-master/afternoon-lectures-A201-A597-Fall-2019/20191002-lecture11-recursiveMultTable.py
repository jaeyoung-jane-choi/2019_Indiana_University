# print a multiplication table, recursively!
def printRow(column, row):
    if (column > 10):  # base case for row: end of columns!
        print()
        return
    else:
        n = row * column                # compute value to be printed
        print( "\t" + str(n), end="" )  # print the value
        column = column + 1             # go towards the end of recursion
        printRow(column, row)

def printTable( row ):
    if (row > 10):     # base case for table: end of rows!
        return
    else:                     # recursive case:
        printRow(1, row)      # compute & print 1 row
        row = row + 1         # go 1 step towards end
        printTable( row )     # call function recursively 
        
