# Quiz Game
# Author: Winston
# Date: December 4, 2020

import time
name = input("Welcome! What's your name?\n")
score = 0

print(f"Hey {name}, I have a short quiz for you, Good Luck!")
time.sleep(2)

if input("Finish the sentence:  Who lives in a ___ under  the seaaa\n").lower() == "pineapple":
    score += 1
    print("Correct!")
else:
    print("The correct answer was 'pineapple' :( ")

if input("What's 15 times 12?\n") == "180":
    score += 1
    print("Correct!")
else:
    print("The correct answer was '180' :( ")

if input("Who is the main character in the 'Mario' Franchise?\n").lower() == "mario":
    score += 1
    print("Correct!")
else:
    print("The correct answer was 'mario' :( ")

if input("True or False: Penguins can fly.\n").lower() == "true":
    score += 1
    print("Correct!")
else:
    print("The correct answer was 'True' :( ")

if input("Last Question, did you like this quiz?\n").lower() == "yes":
    score += 1
    print("Correct!")
else:
    print("The correct answer was 'yes' >:( ")

percent = score/5 * 100

print(f"That's all! You're final percentage was {percent}%, You're awesome {name}!")

#.lower.strip