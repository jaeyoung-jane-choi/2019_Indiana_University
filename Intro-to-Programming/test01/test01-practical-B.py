


#B.(a)


def three_string(a,b,c):
    """given three strings will be returned by a new string of the three strings concatenated together

    string, string, string -> string """

    result =str(a)+str(b)+str(c)
    return result



#B.(b)

def bye_string(a):
    """given a string, returns a new string without first, last character of original 

    string -> string"""
    result = a[1:(len(a)-1)]
    return result


#B.(c)

def even_num(a):
    """given an integer if even returns True, if odd returns False

    int -> bool"""
    return int(a) % 2 == 0  
