from modmarkov import *

def chat_with_markov():
    print 'Hello!'
    user_input = raw_input()
    word_table = table_of_next_words(user_input)
    while user_input != 'bye!':
        response =  make_text(word_table)
        print response
        user_input = raw_input()
        update_table(word_table, user_input)  