import sys # for sys.exit()

def enter_file():
    user_file = raw_input("What file to open (hit enter for catch.txt)? ")
    if not user_file:
        user_file = "catch.txt"
    return user_file

def split_string_into_list(userfile):
    values = []
    try:
        with open(userfile, 'r') as f:
        # Read a list of integers from a file
            text = f.read()
        # remove trailing whitespace
        # See: http://docs.python.org/library/stdtypes.html#str.rstrip
            text = text.rstrip()
        # split up string into an array, splitting on whitespace
        # See: http://docs.python.org/library/stdtypes.html#str.split
            values = text.split()
    except IOError:
        print "The file you have entered is invalid. Try again."
        split_string_into_list(enter_file())
    return values

stringvalues = split_string_into_list(enter_file())

# Convert those strings from the file to integers
intvalues = []
try:
    for x in stringvalues:
       intvalues.append(int(x))
except ValueError:
    print "The contents of the selected file are not composed solely of integers. Exiting."
    sys.exit()



while True:
    command = raw_input("Input one letter: h(elp), a(verage), p(rint), e(x)it")
    if command == 'h':
        help_text = {
            'a': 'print the average of all values',
            'p': 'print all the values',
            'h': 'print help text',
            'x': 'quit',
        }
        try:
            what_help = raw_input("Help on which command letter? ")
            print help_text[what_help]
        except KeyError:
            what_help = raw_input("You have entered an invalid command letter. Try again. ")
        # a dictionary of help text
        
        
    elif command == 'a':
        try:
            the_sum = 0
            for x in intvalues:
                the_sum += x
            average = the_sum / float(len(intvalues))
            print "The average is: %f" % average
        except ZeroDivisionError:
            print "The file you have chosen contains no integers. Exiting."
            sys.exit()
    elif command == 'p':
        print intvalues
    elif command == 'x':
        # Forcibly exit.  We could also just use 'break' here.
        sys.exit()
    else:
        print "Invalid command: %s" % command
