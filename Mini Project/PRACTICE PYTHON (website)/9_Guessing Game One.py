# make a random number between 1 and 9
# make the user guess the number

import random

num = random.randint(1,9)
print (num)
Guess = None
counter = 0

while Guess != num:
    Guess = int(input("what is your guess? "))

    if Guess < num :
        print ("Your guess is 'smaller' than the answer")
    elif Guess > num:
        print ("Your guess is 'bigger' than the answer ")
    else:
        print ("Your guess is 'correct' ")
    counter += 1

print ("the nmber of guesses you did is", "'", counter, "'")