#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Reading Assignment 03", "Jaeyoung Choi(Jane Choi), "janechoi"



#B.1 

def toThePower(num1,num2):
    """ takes two numbers (x,y) and returns the value of x to the power of y	

    number, number ->number"""

    result = num1 ** num2
    return result


##############################    


#B.2

def quadruplicate(string):
	"""takes a string and returns the three copies of that string together  
	
	string -> string"""
    result = string *3
    return result


##############################    


#B.3


def subtract(num1, num2):
    """takes two numbers and returns the difference between them
	
    number, number -> number
    """
    result = num1-num2
    return result


##############################    


#B.5


def multiplicate(string, num):
    """takes a string and number , and returns copies of the string as much as the number
	
    string, number -> string
    """
    result = string * num
    return result 




############################################################    


#D

def kgswap(num):
    """takes a number(kg) and converts this number into the unit of pounds(lbs)

    number -> number """
    result = float(num) *2.2046
    return result 



def cmswap(num):
    """takes a number(cm) and converts this number into the unit of inches(in)

    number -> number """
    result = float(num) * 0.3937
    
    return result 


def BMI(weight, height):
    """takes the height(inch) and weight(lbs) and converts these to BMI 

    number, number -> number """
    result = float(((weight) / ((height)**2) )*703)
    return result 



print('This program swaps kilograms to pounds, Centimeters to foot, and cacluates the BMI for FEMALE')

kilogram = input('input the weight in kilograms(kg):')

centimeter = input('input the height in Centimeters(cm):')

print( str(kilogram)+' (kg) '+ ' is converted to ' + str(kgswap(kilogram)) + ' (lbs) '+
       ' ,and '+ str(centimeter) + ' cm ' + ' is convertend to '+ str(cmswap(centimeter))+' (inches) ')

print( ' The BMI is ' + str(BMI(kgswap(kilogram) , cmswap(centimeter)))+ '.')


