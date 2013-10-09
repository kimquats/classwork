#guessmynumber.py

#In guessmynumber.py, write a program which picks a single random
#integer between 0 and 100 and repeatedly asks the user to guess it.

# - When the user is correct, print "You win!" and end the program
# - When the user is incorrect, tell them whether their guess was
#   too high or too low, and then let them guess again until they get it.

import random
z = [random.randint(0,100), 0]

print "Guess my number between 0 and 100 and get a prize!",
z.append(input())

while z[0] != z[1]:
  if z[0] > z[1]:
	print "Too low. Guess again!"
  elif z[0] < z[1]:
	print "Too high. Guess again!"
  z[1] = input()
print "You win!"