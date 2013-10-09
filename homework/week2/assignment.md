## Reading

Read chapter 2 from [*Think Python: How To Think Like a Computer Scientist*](http://www.greenteapress.com/thinkpython/html/thinkpython003.html)

## Playing with list slices

First, read [the Python list documentation](http://docs.python.org/tutorial/introduction.html#lists).

Assume that x has been assigned the following list:

    x = [3, 5, 7, 2, 4, 8, 100, 2]

For each of the following, try these in a Python interpreter and then
describe in English what they mean:

    (example) x[-1]
        x[-1] is 2. The index of -1 refers to the last element in the list.

    (a) x[2:4]
      x[2:4] is [7, 2]. It slices the 3rd - 4th elements in the list
    (b) x[1:]
      x[1:] is [5, 7, 2, 4, 8, 100, 2]. It returns a list containing all elements in list x after the first element.
    (c) x[:4]
      x[:4] is [3, 5, 7, 2]. It returns a new list containing all elements in list x up to the fifth element.
    (d) x[1:][2]
      x[1:][2] is 2. It creates two new lists, and returns the second. The first list contains all elements from list x after the first element. The second is contains the third element from the first list. 
    (e) x[2:-2]
      x[2:-2] is [7, 2, 4, 8]. It returns a list containing all elements from list x after the first element, and before the second-to-last element.
    (f) x[5:3]
      x[5:3] is [], an empty list. When the first slice index is larger than the second, the Python interpreter will return an empty list.
    (g) x[100]
      x[100] returns an error message. List x is 8 strings long, so there is no element at index [100] to return. 
    (h) x[-100:100]
      x[-100:100] is [3, 5, 7, 2, 4, 8, 100, 2], which contains all of list x. A negative out-of-range first slice index will be replaced by 0, a positive out-of-range second slice index will be replaced by the largest index in the list.
    (i) "surprise"[1:4]
      "surprise"[1:4] is 'urp'. In this case, the second through fourth characters are sliced from the string "surprise".

What's the difference between `x[2:3]` and `x[2]`?
  x[2:3] returns a list containing only the third value in list x. x[2] returns the third value in list x, but only as an individual value.

## List sorting

In the provided file listsorter.py, write a program that prompts a
user for 5 numbers. Store those numbers in a list. Print out a list
containing those numbers from smallest to largest.  When you run the
program, you should get output like the following:

    Enter a number: 3
    Enter a number: 2
    Enter a number: 1
    Enter a number: 10000
    Enter a number: -5

    [-5, 1, 2, 3, 10000]

You may want to refer to [this section of the Python
docs](http://docs.python.org/tutorial/datastructures.html#more-on-lists) for
handy functions that you can call on lists.

You can assume that the user of this program will always enter a
number. Don't worry about handling non-number input.

## Practice with dicts

You're going to write a mini-database of favorite foods. Think of 5 people you
know and a food they like, e.g. "Naomi" and "brussels sprouts". In the file
fooddatabase.py, write a program that prompts the user for a name and prints out
that person's favorite food, e.g.

    What person do you want to know about? Naomi
    Naomi's favorite food is: brussels sprouts

Use a dictionary to store the association between people and
food. See:
[the dictionary docs](http://docs.python.org/tutorial/datastructures.html#dictionaries)
if you need a refresher on dictionaries.

For now, don't worry about what happens when your dictionary doesn't
have somebody's name in it. It's fine to have your program throw an
exception. Although, if you're interested in how you would handle
this, check out
[try statements](http://docs.python.org/reference/compound_stmts.html#try)

## Practice with finding information

Use the internet to figure out how to get python to give you a random
integer between 0 and 100.  Write down what function you would use:

In guessmynumber.py, write a program which picks a single random
integer between 0 and 100 and repeatedly asks the user to guess it.

 - When the user is correct, print "You win!" and end the program
 - When the user is incorrect, tell them whether their guess was
   too high or too low, and then let them guess again until they get it.

Hint:

    import foo

is a python statement that makes module foo available from your
program.  For example, if there is a function in foo called flip(),
then you would be able to write foo.flip() in your program.

## Manufactoria

Exercises #3, #4a, #4b

If you didn't finish [Manufactoria](http://pleasingfungus.com/Manufactoria/) puzzle #3, please finish it now.  Do both of the puzzles that branch from #3.
