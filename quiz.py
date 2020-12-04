# Quiz Game
# Author: Winston
# Date: December 4, 2020

import time
name = input("Welcome! What's your name?\n")
score = 0

print(f"Hey {name}, I have a short quiz for you, Good Luck!")
time.sleep(2)

if input("Finish the sentence:  ___ ") == "n":
    score += 1
percent = score/5

#.lower.strip