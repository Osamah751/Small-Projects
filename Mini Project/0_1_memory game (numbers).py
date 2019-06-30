"""
In this game you will
1- tell the program how many numbers do you want to remember
2- it will show you the number you have to remember
3- then it will delete it and ask you about the number
4- it will give you a feed back for your answer
5- if your answer is CORRECT and will ask you if you want to play again
6- if your answer is WRONG it will ask you again to answer again
"""
import sys
import random
import time
def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

difficulty=int(input("how many numbers do you want to remember: ")) # asking the user to set the difficulty
num= [] # an empty list to add numbers on
for i in range(difficulty):
    a = random.randint(0, 9) #the random number
    num.append(a) # adding the random number to the list

num = int(''.join(str(e) for e in num))
print (num)
time.sleep(5)
delete_last_lines(2)
answer=int(input("Enter the number that you remember: "))
if answer == num:
    print("CORRECT")
else:
    print("WRONG")

