# ask the user for a sentence then return it in a reverse order of its words


string = "My name is Michele"

def reverse_a_string (string):
    string = string.split(" ")
    string = ' '.join(string[::-1])
    return (string)

print (reverse_a_string(string))