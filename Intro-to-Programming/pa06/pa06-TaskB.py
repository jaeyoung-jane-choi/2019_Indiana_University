
#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 06", Jane Choi, janechoi


#B 

#this function is for printing out the stars for each name
def printingstars(num):
    """user inputs a number and as much as that number a star is printed out

    int -> none"""
    
    stars = "*"*num

    
    #the result is the * multiplied by the inputed number 

    #returns the result for printingstars
    return stars 




#going to concatenate the output
output = ''   


while True:

    #the user inputs the name 
    user_input1 = input("Enter a name (To end the program enter 'stop'):")



    #if the input1 is not stop, the if statement continues
    if user_input1  != 'stop' :

        #the first input is called name 
        name = user_input1

        
        #the user now inputs the integer 
        user_input2 = input("Enter an integer:")
       
        #by using the function used above, we get the stars 
        star_num = printingstars(int(user_input2))

        
        #info is where thje name and stars are concatenated 
        info = str(name)+'    '+ str(star_num)
        
        #the output is concatenated with the new info 
        output = output +'\n'+ info 
        
    #if the user inputs stop, the process stops
    else: break 




#the result is printed out 
print('------------------------------------' + '\n'+
      output+'\n'+
      '------------------------------------'
      , end= '')



