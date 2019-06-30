# make a list of the common element from two lists
# print the common_elements_list={cel}

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a = range(1,random.randint(1,30) ) # will make a list contain a random number of numbers in a row between the range we wanted
# b = random.sample(range(1, 100), 10) # will make a list using the range we wanted contain random numbers and only 10 numbers
#
# print ("a = ", a)
# print ("b = ", b)

cel =[ ] # a list of the common elements from the 2 lists

for i in a:
    if (i in b) and not (i in cel):
        cel.append(i)

print (cel)