s = input("Enter the string you want to check ")
temp = ""
string = ""

#if the given string is empty
if len(s) == 0:
    temp = s
else:
    #the checker
    for char in s:
        if temp == "":
            temp += char
        elif (temp[-1] < char) or (temp[-1] == char):
            temp += char
        elif temp[-1] > char:
            temp = char
        #remaking the string
        if len(temp) > len(string):
            string = temp
print ("Longest substring in alphabetical order is: " + string)
