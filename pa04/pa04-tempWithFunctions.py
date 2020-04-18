#"A201 / Fall 2019", "Programming Assignment 04", Jaeyoung Choi(Jane Choi)/ janechoi



#This function will convert celsius to farehneit'

def fromCtoF(num):
    """This function makes conversion from Celsius to Fahrehneit

    num-> num """

    #input Celsius number 

    result = (num* 9/5) + 32 #recieves a number and calculates to result

    #output Farhrehneit number 
    return result



####################################################################


#This function will convert farehneit to celsius
def fromFtoC(num):
    """This function makes conversion from Fahrehneit to Celsius

    num-> num """
    #input Farhrenheit number
    
    result = (num-32)* 5/9 #recieves a number and calculates to result

    #output Celsius number 
    return result 
