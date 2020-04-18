
#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 08", Jane Choi, janechoi


#J



#a *character record* is a list of two-item lists where...

#The first item in each pair is the character,
#and the second is an integer representing how many times that character appears


#ex) [['K',1],['o',3],['k',1],['m',1],['?',1]]
#   There are one 'K' , there 'o's , one 'k', one 'm', and one '?'



def isInRecord(s,l): 
    """Takes one character & one character record, returns True when character is listed in character record

    string, list-> bool"""

    index = 0

    #while the index in smaller than the length of the list, 
    while index < len(l):

        #if the string is in the l[index]
        if s in l[index][0]:
            #it returns True 
            return True
        #if not seek the next index 
        else:
            index = index +1

    #and when the while loop ends, we return false, since it wasn't in the l
    return False 


#####################################################################

def addToRecord(s,l):
    """Takes one character &one character record, and adds an occurrence of that character to the character record.

    string, list -> list"""


    #the index starts at 0 
    index=0
    #copied the list just in case 
    newlist = l.copy()

    #while the index is smaller than the length of the list 
    while index < len(l):

        #we seek s in the l
        if s in l[index][0]:

            #and if it is in l, we add an amount to the frequency 
            newlist[index][1]= newlist[index][1]  + 1

            #and can stop looking, since there is no duplicates in this case
            #we break the loop by just returning the newlist 
            return newlist

        #if there is no s in the l[index],
        #we seek the next index 
        else:
            index = index +1

    #since the while loop hasn't breaked, we can just add it by append. 
    newlist.append([s,1])
    
    return newlist 
        


#####################################################################

def createRecord(s):
    """Takes any string, and returns out a new character record from that string

    str -> list"""
    

    #make a empty recordlist 
    recordlist=[]

    #append the first record, amount of 1 
    recordlist.append([s[0],1])
    
    #since we appended the first, the index needs to start at 1 
    index=1

    #while the index in smaller than the length : 
    while index < len(s):

        #we need a newindex to count for the recordlist 
        newindex = 0

        #this flag will indicate if the record includes s
        flag  = False

        #while the newindex in smaller than the length of the recordlist, 
        while newindex < len(recordlist):
            
            #if the s[index] is same as the recordlist[newindex]'s letter, 
            if s[index] == recordlist[newindex][0] :

                #we add a 1 to the letters amount 
                recordlist[newindex][1] = recordlist[newindex][1] + 1

                #and say that the flag is true: since we added it
                flag  = True
                #when it is added, we can break the while loop 
                break

            #when we can't add it, the flag is false 
            else:
                flag = False

            #now we see the next index 
            newindex = newindex + 1

        #seeing all the new indexs , we know that if
        #added -> flag is True (breaked the while loop)
        #not added -> flag is False (so we need to append it to the list)
        
        if flag == False:
            #we append the value in the list,
            #since we didn't have the same value in the list 
            recordlist.append([s[index],1])
                
        #now we look for the next index 
        index = index + 1

    #we return the recordlist 
    return recordlist 

        

#####################################################################
        

    
def frequencies(s,l):
    """Takes one character & one character record, returns the frequency associated with that character in the given character record


    string, list -> int"""


    #for all the list in  l : 
    for lists in l:
        #if there is the s in the lists[0] : 
        if lists[0] == s:
            #they return the amount of the frequency 
            return lists[1]
    #if not in all l, we return 0 
    return 0

            

        













    

    
