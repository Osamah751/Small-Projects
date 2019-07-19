# ask the user for a string
# see if you can read it farward or backward without changing the word

string = input("what is the word you want to check ? ")

rv_string = string [::-1]

if string == rv_string:
    print ("The word", "'"+ string+ "'", "is a palindrome word")
else:
    print ("The word", "'"+ string+ "'", "is NOT a palindrome word")
