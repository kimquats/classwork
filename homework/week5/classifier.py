def is_string_int(s):
    """
    This function takes in the parameter s as a string and returns True
    if s can be safely converted to an int.  It returns False otherwise.
    """
    pass
    try:
        int(s)
    except ValueError:
        return False
    return True


def is_string_float(s):
    """
    This function takes in the parameter s as a string and returns True
    if s can be safely converted to a float.  It returns False otherwise.
    """
    pass
    try:
        float(s)
    except ValueError:
        return False
    return True
        

user_input = raw_input("What string do you want to know about? ")
if is_string_int(user_input):
    print user_input, 'is an int'
elif is_string_float(user_input):
    print user_input, 'is a float'
else:
    print user_input, "doesn't look like an int or a float"