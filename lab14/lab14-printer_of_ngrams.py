#"A201 / Fall 2019", "Lab Task 14", Jane Choi, janechoi

#D

#n is the input of number of characters 
n = input('How many characters should I display at a time?')

#ask for what file want to disply 
user_input2 = input("What file should I display?")


while True:
    
    try:
        
        text = open(user_input2, 'r')
        text2 = open(user_input2, 'r').read()
        length = len(text2)
    
        while text.tell() < length :
            print(text.read(int(n)))
            
        else:
            text.close()

        #when over, break the true loop 
        break
    #when error 
    except:
        #print out messgae 
        print('There was an error working with that file. Please choose a different filename.')
        #and ask for input again 
        user_input2 = input("What file should I display?")
    
