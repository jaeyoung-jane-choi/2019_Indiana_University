#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 13", Jane Choi(Jaeyoung Choi) ,janechoi

choice = None
scores =[]

while choice != "0"  :
    try :
      #  print('try')
        file = open('scores.txt', 'r+')
        newscores = file.readlines()
        #print(newscores)
        scores =[]
        #for the lines in the newscores they are all string
            #by using eval, make them tuples 
        for line in newscores:
            #print(line)
            #strip out the \n
            line.strip('\n')
            line = eval(line) #tuple 
         #   print(line)
         #   print(type(line))
        
            scores.append(line) #append to new scores list 
         
          #  print(scores)
        
       # print(scores)
        
    except:
      #  print('except')
        file = open('scores.txt', 'w')
        
    

   
        
    print(
    """
    High Scores 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    """
    )

    choice = input("Choice: ")

    if choice == "0":
        print("Good-bye.")

    # display high-score table
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")

        for lines in scores:
            
            print(lines)
        

# add a score
    elif choice == "2":
        
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?: "))
        
        entry = (score, name)
      #  print(scores)
 
        scores.append(entry) #append new name to scores list 

                
        #print(scores)
        scores.sort(reverse = True) #sort the scores 
       # print(scores)

        
        scores = scores[:5]
             # keep only top 5 scores
       # print(scores)
        
        file.seek(0) #make the location 0 
        
        file = open('scores.txt', 'w+')
        for lines in scores:
           #open the file to append new lines 
            file = open('scores.txt', 'a+')
            #print(lines)
            #print(file.tell())
            file.write((str(lines) +'\n'))
           # print('writing')
           # print(file.tell())
            
            read = file.read()
            #print(read)

            #close the file 
            file.close()
             
        

    
# some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")
        print("list of high scores", scores)

    
    
print()
# exit

    




    
