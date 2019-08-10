# take a list of numbers
# make a new list contains only the even numbers from the given list
# do it in one line

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [number for number in a if number % 2 == 0] # to make a new list contains only the even numbers from the old list

print (b)
