import sys, os
from random import *


def is_word(text):
    """  
    Determines whether or not a given string contains only alphanumeric characters
    with or without apostrophes, and with no spaces or other punctuation.

    Parameters:
    text - An english string which will be determined to be a word or not.

    For a string containing at least one alphanumeric character, return True.
    
    For a string containing at least one alphanumeric character and any number of 
    apostrophes, return True.

    For everything else, return False.

    """
    if text == "'":
        return False
    #for contractions
    elif text.replace("'", "").isalnum():
        return True
    return False

def split_words_and_punctuation(text):
    """
    Converts a string of text into a list containing the individual words and punctuation
    marks in the input string.

    Parameters:
    text - An English string which will be used to generate the list.

    This function should return a list containing strings, with each string being
    a word or a punctuation mark.
    """
    words = []
    currentword = ""
    for i in range(len(text)):
        c = text[i]
        if i+1 < len(text):
            next = text[i+1]
        else:
            next = None
        if c.isalnum() or (c == "'" and next != None and next.isalnum()):
            #The second part of the or is for contractions, which should
            #appear as a single word
            currentword += c
        elif c.isspace():
            if currentword != "":
                words.append(currentword)
            currentword = ""
        else:
            if currentword != "":
                words.append(currentword)
            words.append(c)
            currentword = ""
    if currentword != "":
        words.append(currentword)
    return words

def add_word(d, word, next_word):
    """ 
    Takes a dictionary of {word:list of next words} pairs and appends a word
    to the list of next words for a given input word. 

    Parameters:
    d - A dictionary containing words.
    word - a key for a given word in the dictionary.
    next_word - the word to append to the list of next words for a given key
    in the dictionary.

    This function does not return anything; it merely appends to d
    """
    if word in d:
        d[word].append(next_word)
    else:
        d[word] = [next_word]

def table_of_next_words(text):
    """
    Creates a table of what words we have seen after other words.

    Parameters:

    text - an English string with which we will create our table.
    
    Returns a dictionary where:
    
    * Every word or punctuation in the given text is a key, and the
      associated value is a list of every word that follows the key in
      the given text.

    * If one word follows another more than once, it appears in the
      list more than once.

    * The beginning of the text is marked by a special "word" denoted by
      the python value None, as is the end of the text.

    For example, the output for the text "a a b c a b" is:
    { None: ['a'],
      'a': ['a', 'b', 'b'],
      'b': ['c', None],
      'c': ['a']
    }
    """
    # word_table = {}
    # make a dictionary. split words and punc in text, assign to wordslist. 
    # take wordslist, and for each word/punc in the list, if the next word is a word,
    # add it is a paired 
    word_table = {}
    words_list = ['']
    words_list = split_words_and_punctuation(text)
    prev_word = ''
    last_word = ''
    for this_word in words_list:
        if is_word(prev_word):
            add_word(word_table, prev_word, this_word)
        prev_word = this_word
    #i = -1
    #while is_word(words_list[i]) == False:
    #    i -= 1
    #last_word = words_list[i]
    for i in reversed(words_list):
        if is_word(i):
            last_word = i
            break
    if len(words_list) > 0 and len(last_word) > 0:
        add_word(word_table, None, words_list[0])
        word_table[last_word].append(None)
    else:
        add_word(word_table, None, None)
    return word_table

        


def pick_random_element(lst):
    """ Return a random element in the given list lst."""
    pass
    import random
    random_element = random.choice(lst)
    return random_element


def make_text(table):
    """
    Given a table of next words, construct a random text with similar
    word frequencies.

    Parameters:

    table - a dictionary of the form word->list of next words seen --
    the same form that comes out of the function table_of_next_words

    Returns a string where:

    * The first word is randomly chosen from the list table[None]

    * Every further word is randomly chosen from the list gotten by
      looking up the previous word

    * When the next word is chosen to be None, there is no next word
      and the words chosen so far are returned as a string.

    * Every word is preceded by a space.

    * No punctuation is preceded by a space.
    
    """
    # new text is a list. First word is value for key None. while current_word != None, if is_word(current_word) == True, new_text.append(current_word + ' '), elif is_word append current word to new_text, where current_word = pick_random_element(dict[new_text[-1]])
    new_text = []
    new_text.append(table[None])
    current_word = ''
    while current_word != None:
        current_word = pick_random_element(new_text[-1])
        if is_word(current_word):
            new_text.append(' ' + current_word)
        else:
            new_text.append(current_word)
    text = ''
    for i in new_text:
        text += new_text[i]
    return text
 

def main(argv):
    if len(argv) == 0:
        filename = "alice.txt"
    else:
        filename = argv[0]
    with open(filename) as f:
        text = f.read()
        table = table_of_next_words(text)
        print make_text(table)

if __name__ == '__main__':
    main(sys.argv[1:])
