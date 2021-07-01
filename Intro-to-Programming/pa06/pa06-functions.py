
#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 06", Jane Choi, janechoi

#C


def sum_all_digits(string):
    """takes a string and returns the sum of all digits in the string 

    str-> int """
    
    
    #n is the index for the function 
    n = 0

    #sum digits is the sum of all digits inside string 
    sum_digits = 0


    
    #n starting from 0, when n is smaller than the length of the string,
    #the loop will contiune 
    while  n < len(str(string)):
    
        #this print showed the index of the string 
        #print('index is ' +str(string)[n]


        #if the index  outcome has digits inside: 
        if str(string)[n] in ('1234567890') :

            #the sum will be added up 
            sum_digits += int(str(string)[n])

            #and the next index is called 
            n =  n + 1

        #if the index outcome is not a digit, the next index is called 
        else : n = n + 1

    #the function returns the sum of all digits inside the string    
    return sum_digits









###########################################################################


#D 


#this function recieves two arguments of any type!

def swapTwoNumbers(num1,num2):
    """this function revieves two argument and returns the swaped values

    any type arg, any type arg -> tuple """

    
    #returns the switched version 
    return num2, num1
    

















