#"A201 / Fall 2019", "Programming Assignment 11", Jane Choi, janechoi

class Player(object):
    """represents a player carrying a list of items

    attributes: name(str), max_items(int), items(list)"""

    def __init__(self, pname, pmax, plist):
        """initializes Player with name, max items carry avaliable, list of items

        Player , str, int, list -> None """

        #the player has to have... 
        self.name = pname
        self.max_items = pmax
        self.items = plist

    #the inventory shows the list of items 
    def inventory(self):
        """displays the players inventory items

        Player -> None """

        #when the item list is 0 , print out having no items 
        if len(self.items) == 0:
            
            print('The player has no items')

        #if not, print out the item list 
        else:
            print(self.items)


    def take(self, pitem):
        """takes an item and adds to the list when max_items is not exceeded

        Player, str -> None """

        #if adding one more item is exceeding the max item carry , say no to add 
        if self.max_items <= len(self.items):
            
            print('The player item list has been exceeded the maximum number of \n items the player can carry')

        #if not add the item to the list 
        else:
            self.items.append(pitem)

    def drop(self, pitem):
        """takes an item and removes from the list when item exists in the list

        Player, str -> None """

        #if the item is not inside the item list, can't drop it 
        if pitem not in self.items:
            print('The player does not carry the item')

        #if not, remove the item 
        else:
            self.items.remove(pitem)
    
        
        
        
