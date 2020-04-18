#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Programming Assignment 10", Jane Choi, janechoi


class ElectricScooter(object):
    """information about an electric scooter

    Attributes : nickname(str), payment(float), lockstatus(bool), useableminutes(float)"""


    def __init__(self):
        """constructor  method for ElectricScooter

        ElectricScooter -> none """
        
        self.nickname = '' #empty string 
        self.payment = 0.0 #before payment = 0 
        self.lockstatus = True  #at first always locked 
        self.useableminutes = 100.0 #always start with 100 minutes 
        

    def info(self):
        """returns nickname, usable  remaining minutes

        ElectricScooter -> string, float"""

        #returned automatically tuple but you can access it as string and float 
        return self.nickname, self.useableminutes
        
        
    def unlock(self, pnickname, ppayment):
        """returns string with current scooters status(remaining money, charge)

        ElectricScooter, str, float -> str  """

        #the parameters are the nickname,payment value 
        self.nickname = pnickname
        self.payment = ppayment 

        #if the usable minutes are below 10 minutes it refuses payment and is still locked 
        if self.useableminutes < 10 :
            print('This scooter has below 10 usable minutes.. It Refuses your payment')
            self.payment = 0.0
            self.lockstatus = True
            
        else:
            #if the usable minutes are over 10 minutes lock is unlocked 
            self.lockstatus = False
            current_status = 'The current payment is..'+str(self.payment) + ' The current usable minutes is..'+ str(self.useableminutes)
            

            return current_status #self payment & usable minutes are returned 


    def drive(self, pmiles):
        """decrements the usable minutes and payment by miles parameter

        ElectricScooter,float -> None """

        
        #if the payment is below 0 or usable minutes are under 10 min, you can't drive 
        if self.payment<=0 or self.useableminutes < 10 :
            print('Your payment is currently 0 or the charge is below 10 usable minutes.')


        else:
            self.useableminutes = self.useableminutes - (pmiles/10) #usable minutes are decremented 
            self.payment = self.payment - pmiles*0.01 #payment is decremented too
            current = 'The current payment is..'+str(self.payment) + ' The current usable minutes is..'+ str(self.useableminutes)

            return current

        

#1 min = 10 mile =0.1dollar 
#1 dollar = 10 min =100 mile 
#1mile = 0.01 dollar= 0.1 min

        
########################################################
####################MAIN PROGRAM########################
########################################################
            

bike1 = ElectricScooter()

bike2 = ElectricScooter()




        



