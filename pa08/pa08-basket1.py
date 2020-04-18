
#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 08", Jane Choi, janechoi


########################################################################


#D


print("Add as many items to the basket as you want. When you're done, enter 'nothing'.")


#we need 2 variables, a user_input and a list named basket 
user_input=''
basket = []


#while the user_input is not nothing, ask the input 
while user_input != 'nothing':

    
    user_input = input('What do you want to put into the basket now?')
    print('Okay.')

    #when the userinput is not nothing, we add the input to the basket list 
    basket.append(user_input)

#we now remove nothing from the list since it is appended 
basket.remove('nothing')

#print out the length of the list and items inside 
print('There are '+ str(len(basket)) + ' items in the basket: ' + str(basket) )


