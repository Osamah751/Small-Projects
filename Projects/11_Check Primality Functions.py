# take a number from the user
# find if the number is prime or not

num = int(input("Give me the number that you want to learn the divisors of it: "))
Divisors = []

for i in range (1,num+1):
    if num % i == 0:
        Divisors.append(i)
if len(Divisors) <= 2:
    print ("The number is ' prime '")
else:
    print ("The number is ' NOT prime ' ")