howManyScoops = int ( input("how many scoops total?") )

jill = 0
jo   = 0
jane = 0

# as long as I don't have 0 scoops, continue:
while ( howManyScoops != 0 ) :

    # give 1 scoop to jill:
    jill = jill + 1
    print("jill got a scoop of icecream!")
    howManyScoops = howManyScoops - 1
    
    # give 1 scoop to jo:
    jo = jo + 1
    print("jo got a scoop of icecream!")
    howManyScoops = howManyScoops - 1
    
    # give 1 scoop to jane:
    jane = jane + 1
    print("jane got a scoop of icecream!")
    howManyScoops = howManyScoops - 1
    
if howManyScoops > 0 :
    print(" and " + str(howManyScoops) + " for me!")

print ("they ate all the scoops")
