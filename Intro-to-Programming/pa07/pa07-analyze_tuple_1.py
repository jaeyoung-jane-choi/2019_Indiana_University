

#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 07", Jane Choi, janechoi


##A


def analyze_tuple_1(myTuple) :
    """takes a tuple and returns the length, type ,max of the tuple(if not tuple return -1,None,None)


    tuple -> tuple"""


    #if not a tuple, it would be not in loop and returned as -1,None,None
    while isinstance(myTuple ,tuple):

        #the first value is the length of the Tuple 
        first = len(myTuple)


        #The while loop needs: 
        counter = 0

        integer = ''

        
        #while the counter is smaller than the length, the while loop continues 
        while counter < len(myTuple) :


            isint = isinstance(myTuple[counter] ,int)

            #the result of the bool with be stored into 'integer' 
            integer = integer+ str(isint)
        
            #the counter increases 
            counter = counter + 1


        #mixed = mix of TrueFalse , string =  only FalseFalse ,
        #int = only TrueTrue

        #if there is true in the integer , it means it could be int or mixed :    
        if  'True' in integer:
            #if there is true and false in the integer, means that it is mixed 
            if 'False' in integer:
                
                second = 'mixed'
                third = None

            #if there is no false, it means that it is a int 
            else:
                second = 'integer'

                #easily get the max by using max function 
                third = max(myTuple)

        #there is no true in the integer, so only false meaning string 
        else:
            second = 'string'

            #to get the max length string we need another while loop 
            newcounter = 0
            
            maxvaluelen = 0

            
            while newcounter < len(myTuple):


                #if the element is larger than the maxvaluelen it would become
                #the new maxvaluelen 
                if len(myTuple[newcounter]) > maxvaluelen :
                    
                    maxvaluelen = len(myTuple[newcounter])
                    maxvalue= myTuple[newcounter]
                    newcounter = newcounter + 1
                    
                #if the maxvaluelen is larger, the counter goes up 
                else :  newcounter = newcounter + 1

            #the saved maxvalue is the longest string 
            third = maxvalue

                
        
        #now we make the result a tuple 
        result = (first,second,third)
            
            
        #return the result 
        return result


    return (-1, None, None )









