# take a number from the user
# find and print the Divisors for that number

num = int(input("Give me the number that you want to learn the divisors of it: "))
Divisors = []

for i in range (1,num+1):
    if num % i == 0:
        Divisors.append(i)

print (Divisors)
