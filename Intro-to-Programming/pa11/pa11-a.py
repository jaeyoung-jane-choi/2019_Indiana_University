#"A201 / Fall 2019", "Programming Assignment 11", Jane Choi, janechoi


class Bike(object):
    """represents a Bike 

    attributes : name(str), tire_pressure(float)"""

    #default is Celerifere, 0 
    def __init__(self,str1 = 'Celerifere', str2 = None ):
        """initializes with given name and pressure
        if name is left out, assumed to be 'Celerifere'
        if pressure is left out, assumed to be 0 

        Bike, str or float -> None
        Bike,str, float -> None """

        #if the str2 is not inside : 
        if str2 == None:
            print('str2 is None')

            #if the str1 is a string it is a name 
            if isinstance(str1, str):
                print(str1)
                print('str1 is a string')

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
                


            
    def status(self):
        """displays a string form of the bikes name and tire pressure

        Bike -> None"""

        #print out the status of the Bike
        print("The bike's name is.."+ self.name +
              '\n and the tire pressure is..'+ str(self.tire_pressure))

