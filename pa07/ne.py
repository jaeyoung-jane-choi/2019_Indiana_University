


def analyze_tuple1(myTuple):

    if isinstance(myTuple, tuple):
        first = len(myTuple)

        value = ''
        for element in myTuple:
            #print(element)
            new = isinstance(element, int)
            value += str(new)[0]
            print(value)

        if 'T' in value:
            if 'F' in value:
                second = 'mixed'
                third = None
            else:
                second = 'int'
                third = max(myTuple)

        else: 
            second = 'str'
            
            maxvalue = 0
            maxelement = ''
            for element in myTuple:
                if maxvalue < len(element):
                    maxvalue = len(element)
                    maxelement = element
            third = element
    

            
           
            
            
                
    else:
        first = -1
        second = None
        third = None 
       
    return first,second,third


tup = (1,2,3,4)
tup2 = (1,'j',2)
