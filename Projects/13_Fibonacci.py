# ask the user for a number then make Fibonacci list out of it

num = int( input("how many numbers do you want? ") )


def fibonacci (num):
    list = []
    num = num + 1
    for i in range (1,num):
        if i <= 2:
            list.append(1)
        else:
            new_num = int(list[i-3]) + int(list[i-2])
            list.append(new_num)
    return (list)

print ( fibonacci(num) )