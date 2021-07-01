#"A201 / Fall 2019", "Programming Assignment 04", Jaeyoung Choi(Jane Choi)/ janechoi

user_input1 = float(input("Please enter a temperature: "))
#user inputs a tempurature which is a number 


print('The converted temperature is:')


#this function converts f to C 
print(str(user_input1) +  'Fahrenheit ->'  +  str((user_input1-32)* 5/9) + 'Celsius')



#this function converts C to F
print(str(user_input1) +  'Celsius ->'  +  str((user_input1* 9/5) + 32 ) + 'Fahrenheit')




