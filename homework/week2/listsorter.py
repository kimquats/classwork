#listsorter.py

#In the provided file listsorter.py, write a program that prompts a
#user for 5 numbers. Store those numbers in a list. Print out a list
#containing those numbers from smallest to largest.

x = []

print "Enter a number",
x.append(raw_input())

print "Enter a number",
x.append(raw_input())

print "Enter a number",
x.append(raw_input())

print "Enter a number",
x.append(raw_input())

print "Enter a number",
x.append(raw_input())

x.sort()

print x