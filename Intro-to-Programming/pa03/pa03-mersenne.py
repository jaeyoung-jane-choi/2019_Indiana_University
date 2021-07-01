#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Reading Assignment 03", "Jaeyoung Choi(Jane Choi), "janechoi"



#######################################################################



#C.1 


def mersenne(num):
    """takes an input of a number and outputs the number 2**n-1

    int -> int """
    result = (2**int(num)) -1
    return result 






##############################    





#C.2



#user_input1,user_input2,user_input3  = input('input 3 numbers:').split()

user_input1 = input('input the first number of the three numbers:')

user_input2 = input('input the second number of the three numbers:')

user_input3 = input('input the third number of the three numbers:')



print( 'This is the Mersenne numbers of your input:'+ str(mersenne((user_input1)))
       + ',' +str(mersenne(user_input2)) +','+ str(mersenne(user_input3)) +'.' ) 


#######################################################################







