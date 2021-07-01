

#######PROF ANSWER

#get first user input
#using a counter

num_of_words = 0
total_letters = 0
user_input=''


while num_of_words < 5  and user_input != 'done':
    
    user_input = input('plz enter a word (enter done when done):')

    
    current_length = len(user_input)
    total_letters = total_letters + current_length

       
    num_of_words = num_of_words + 1


    
print('You have entered ' + str(total_letters)+ 'letters')
