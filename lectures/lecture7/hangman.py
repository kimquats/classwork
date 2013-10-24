WRONG_GUESSES_ALLOWED=5

right_guesses = ""
wrong_guesses = ""

def hangman(word):
    """
    Requires word to be a string

    Repeats asking the player for a letter and telling the player whether their
    guess is in the word.

    If the player guesses right, the position(s) of the letter in the word is
    revealed.

    If the player guesses wrong a number of times, the player is informed that
    they lost.

    If the player guesses all the letters in the word, informs the player that
    they have won.
    """
    global WRONG_GUESSES_ALLOWED
    global right_guesses
    global wrong_guesses
    while WRONG_GUESSES_ALLOWED != 0 and word != display_word_with_guesses(word, right_guesses):
        print display_word_with_guesses(word, right_guesses)
        print "Available letters:" + letter_pool(right_guesses, wrong_guesses)
        print "Guesses remaining:" + str(WRONG_GUESSES_ALLOWED)
        guess = ask_for_letter(right_guesses, wrong_guesses)
        if guess in word:
            print "You have guessed correctly!"
            right_guesses += guess
        else:
            print "You have guessed incorrectly!"
            wrong_guesses += guess
            WRONG_GUESSES_ALLOWED += -1
    if WRONG_GUESSES_ALLOWED == 0:
        print "Game over!"
    else:
        print "You win!"
    


   #     print letter_pool(right_guesses, wrong_guesses)

    # We want to keep around a set of wrong_guesses, and a set of right_guesses.

    # Write a while loop (that stops when either the word is complete, or there
    # have been five wrong guesses) to keep asking the player for a guess, and
    # processing that guess.


def letter_pool(right_guess, wrong_guess):
    """
    Requires right_guesses to be a string of letters the player has guessed
    before correctly, and wrong_guesses to be a string of letters the player has
    guessed before incorrectly.

    Returns the alphabet minus any letter that has been guessed before
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    guesses = right_guess + wrong_guess
    for letter in guesses:
        if letter in alphabet:
            alphabet = alphabet.translate(None, letter)
    return alphabet


def ask_for_letter(right_guesses, wrong_guesses):
    """
    Requires right_guesses to be a string of letters the player has guessed
    before correctly, and wrong_guesses to be a string of letters the player has
    guessed before incorrectly.

    Asks the player for a letter.

    If the input is exactly one letter and has not been guessed before, returns
    that letter.

    If the input is either not a letter, or not a single letter, or has been
    guessed before, asks the player for input again.
    """
    # user is prompted for a string. String is checked to see whether or not it is a valid entry.
    # if valid, one of two things happens:
    #1. if string is correct, append to string correct_guesses
    #2 if string is incorrect, append to wrong_guesses
    print "Guess a letter:",
    guess = raw_input()
    already_guessed = right_guesses + wrong_guesses
    while guess.isalpha() == False or len(guess) != 1 or (guess in already_guessed) == True:
        print "Try again. Your guess must be one letter that you have not previously guessed:",
        guess = raw_input()
    return guess
        



def display_word_with_guesses(correct_word, guesses):
    """
    Returns a string where every letter in the word contained in guesses is
    shown as that letter, and every letter in the word not contained in guesses
    is shown as an underscore.
    """
    global word
    global right_guesses
    guesses = right_guesses
    result = ""
    for letter in correct_word:
        if letter in guesses:
            result += letter
        else:
            result += "_"
    return result
# for each letter in the word, check to see if the letter is in the list of correct
# guesses, and if it is, append it to result. if it isn't, return "_" 

def example(word):
    """
    return the word, reversed
    """
    return word[::-1]

