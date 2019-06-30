#The program will create a number then you have to guess and it will tell you a hint or tell you that you are correct.

import random

num=random.randint(0,100)
answer = int(input("Enter your guess: "))

while answer != num:
    if answer < num:
        print ("The guess is SMALLER than the number")
    if answer > num:
        print ("The guess is BIGGER than the number")
    answer = int(input("Enter your new guess: "))

print ("Your Guess is CORRECT")