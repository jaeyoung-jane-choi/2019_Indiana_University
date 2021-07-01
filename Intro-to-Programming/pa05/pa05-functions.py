#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 05", Jane Choi, janechoi


###################################################################

#A


def contains_letter(string):
    """This function takes a string and returns TRUE if it has at least one alphabtic letter, and FALSE if otherwise.

    string ->  bool"""
     
    index = 0 #This is the counter of the index
        
    while (index < len(string)):
        result = string[index].isalpha() #A T/F statement becomes the result
        
        if result == True: 
            
            return result #if the result is true, stops the loop and retuns result
        
        else :index = index + 1 #if false counter +1 
        
    return result 

    
        

###################################################################

#B

def contains_only_digits(string):
    """This function takes a string and returns TRUE if all characters of string are integers and FALSE for otherwise"

    string -> bool"""
    
    index= 0 #the index is the counter
    
    while (index<len(string)): #checking each index
        if (string[index] not in '1234567890'): #if the string index is not in numbers 
            return False #it will stop and return False 
        else: index = index + 1 #if there is a number it will seek the next index 
    return True #if the while statement ends , that means there are only numbers / blank space => TRUE















    
