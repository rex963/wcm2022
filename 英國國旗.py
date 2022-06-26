import turtle

# Create screen and turtle objects
screen = turtle.Screen()
screen.setup(100, 100)
myTurtle = turtle.Turtle()
myTurtle.color('black')
myTurtle.begin_fill()
# 藍底
for i in range(2):
    myTurtle.forward(600)
    myTurtle.left(90)
    myTurtle.forward(300)
    myTurtle.left(90)

myTurtle.fillcolor('blue')
myTurtle.end_fill()

#斜條白
myTurtle.begin_fill()
myTurtle.pencolor('white')
myTurtle.goto(0,30)
myTurtle.goto(570,300)
myTurtle.goto(600,300)
myTurtle.goto(600,270)
myTurtle.goto(30,0)
myTurtle.goto(0,0)
myTurtle.fillcolor('white')
myTurtle.end_fill()

#斜條紅
myTurtle.begin_fill()
myTurtle.pencolor('red')
myTurtle.goto(0,0)
myTurtle.goto(210,100)
myTurtle.goto(230,100)
myTurtle.goto(20,0)
myTurtle.fillcolor('red')
myTurtle.end_fill()

#斜條白
myTurtle.begin_fill()
myTurtle.pencolor('white')
myTurtle.penup()
myTurtle.goto(0,300)
myTurtle.pendown()
myTurtle.goto(0,270)
myTurtle.goto(570,0)
myTurtle.goto(600,0)
myTurtle.goto(600,30)
myTurtle.goto(30,300)
myTurtle.goto(0,300)
myTurtle.fillcolor('white')
myTurtle.end_fill()

#斜條紅
myTurtle.begin_fill()
myTurtle.pencolor('red')
myTurtle.penup()
myTurtle.goto(600,300)
myTurtle.pendown()
myTurtle.goto(390,200)
myTurtle.goto(370,200)
myTurtle.goto(580,300)
myTurtle.fillcolor('red')
myTurtle.end_fill()

#斜條紅
myTurtle.begin_fill()
myTurtle.pencolor('red')
myTurtle.penup()
myTurtle.goto(0,300)
myTurtle.pendown()
myTurtle.goto(0,280)
myTurtle.goto(190,200)
myTurtle.goto(210,200)
myTurtle.goto(0,300)
myTurtle.fillcolor('red')
myTurtle.end_fill()

#斜條紅
myTurtle.begin_fill()
myTurtle.pencolor('red')
myTurtle.penup()
myTurtle.goto(600,0)
myTurtle.pendown()
myTurtle.goto(390,100)
myTurtle.goto(410,100)
myTurtle.goto(600,20)
myTurtle.goto(600,0)
myTurtle.fillcolor('red')
myTurtle.end_fill()


#橫條白
myTurtle.begin_fill()
myTurtle.pencolor('white')
myTurtle.penup()
myTurtle.goto(0,100)
myTurtle.pendown()
for i in range(2):
    myTurtle.forward(600)
    myTurtle.left(90)
    myTurtle.forward(100)
    myTurtle.left(90)

myTurtle.fillcolor('white')
myTurtle.end_fill()

#直條白
myTurtle.begin_fill()
myTurtle.pencolor('white')
myTurtle.penup()
myTurtle.goto(250,0)
myTurtle.pendown()
for i in range(2):
    myTurtle.forward(100)
    myTurtle.left(90)
    myTurtle.forward(300)
    myTurtle.left(90)

myTurtle.fillcolor('white')
myTurtle.end_fill()

#橫條紅
myTurtle.begin_fill()
myTurtle.pencolor('red')
myTurtle.penup()
myTurtle.goto(270,0)
myTurtle.pendown()
for i in range(2):
    myTurtle.forward(60)
    myTurtle.left(90)
    myTurtle.forward(300)
    myTurtle.left(90)

myTurtle.fillcolor('red')
myTurtle.end_fill()

#直條紅
myTurtle.begin_fill()
myTurtle.pencolor('red')
myTurtle.penup()
myTurtle.goto(0,120)
myTurtle.pendown()
for i in range(2):
    myTurtle.forward(600)
    myTurtle.left(90)
    myTurtle.forward(60)
    myTurtle.left(90)

myTurtle.fillcolor('red')
myTurtle.end_fill()





