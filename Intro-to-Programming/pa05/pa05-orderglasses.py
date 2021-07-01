#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 05", Jane Choi, janechoi
#D


###################################################################

#This program is where the user inputs stuff 
print("""This is the Sunglasses Order Program.
Type your coices, and we'll print our your order.""")

user_input0 = input('Brand name:')

print('Please answer the following questions with Y for yes, N for no.')

user_input1 = input('Should we add Anti-reflective Coating?:').lower()

user_input2 = input('Should we add Polarized Filter Coating?:').lower()

user_input3 = input('Should we add Scratch Resistant Coating?:').lower()

user_input4 = input('Should we add Mirror Coating?:').lower()


print("Please choose one of the following tint color for lenses:")


user_input5 = input('Dark Gray, Teal, Amber or Green?').lower()

if user_input5 != 'dark gray' and user_input5 != 'darkgray'\
   and user_input5 != 'teal' \
   and user_input5 != 'amber' \
   and user_input5 != 'green': #if not above colors it will be dark gray with a printed comment
    user_input5 = 'Dark Gray'
    print("The tint color is not available. We'll make them Dark Gray.")

##################################################################


if user_input0 == '' :
    user_input0 = 'unspecified'#if the user inputed nothing, it will be unspecified
    

##################################################################
##################################################################

#the program results start to print out from  here! 
print("Your order for sunglasses is ready:")



print("--------------------------------------")

print("Brand name:" + str(user_input0) + '.')
#the inputted brand name will come out, if no name it will be unspecified 

print('Coating(s):')

if user_input1 == 'y':
    print('Anti-reflective Coating') #if y , print out the coatings 
if user_input2 == 'y':
    print('Polarized Filter Coating')

if user_input3 == 'y':
    print('Sratch Resistant Coating')

if user_input4 == 'y':
    print('Mirror Coating')


if user_input1 == 'n' \     #if all are no, the statement no coating comes out 
   and user_input2 == 'n'\
   and user_input3 == 'n'\
   and user_input4 == 'n':
    print('No coating')


print('Tint color:' + str(user_input5)+ '.') #the tint color is printed out

print("--------------------------------------")

