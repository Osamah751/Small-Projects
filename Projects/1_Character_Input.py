
name= input("Enter your name please: ")
age= int(input("Enter your age please: "))
n= int(input("how many times do you want to see the message: "))
years= 100-age

# print (n*("Hi" + name + " you will turn 100 after "+years+" years.\n"))
# print (n*("Hi %s you will turn 100 after %d years.\n" (name, years)))
print (n*("Hi {} you will turn 100 after {} years.\n" .format(name, years) ))

