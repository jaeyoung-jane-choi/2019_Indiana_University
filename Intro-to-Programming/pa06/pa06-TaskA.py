
#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 06", Jane Choi, janechoi


####A 


#the user inputs a number 
first_num= input("Enter a number (To end the program enter 'stop'):")

#the inputed value are made as the first start of max/min/sum number 
max_number = int(first_num)
min_number = int(first_num)
sum_number = int(first_num)


#while the block of codes are true:
while True:
    
    #user inputs another number or stop
    user_input= input("Enter a number (To end the program enter 'stop'):")

    #if the user inputs sth not stop : 
    if user_input != 'stop':

        #the sum number adds up 
        sum_number += int(user_input)


        #the max number compares with the user_input
        if int(user_input) >= max_number:
            
            #if the user_input is bigger than the max_number,
            #the max number is the user_input
            max_number  = int(user_input)
            
        elif int(user_input) <= min_number:
            #if the user_input is small or same as the min_number,
            #the min_number is the user_input
            min_number = int(user_input)
    
    #else is when the input is stop: 
    else: break
       


#print out the sum statement , max,  min statement 
print('The sum is: ' + str(sum_number) +'\n'+ 'The max number is: '+ str(max_number) + '\n'
      'The min number is: ' + str(min_number) )





