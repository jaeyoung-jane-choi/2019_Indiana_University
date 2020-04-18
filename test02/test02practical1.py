
#Jane Choi , janechoi


##1 

def addItemToList(l,i):
    """Recieves a list, item and append the item to the list

    list, string -> list """
    #the item is appended to the list 
    l.append(i)
    #returns the list 
    return l 

print("""Add as many items to the bicycle as you want. When you're done, enter
'nothing'.""")

#before the while loop .. we need
#a empty list 
itemlist = []
#the user input object 
user_input =''

while user_input != 'nothing':
    #while the user input is not nothing
    #ask the user input first (since our user input is '' at first )
    user_input = input('What do you want add to the bicycle now?')
    #now use the function addItemToList , and append the input 
    addItemToList(itemlist, user_input)
    
    print('Okay')

#since the itemlist includes nothing, for both length and list we substract the nothing value
itemlist.remove('nothing')

print( 'There are ' +str(len(itemlist))+ ' items added to the bicycle: ' +str(itemlist))


