
#Jane Choi , janechoi

#(a)

def newstring(l):
    """given a list of strings , returns a new strng containing all the characters in the strings of list concatenated together  

    list of strings ->string """

    #new is the new string to put 
    new=''

    #for all the items in the list 
    for strings in l :
        #concatenate the items in the list together 
        new += strings
    return new
        


#(b)

def modifinglist(l):
    """given a list of strings, modify the list with the second&last element removed

    list of srings-> None """

    #when the length of the list is larger than 3 
    if len(l) > 3 :
        #delete the second value 
        del l[1]
        #delete the last value 
        del l[len(l)-1]
    #if the length is 2 
    elif len(l)  == 2  :
        #only delete the second value 
        del l[1]
    #if the lenght is 1
    elif len(l) ==1 :
        #delete the first value 
        del l[0]

