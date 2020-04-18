#"A201 / Fall 2019", "Lab Task 14", Jane Choi, janechoi



#A

def bisect(pinput):
    """takes an argument of any type and returns half of the argument

    Any type -> same type as inputed"""

    try :
        
        result = pinput/2

    #when error occurs
    except :

        #try again 
        try:
            #num is the rounded number of length/2 of the tuple..list...
            num = round(len(pinput)/2)

            #the result is the showed until the num
                #if num =3, due to index the result will be shown value of 0,1,2
            result = pinput[:num]
            
        #when there is no length able to calculate 
        except:
            #the result is not modified 
            result = pinput

    return result

    

#B

def print_trigrams(pname):
    """takes a filename and opens the file with the given name, diplay contents and close the ifle 

    str-> str"""
    #open the file 
    text = open(pname, 'r')
    
    #open the file but this time with .read() to make it a string 
    text2 = open(pname, 'r').read()
    
    #calculate the length of the string text 
    length = len(text2)

    #while the text.tell(): the current location , is smaller than the length
    while text.tell() < length :
        #print 3 characters a time 
        print(text.read(3))
        
    #if the while loop is ended close the text
    else:
        text.close()


#C


def print_ngrams(pname,n):
    """takes a filename and positive integer n, diplay content n characters a time and closes file

    str, int -> str"""
    
    try: 
        text = open(pname, 'r')
        text2 = open(pname, 'r').read()
        length = len(text2)
    
        while text.tell() < length :
            #same as print_trigrams() but this times takes a n
            print(text.read(int(n)))
            
        else:
            text.close()
            
    #when error print out message 
    except:
        print("I'm sorry, but I could not find a file with that name.")
    


#E

def is_anagram(str1, str2):
    """takes two strings and returns True if the strings are anagrams of each other

    str, str -> bool """
    #letter1 is the list for the letters in the first string 
    letter1 = []
    #save all the letters in the first string to letter1 
    for letters in str1:
        letter1 += letters.lower() #make all alphabet in lower 
    #sort the letter1 
    letter1.sort()
    
    #letter2 is the list for the letters in the second string 
    letter2 = []
    
    for letters in str2:
        letter2 += letters.lower()
    letter2.sort()
    
    #return bool for whether same or not 
    return letter1 == letter2
        

#F



def find_anagrams(str1):
    """takes a string and returns a list of anagrams for that string from wordlist.txt

    str-> list """
    #new list for where to append anagram word 
    newlist = []
    #open the wordlist file 
    text = open('wordlist.txt','r')
    #read the file, and make it a string to get the length 
    text2 = open('wordlist.txt','r').read()
    length = len(text2)
    
    #while the length is larger than the current location 
    while text.tell() < length:
        #read each line 
        line = text.readline()
        #strip out the \n 
        line =line.strip('\n')

        #use the function, if true append 
        if is_anagram(str1, line) :
            newlist.append(line)
            
    #close the wordlist text 
    text.close()

    #return the appended newlist
    return newlist
    

    













    

    
