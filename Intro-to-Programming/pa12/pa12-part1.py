


#"A201 / Fall 2019", "Programming Assignment 12 part I", Jane choi, janechoi

class Thing(object):
    """represents physical objects in the game

    Attributes: name(str), location(str)"""

    
    #constructor method
    def __init__(self, pname, plocation):
        """constructor method accepting a name, location of the thing

        Thing, str, str -> None"""

        self.name = str(pname)
        self.location = str(plocation)

    #instance method
    def description(self):
        """returns a string that describes the object 

        Thing -> str"""

        return 'The ' + self.name +  ' is ' + self.location
        

class Openable(Thing):
    """represents physical objects that can be opened (subclass of Thing)

    Attributes : is_open(bool) """

    def __init__(self, pname, plocation, popen = False ):
        """constructor method accepting a name, location, whether is open 

        Openable, str,str, bool -> None """
        #inherits superclass parameter values
        super().__init__(pname, plocation)
        
        self.is_open = popen

    def description(self):
        """returns a string that describes the object 

        Openable -> str"""
        
        #if opened 
        if self.is_open == True :
            return 'The ' + self.name  +' '+ self.location + ' is open'

        #when closed
        else:
            return 'The ' + self.name  +' '+ self.location + ' is closed'

    def try_open(self):
        """returns the attempt of opening an object(False when object is already open)

        Openable -> bool"""
        #if opened status, try_open is False 
        if self.is_open == True:
            return False
        #when closed, try_open is True
        #and now the open status is changed to open(true)
        else:
            self.is_open = True 
            return True

class Lockable(Openable):
    """represents physical objects that can be unlocked and opened(subclass of Openable, Thing)

    Attributes: is_locked(bool), key(Thing)"""

    #constructor method 
    def __init__(self, pname , plocation, pkey, popen = False, plock= False):
        """constructor method accepting a name, location, whether is open , whether is locked

        Lockable, str,str, bool, bool -> None """

        #inherited from openable
        super().__init__(pname,plocation,popen)
    
        self.key = pkey
        self.is_locked = plock

    def description(self):
        """ returns a string that describes the obejct

        Lockable -> str"""
        #when opened, unlocked 
        if self.is_open == True and self.is_locked == False:
            return 'The ' + self.name  +' ' + self.location + ' is open'
        #when closed, unlocked
        elif self.is_open == False and self.is_locked == False:
            return 'The ' + self.name  +' ' + self.location + ' is closed but unlocked'

        else: #when open, locked & when closed, locked
            #when locked (no matter with open status)
            return 'The ' + self.name  +' ' + self.location + ' is locked'

    def try_open(self):
        """fails to open the object if the object is locked, returns the attempt of opening an object(False when object is already open)

        Lockable -> bool"""
        #when locked, can't open 
        if self.is_locked == True:
            return False
        #when unlocked, try open is inherited from openable 
        else:
            #if unlock, open -> false
            #if unlock, close -> true 
            return super().try_open()

    def try_unlock_with(self, pthing):
        """returns the attempt of unlocking an object(False when object is already unlocked)

        Lockable, Thing -> bool"""

        #when unlocked, can't unlock -> false
        if self.is_locked == False: #when unlocked
            return False
        #when locked 
        else:
            #if the key is right 
            if self.key == pthing :
                #change lock state to unlock(false)
                self.is_locked = False
                
                return True
            #when key is wrong 
            else:
                #can't unlock
                return False


            
####################################################################
##################MAIN PROGRAM####################
####################################################################


print('--------------------------------------------------------------------------------')
print("***First, let's test the Thing class***")

print("\n #### a house_key (Thing) ")

print("\n Creating house_key with name 'front door key' and location 'in your jacket pocket'...")

house_key = Thing("front door key", "in your jacket pocket")
print(house_key.description())

print('-----------------------------------------')
print("\n #### a rusty_key (Thing) ")

print("\n Creating rusty_key with name 'rusty key' and location 'in your jeans pocket'...")

rusty_key = Thing("rusty key", "in your jeans pocket")
print(rusty_key.description())


print('-----------------------------------------')
print("\n #### a tiny_key (Thing) ")

print("\n Creating tiny_key with name 'tiny key' and location 'in the back yard'...")

tiny_key = Thing("tiny key", "in the back yard")
print(tiny_key.description())

print('--------------------------------------------------------------------------------')

print("***Now, let's test the Openable ***")

print("\n #### a window (Openable) ")

print("\n Creating window1 with name 'large window' and location 'in the south wall' , and open state True...")
window1 = Openable("large window", "in the south wall", True)
print(window1.description())

print('\n Attempting to open window1...')

print('window1.try_open() returned the value ' + str(window1.try_open()))
print(window1.description())

print('-----------------------------------------')
print("\n #### a book (Openable)")

print("\n Creating book1 with name 'Harry Potter ' and location 'on the bookshelf' , and default open state...")
book1 = Openable("Harry Potter", "on the bookshelf")
print(book1.description())

print('\n Attempting to open book1...')

print('book1.try_open() returned the value ' + str(book1.try_open()))
print(book1.description())


print('--------------------------------------------------------------------------------')


print("***And now, let's test the Lockable ***")

print("\n #### a door (Lockable) ")

print("\n Creating door1 with name 'door' and location 'at front of the house' ,key house_key,  open state False, and locked state True...")
door1 = Lockable("door", " at front of the house ", house_key,False, True) 
print(door1.description())

print('\n Attempting to open door1...')

print('door1.try_open() returned the value ' +str(door1.try_open()))
print(door1.description())

print('\n Attempting to unlock door1 with rusty_key...')
print('door1.try_unlock_with(rusty_key) returned the value ' + str(door1.try_unlock_with(rusty_key)))
print(door1.description())


print('\n Attempting to unlock door1 with house_key...')
print('door1.try_unlock_with(house_key) returned the value ' + str(door1.try_unlock_with(house_key)))
print(door1.description())


print('\n Attempting to open door1...')
print('door1.try_open() returned the value ' +str(door1.try_open()))
print(door1.description())
print('-----------------------------------------')
print("\n #### a diary (Lockable) ")

print("\n Creating my_diary with name 'diary' and location 'under clothes' ,key tiny_key,  open state True, and default locked state...")
my_diary =Lockable("diary", "under clothes", tiny_key, True)
print(my_diary.description())

print('\n Attempting to open my_diary...')
print('my_diary.try_open() returned the value '+ str(my_diary.try_open()))
print(my_diary.description())

print('\n Attempting to unlock my_diary with tiny_key...')
print('my_diary.try_unlock_with(tiny_key) returned the value ' +str(my_diary.try_unlock_with(tiny_key)))
print(my_diary.description())

print('-----------------------------------------')
print("\n #### an ancient treasure chest (Lockable) ")

print("\n Creating chest with name 'ancient treasure chest' and location 'at the bottom of the sea' ,key rusty_key,  and default open state and locked state...")
chest =Lockable("ancient treasure chest", "at the bottom of the sea", rusty_key)
print(chest.description())


print('\n Attempting to unlock chest with house_key...')
print('chest.try_unlock_with(house_key) returned the value ' +str(chest.try_unlock_with(house_key)))
print(chest.description())

print('\n Attempting to unlock chest with rusty_key...')
print('chest.try_unlock_with(rusty_key) returned the value ' +str(chest.try_unlock_with(rusty_key)))
print(chest.description())


print('\n Attempting to open chest...')
print('chest.try_open() returned the value ' +str(chest.try_open()))
print(chest.description())



