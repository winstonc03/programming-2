# Quiz Game
# Author: Winston
# Date: December 4, 2020
import time
import sys

## type characters one by one, unnecessary but looks cool
def type_slow(slow_string):
    for l in slow_string:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)


type_slow("Welcome! What's your name?\n")
name = input()
score = 0

type_slow(f"Hey {name}! I have a short quiz for you, Good Luck!\n")
time.sleep(1.5)

type_slow("Finish the sentence:  Who lives in a ___ under  the seaaa\n")
q1 = input().lower().strip("!., -")
if q1 == "pineapple":
    score += 1
    print("Correct!")
else:
    print("The correct answer was 'pineapple' :( ")

type_slow("What's 15 times 12?\n")
q2 = input().lower().strip("!., -").replace(" ","")
if q2 == "180" or q2 == "onehundredeighty":
    score += 1
    print("Correct!")
else:
    print("The correct answer was '180' :( ")

type_slow("Who is the main character in the 'Mario' Franchise?\n")
q3 = input().lower().strip("!., -")
if q3 == "mario":
    score += 1
    print("Correct!")
else:
    print("Cmonnnnnn :( ")

type_slow("True or False: Penguins can fly.\n")
q4 = input().lower().strip("!., -")
if q4 == "true" or q4 == "t":
    score += 1
    print("Correct!")
else:
    print("Nah penguins do be flying 0.o ")

type_slow("Last Question, is this the best quiz ever?\n")
q5 = input().lower().strip("!., -").replace(" ","")
like_quiz = ["yes", "yeah", "sure","yessir", "ofcourse"]
if any(x in q5 for x in like_quiz):
    score += 1
    print("Awesome!")
else:
    print("Aw :( ")

percent = score/5 * 100

if score >= 3:
    type_slow(f"That's all! Your final percentage was {percent}%, You're awesome {name}!")
else:
    type_slow(f"That's all! Your final percentage was {percent}%, Nice try {name}!")
