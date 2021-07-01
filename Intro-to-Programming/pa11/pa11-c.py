#"A201 / Fall 2019", "Programming Assignment 11", Jane Choi, janechoi



class Bike(object):
    """represents a Bike 

    attributes : name(str), tire_pressure(float) , use(bool)"""

    #default is Celerifere, 0 
    def __init__(self,str1 = 'Celerifere', str2 = None ):
        """initializes with given name and pressure
        if name is left out, assumed to be 'Celerifere'
        if pressure is left out, assumed to be 0 

        Bike, str or float -> None
        Bike,str, float -> None """


        #if the str2 is not inside : 
        if str2 == None:

            #if the str1 is a string it is a name 
            if isinstance(str1, str):

                self.name =str1
                #and the pressure is the default value 0
                self.tire_pressure = 0.0
            #if the str1 is not a string , it means it is the pressure 
            else :
                #so the name is the default value 
                self.name = 'Celerifere'
                self.tire_pressure = str1
                
        #if both values are present 
        else :
            #the name is str1, and the tire_pressure is str2 
            self.name =str1
            self.tire_pressure = str2

        #if the tire pressure is under 0 , it is fixed to 0
        if self.tire_pressure <0 :
            self.tire_pressure = 0

        #as a default the bike use is True 
        self.use = True 


            
    def status(self):
        """displays a string form of the bikes name and tire pressure

        Bike -> None"""

        #print out the status of the Bike
        print("The bike's name is.."+ self.name +
              '\n and the tire pressure is..'+ str(self.tire_pressure))


    def ride(self, pdistance):
        """takes the distance and displays if it can be rided  

        Bike, float -> None"""

        #if the use is True , we can ride it 
        if self.use == True :
            
            #if the distance is under 1 we can't ride it 
            if pdistance < 1:
                print('The bike can not ride a distance less than 1')

                
            #if the distance is lower than tire pressure*1000
            elif pdistance <= self.tire_pressure*1000 :
                #the tire pressure is reduced 
                self.tire_pressure = self.tire_pressure - pdistance/1000 
                print('The tire pressure has reduced to..' + str(self.tire_pressure))

                
            #if it is over the tire pressure,
                #we can't ride the bike
            elif pdistance > self.tire_pressure*1000:
                print('The bike does not have enough tire pressure to move')

            
        #when the use status is False 
        else:
            print('The bike is not usable, the tire has exploded')

        #the function returns the status
        return self.status()
            

        


    def repressurize(self, padd):
        """takes a float to add some amount of pressure into the tire's pressure

        Bike, float -> None"""

        #when the self use is True 
        if self.use == True:

            #if the padd is under 1 , don't accept it 
            if padd < 1 :
                print('The bike can not be repressurized with an amount less than 1 ')

            #if not , the self pressure is added with the add 
            else:
                self.tire_pressure = self.tire_pressure +padd
                print('The bike tire pressure has been added with the value')

                #after the add if the pressure is over 100, change the use status to False
                if self.tire_pressure > 100:
                    print('But..the bike tire has been exploded due to too much pressure')
                    self.use = False 
                
        #when the use status is False we can't use the bike 
        else:
            print('The bike is not usable since the tire has exploded')

        #the function returns the status 
        return self.status()    
            

    























        
