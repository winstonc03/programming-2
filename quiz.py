# Quiz Game
# Author: Winston
# Date: December 4, 2020

name = input("Welcome! What's your name?\n")
score = 0

print(f"Hey {name}, I have a short quiz for you, Good Luck!")

q1 = input("Finish the sentence:  Who lives in a ___ under  the seaaa\n").lower().strip("!., -")
if q1 == "pineapple":
    score += 1
    print("Correct!")
else:
    print("The correct answer was 'pineapple' :( ")

q2 = input("What's 15 times 12?\n").lower().strip("!., -").replace(" ","")
if q2 == "180" or q2 == "onehundredeighty":
    score += 1
    print("Correct!")
else:
    print("The correct answer was '180' :( ")

q3 = input("Who is the main character in the 'Mario' Franchise?\n").lower().strip("!., -")
if q3 == "mario":
    score += 1
    print("Correct!")
else:
    print("Cmonnnnnn :( ")

q4 = input("True or False: Penguins can fly.\n").lower().strip("!., -")
if q4 == "true" or q4 == "t":
    score += 1
    print("Correct!")
else:
    print("Nah penguins do be flying 0.o ")

q5 = input("Last Question, did you like this quiz?\n").lower().strip("!., -")
if q5 == "yes" or q5 == "yessir":
    score += 1
    print("Awesome!")
else:
    print("Aw :( ")

percent = score/5 * 100

if (score >= 3):
    print(f"That's all! Your final percentage was {percent}%, You're awesome {name}!")
else:
    print(f"That's all! Your final percentage was {percent}%, Nice try {name}!")
