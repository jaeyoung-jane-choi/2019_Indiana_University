#"A201 / Fall 2019" (or "A597 / Fall 2019"), "Reading Assignment 04","Jane Choi", 'janechoi'

def factorial(n):
    """This function takes a number and returns the factorial of the number


    number -> number """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def factorial(n):
    """This function takes a number and returns the factorial of the number


    number -> number """
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	



print(factorial(5))


def factorial(n):
    """This function takes a number and returns the factorial of the number


    number -> number """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def print_n(s, n):
    """This function takes string and prints out the string as the amount of n


    string,number -> string """
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)


def do_n(a,n):
    """This function takes a function object and a number and calls the function as much as n times

    function, number ->  """
    
    if n <= 0:
        return
    print()
    do_n(a,n-1)

#cant figure out how to do the do_n function 
########################################################  

def f1(x):
    """This function takes a number and calls the same function f1 again

    number -> function"""
    return f1(x)


def f2(x):
    """This function takes a number and calls 1 smaller function f2 again

    number -> function"""
    return f2(x-1)

def f3(x):
    """This function takes a number and calls the 1 smaller function f3 until the number reaches 0

    number -> number"""
    if x == 0:
        return 55
    else:
        return f3(x-1)
def f4(x):
    """This function takes a number and calls the 1 smaller function function f4 again and adds 5 until the number reaches 0

    number -> function"""
    if x==0:
        return 0
    else:
        return f4(x-1)+5



########################################################  



def f3(x):
    """This function takes a number and calls the 1 smaller function f3 until the number reaches 0

    number -> number"""
    if x == 0:
        return 55
    else:
        return f3(x-1)
def f4(x):
    """This function takes a number and calls the 1 smaller function function f4 again and adds 5 until the number reaches 0

    number -> function"""
    if x==0:
        return 0 #base case
    else:
        return f4(x-1)+5  #recursive case


def factorial(n):
    """This function takes a number and returns the factorial of the number


    number -> number """
    if n == 0:
        return 1 #base case
    else:
        return n * factorial(n-1)#recursive case


########################################################  



















