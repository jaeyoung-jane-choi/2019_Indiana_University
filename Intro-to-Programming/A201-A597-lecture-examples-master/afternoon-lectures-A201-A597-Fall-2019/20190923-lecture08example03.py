howManyScoops = int ( input("how many scoops total?") )

minnie = 0



# set up the while loop:

print("debug, before while loop begins, myIdex = " + str(myIndex) )
while  ( myIndex < len(myString) )  :

    print("debug, before printing, myIdex = " + str(myIndex) )

    # print one character from myString:
    print(  myString[myIndex] )
    print("debug, after printing, myIdex = " + str(myIndex) )
    
    # go to the next character,
    # i.e. increment myIndex:
    myIndex  = myIndex + 1
    print("debug, after incrementing, myIdex = " + str(myIndex) )
    
    
    # block to execute if above condition is true
    
