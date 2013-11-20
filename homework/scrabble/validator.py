import board
import samples

def validate(d):
    """
    Returns True if the board is a valid Scrabble state, False if not.

    Parameters:
    d - a board in the array-of-arrays format.
    """
    if are_squares_connected(d) and check_all_words(d):
        return True
    else:
        return False

def are_squares_connected(d):
    """
    For a given board, checks to see if each played letter is on a played square or playable
    square.

    Parameters:
    d - a board in the array-of-arrays format.
    """
    mark_connected_squares(d)
    state = ''
    for row in d:
        for square in row:
            if square['letter'] != None and square['state'] != 'playable' or 'played':
                state = 'bad'
                break
            elif square['letter'] != None and square['state'] == 'playable' or 'played':
                state = 'good'
        if state == 'bad':
            break
    if state == 'good':
        return True
    else:
        return False

def check_all_words(d):
    """
    Returns true if all words on the board are legal words (present in the game's dictionary)

    Parameters:
    d - a board in the array-of-arrays format.

    """
    rows, columns = get_rows_and_columns_as_strings(d)
    played_words = get_all_words(rows, columns)
    with open('word_list.txt', 'r') as f:
        wordlist = f.read()
        wordlist = wordlist.splitlines()
    state = ''
    for word in played_words:
        word = word.upper()
        if word not in wordlist:
            state = 'invalid'
            break
        else:
            state = 'valid'
    if state == 'valid':
        return True
    else:
        return False

def get_rows_and_columns_as_strings(d):
    """
    For a given input board, returns two lists, one containing the letters in each column as strings, and one contaning the letters in each row as a string.

    Parameters:
    d - a board in the array-of-arrays format.

    """

    rows = []
    columns = []
    for x in range(len(d)):
        row = ''
        for y in range(len(d[x])):
            if d[x][y]['letter'] != None:
                row += d[x][y]['letter']
            else:
                row += '.'
        rows.append(row)
    for y in range(len(d)):
        column = ''
        for x in range(len(d[y])):
            if d[x][y]['letter'] != None:
                column += d[x][y]['letter']
            else:
                column += '.'
        columns.append(column)
    return (rows, columns)

def get_all_words(rows, columns):
    """
    For a tuple of a list of strings(one list containing each row represented as a string, one containing each column represented as a string), convert each column and each row into a list of words, defined as more than one letter in adjacent positions.

    Parameters:

    rows - a list containing the letters in each row represented as a string.
    columns - a list containing the letters in each column represented as a string.


    """
    words = []
    for row in range(len(rows)):
        current_row = rows[row].split('.')
        for word in current_row:
          if len(word) > 1 and word.isalpha():
              words.append(word)
    for column in range(len(columns)):
        current_column = columns[column].split('.')
        for word in current_column:
          if len(word) > 1 and word.isalpha():
              words.append(word)
    return words

    

def mark_connected_squares(d):
    """
    For a given board, marks all squares adjacent to played squares as playable squares.

    Parameters:
    d - a board in the array-of-arrays format.

    """
    for x in range(len(d)):
        for y in range(len(d[x])):
            if d[x][y]['state'] == 'played':
                for offset in range(-1, 2):
                    if d[x+offset][y]['state'] != 'played':
                        d[x+offset][y]['state'] = 'playable'
                    if d[x][y+offset]['state'] != 'played':
                        d[x][y+offset]['state'] = 'playable'

#remember to write helper functions!
