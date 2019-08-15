import random

P1 =input("Player 1 ,please Choose Rock , Paper or Scissor: ")
COP =  random.randint(0,2) # 0=Rock , 1=Scissor , 2=Paper

if P1 == "Rock":
    PR= 0
if P1 == "Paper":
    PR = 2
if P1 == "Scissor":
    PR = 1
print ("P1= ", P1)

if COP == 0:
    COR = "Rock"
if COP == 2:
    COR = "Paper"
if COP == 1:
    COR = "Scissor"

R = PR - COP

print ("player 1 chose (", P1, ") and the computer chose (", COR, ")")
if R==-1 or R==2:
    print ("Player 1 Won")
elif R==0:
    print ("It is a draw")
else:
    print ("you lose , computer won and it will rule the world")


