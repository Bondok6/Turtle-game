#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import math
import random

#set up Screen
wn = turtle.Screen()
wn.title("Turtle game by BonDok")
wn.tracer(2)
wn.bgcolor("black")


#create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

#create Goals
maxGoals = 8
goals =[]

for count in range (maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300) , random.randint(-300,300))

#create score variable
score = 0

#set up speed
speed = 0.9

#define functions
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increasespeed():
    global speed 
    speed += 0.9
def decreasespeed():
    global speed 
    speed -= 0.9   
def isCollision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2)) 
    if d < 20:
        return True
    else:
        return False

#set keyboard binding
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
turtle.onkey(decreasespeed,"Down")

#draw boundary
mypen = turtle.Turtle()
mypen.penup() #hide the line
mypen.setposition(-300,-300)
mypen.pendown() #appear (don not hide) the line
mypen.pensize(3) 
mypen.color("white")



for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()  #Finally, Hide my pen 



while True:
    player.forward(speed)

    #border checking
    if player.xcor() > 300 or player.xcor() < -300 :
        player.right(180)

    if player.ycor() > 300 or player.ycor() < -300 :
        player.right(180)        




    #move goal
    for count in range (maxGoals):
        goals[count].forward(2)                           

        #border checking
        if goals[count].xcor() > 290 or goals[count].xcor() < -290 :
            goals[count].right(180)

        if goals[count].ycor() > 290 or goals[count].ycor() < -290 :
            goals[count].right(180)  

        #collision checking
        if isCollision(player , goals[count]):
            goals[count].setposition(random.randint(-300,300) , random.randint(-300,300))
            goals[count].right(random.randint(0,360))
            #increase score
            score += 1
            #draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.color("white")
            mypen.setposition(-290 , 310)
            scorestring = "Score: %s" %score
            mypen.write(scorestring,False,align="left",font=("Arial",14,"normal"))




delay = raw_inout("press enter to finish.")


# In[ ]:





# In[ ]:




