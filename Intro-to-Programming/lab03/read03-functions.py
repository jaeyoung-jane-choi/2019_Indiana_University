# "A201 / Fall 2019" , "Reading Assignment 03", "Jaeyoung Choi(Jane Choi), "janechoi"


def square(num):
    """
    This function takes a number(float/int) into the square of the number

    num -> num
    """
    return num* num

print('the square of -6 is' +str(square(-6)))


###########################################################

def square2(num):
    """
    This function takes a number(float/int) into the square of the number and returns the result of it

    num -> num
    """
    result = num * num
    return result

###########################################################


result = 100
def square4(num):
    """
    This function takes a number(float/int) into the square of the number

    num -> num
    """
    result = num * num
    print("We're inside the function square4.")
    print("Here, the variable result has the value " + str(result))
    return result

print("Currently, the variable result has the value " + str(result))
print("We're about to call the function square4.")
print("square4(1.5) is " + str(square4(1.5)))
print("We've just finished calling square4.")
print("Now, result has the value " + str(result))


###########################################################




def double_dash(text):
    """
    This function takes a string and adds a dash inbetween

    string-> string
    """
    return text + '-'+ text 




def box_volume(width,height,depth):
    """
    This function takes a width, a height, and a depth and calculates the volume of a box with the dimensions

    num, num, num -> num
    """
    return width * height * depth



###########################################################










