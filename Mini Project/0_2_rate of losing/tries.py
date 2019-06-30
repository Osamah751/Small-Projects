# this program will ask the user to enter the number of trials they want
# then it will flip a coin and count the number of times we got a head
# it will print the ( total number of trial so far ) + ( the number of heads counted ) + ( the persentage of winning )

import random
import matplotlib.pyplot as plt

Total = []
Persentage = []

Heads= 0
total =0

trails = int(input("how many trials do you want ? "))


for i in range (trails):
    a = random.randint(0,1) # Head:1 Tail:0
    Heads += a
    total += 1
    Total.append(total)
    persentage = (Heads / total) * 100
    Persentage.append(persentage)


# plotting the points
plt.plot(Total, Persentage)

# naming the x axis
plt.xlabel('x - Total')
# naming the y axis
plt.ylabel('y - Persentage')

# giving a title to my graph
plt.title('coin counter')
# function to grid the plot
plt.grid()
# function to show the plot
plt.show()


