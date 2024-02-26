import turtle
import random
import time
delay=0.1
sc=0
hs=0

#creating a body of a snake 
bodies=[]
#creating a screen
s=turtle.Screen()
s.title("Snake new game")
s.bgcolor("white")
s.setup(width=600,height=600)    #size of a screen

#create snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.fillcolor("yellow")
head.penup() #for not moving the object
head.goto(0,0)  #for place at centre
head.direction="stop"


#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()     #for hiding a turtle
food.goto(150,200)    #where to show food
food.st()     #show turtle

#score board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("white")
sb.penup()
sb.ht()
sb.goto(-250,250)
sb.write("Score:0  |  Highest Score:0")   # to print a message on screen

def moveup():   #for moving in all the direction
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"

def movestop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    
#event handling  -key mappings

s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveright,"Right")
s.onkey(moveleft,"Left")
s.onkey(movestop,"space")


#mainloop
while True:
    s.update()  # to update screen
    #check collision with border
    if head.xcor()>290:
        head.setx(-290)

    if head.xcor()<-290:
        head.setx(290)

    if head.ycor()>290:
        head.sety(-290)

    if head.ycor()<-290:
        head.sety(290)

    #check collision with food
    if head.distance(food)<20:
        x=random.randint(-290,290)   #move food on random place
        y=random.randint(-290,290)
        food.goto(x,y)

        #increase the length of the snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)   #append new body

    #increase the score
        sc=sc+10
    #change delay
        delay=delay-0.001

    #update the highest score
        if sc>hs:
             hs=sc
        sb.clear()
        sb.write("score:{}  |  Highest Score:{}".format(sc,hs))

    #move the snake bodies
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if len(bodies)>0:
             x=head.xcor()
             y=head.ycor()
             bodies[0].goto(x,y)
    move()

#check collison with snake body--
    for body in bodies:
             if body.distance(head)<20:
                 time.sleep(1)
                 head.goto(0,0)
                 head.direction="stop"
                 #hide bodies
                 for body in bodies:
                    body.ht()
                 #outside for loop
                 bodies.clear()
                 sc=0
                 delay=0.1
    #update score board
                 sb.clear()
                 sb.write("Score:{}  | Highest Score:{}".format(sc,hs))
    
    time.sleep(delay)
s.mainloop()




















