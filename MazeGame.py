import turtle
from turtle import Screen, Turtle 
from random import randint
import math
player = turtle.Turtle()

drawer = turtle.Turtle()
drawer.color("green", "purple")
drawer.hideturtle()
drawer.speed(10)

player.color("green", "purple")
player.pensize(4)
player.penup()
player.hideturtle()
drawer.write("Loading...", font=("arial", 30, "bold"), align=("center"))
player.speed(10)
player.shapesize(4, 4)
lines_list1 = []
lines_list2 = []
lines_list3 = []
lines_list4 = []
lines_list5 = []
lines_list6 = []
lines_list7 = []
lines_list8 = []
lines_list9 = []
for i in range(90):
    x = randint(-400, 600)
    y = randint(-300, 300)
    z = randint(0, 360)
    if -400<x<-67 and -300<y<-100:
        lines_list1.append([x, y, z])
    elif -400<x<-67 and -100<y<100:
        lines_list2.append([x, y, z])
    elif -400<x<-67 and 100<y<300:
        lines_list3.append([x, y, z])
    elif -67<x<266 and -300<y<-100:
        lines_list4.append([x, y, z])
    elif -67<x<266 and -100<y<100:
        lines_list5.append([x, y, z])
    elif -67<x<266 and 100<y<300:
        lines_list6.append([x, y, z])
    elif 266<x<600 and -300<y<-100:
        lines_list7.append([x, y, z])
    elif 266<x<600 and -100<y<100:
        lines_list8.append([x, y, z])
    elif 266<x<600 and 100<y<300:
        lines_list9.append([x, y, z])


    player.goto(x, y)
    player.pendown()
    player.left(z)
    player.forward(100)
    player.seth(0)
    player.penup()
drawer.clear()
player.showturtle()
player.setposition(-500, -200)
drawer.penup()
drawer.goto(-200, -200)
drawer.pendown()
drawer.begin_fill()
drawer.forward(400)
drawer.left(90)
drawer.forward(400)
drawer.left(90)
drawer.forward(400)
drawer.left(90)
drawer.forward(400)
drawer.left(90)
drawer.end_fill()
drawer.penup()
drawer.goto(0, 120)
drawer.write("MazeGame", font=("arial", 50, "bold"), align="center")
drawer.goto(80, 0)
drawer.speed(10)
drawer.pensize(5)
drawer.pendown()
drawer.right(30)
drawer.backward(200)
drawer.left(330)
drawer.forward(100)
drawer.right(253)
drawer.backward(100)
drawer.left(330)
drawer.forward(200)

def screenclick(x,y):
    turtle2.dot(600, "green")
    turtle2.penup()
    turtle2.goto(0, 180)
    turtle2.write("1. This is like a normal maze, but with a twist:", font=("arial", 10, "bold"), align=("center"))
    turtle2.goto(0, 150)
    turtle2.write("if the you touch one of the green lines, you have to restart from the beginning.", font=("arial", 10, "bold"), align=("center"))
    turtle2.goto(0, 120)
    turtle2.write("2. The objective of the game is to get the arrow-shaped player", font=("arial", 10, "bold"), align=("center"))
    turtle2.goto(0,90)
    turtle2.write("from the left side of the screen to the right side of the screen, without touching the lines.", font=("arial", 10, "bold"), align=("center"))
    turtle2.goto(0, 60)
    turtle2.write("3. Use the Right Arrow key to move the player forward,", font=("arial", 10, "bold"), align=("center"))
    turtle2.goto(0, 30)
    turtle2.write("use the Left Arrow key to move the player backward,", font=("arial", 10, "bold"), align=("center"))
    turtle2.goto(0, 0)
    turtle2.write("use the Up Arrow Key to turn the player left,", font=("arial", 10, "bold"), align=("center"))
    turtle2.goto(0, -30)
    turtle2.write("and use the Down Arrow key to turn the player right.", font=("arial", 10, "bold"), align=("center"))
    
button = Turtle()
button.penup()
button.hideturtle()
button.goto(-130, -160)
button.shape("square")
button.shapesize(3, 5, 2)
button.fillcolor("purple")
button.onclick(screenclick)
button.showturtle()

turtle2 = Turtle()
turtle2.hideturtle()
drawer.penup()
drawer.goto(-150, -170)
drawer.write("Rules", font=("arial", 10, "bold"))



def screenclick(x,y):
    drawer.clear()
    button.hideturtle()
    button2.hideturtle()

button2 = Turtle()
button2.penup()
button2.hideturtle()
button2.goto(110, -160)
button2.shape("square")
button2.shapesize(3, 5, 2)
button2.fillcolor("purple")
button2.onclick(screenclick)
button2.showturtle()


drawer.penup()
drawer.goto(100, -170)
drawer.write("Play", font=("Arial", 10, "bold"))




def goforward():
    forwardplayer = 1
    player.forward(1)
    x = player.xcor()
    y = player.ycor()
    while forwardplayer <= 15:
        if -400<x<-67 and -300<y<-100:
            i=0
            for i in range(len(lines_list1)):
                
                line_x = (lines_list1[i])[0]
                line_y = (lines_list1[i])[1]
                angle_z = math.tan((lines_list1[i])[2])
                y_inter = line_y - line_x*angle_z
                hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
                turtleangle = round(math.acos((line_x-x)/hypot)*180/math.pi)
                if hypot < 100 and  angle_z-1<turtleangle<angle_z+1:
                    player.goto(-500, -200)
                i += 1
        elif -400<x<-67 and -100<y<100:
            i=0
            for i in range(len(lines_list2)):
                
                line_x = (lines_list2[i])[0]
                line_y = (lines_list2[i])[1]
                angle_z = (lines_list2[i])[2]
                hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
                turtleangle = round(math.acos((line_x-x)/hypot)*180/math.pi)
                if hypot < 100 and angle_z-1<turtleangle<angle_z+1:
                    player.goto(-500, -200)
                i += 1
        elif -400<x<-67 and 100<y<300:
            i=0
            for i in range(len(lines_list3)):
                
                line_x = (lines_list3[i])[0]
                line_y = (lines_list3[i])[1]
                angle_z = (lines_list3[i])[2]
                hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
                turtleangle = round(math.acos((line_x-x)/hypot)*180/math.pi)
                if hypot < 100 and angle_z-1<turtleangle<angle_z+1:
                    player.goto(-500, -200)
                i += 1
        elif -67<x<266 and -300<y<-100:
            i=0
            for i in range(len(lines_list4)):
                
                line_x = (lines_list4[i])[0]
                line_y = (lines_list4[i])[1]
                angle_z = (lines_list4[i])[2]
                hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
                turtleangle = round(math.acos((line_x-x)/hypot)*180/math.pi)
                if hypot < 100 and angle_z-1<turtleangle<angle_z+1:
                    player.goto(-500, -200)
                i += 1
        elif -67<x<266 and -100<y<100:
            i=0
            for i in range(len(lines_list5)):
                
                line_x = (lines_list5[i])[0]
                line_y = (lines_list5[i])[1]
                angle_z = (lines_list5[i])[2]
                hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
                turtleangle = round(math.acos((line_x-x)/hypot)*180/math.pi)
                if hypot < 100 and angle_z-1<turtleangle<angle_z+1:
                    player.goto(-500, -200)
                i += 1
        elif -67<x<266 and 100<y<300:
            i=0
            for i in range(len(lines_list6)):
                
                line_x = (lines_list6[i])[0]
                line_y = (lines_list6[i])[1]
                angle_z = (lines_list6[i])[2]
                hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
                turtleangle = round(math.acos((line_x-x)/hypot)*180/math.pi)
                if hypot < 100 and angle_z-1<turtleangle<angle_z+1:
                    player.goto(-500, -200)
                i += 1
        elif 266<x<600 and -300<y<-100:
            i=0
            for i in range(len(lines_list7)):
                
                line_x = (lines_list7[i])[0]
                line_y = (lines_list7[i])[1]
                angle_z = (lines_list7[i])[2]
                hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
                turtleangle = round(math.acos((line_x-x)/hypot)*180/math.pi)
                if hypot < 100 and angle_z-1<turtleangle<angle_z+1:
                    player.goto(-500, -200)
                i += 1
        elif 266<x<600 and -100<y<100:
            i=0
            for i in range(len(lines_list8)):
                
                line_x = (lines_list8[i])[0]
                line_y = (lines_list8[i])[1]
                angle_z = (lines_list8[i])[2]
                hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
                turtleangle = round(math.acos((line_x-x)/hypot)*180/math.pi)
                if hypot < 100 and angle_z-1<turtleangle<angle_z+1:
                    player.goto(-500, -200)
                i += 1
        elif 266<x<600 and 100<y<300:
            i=0
            for i in range(len(lines_list9)):
                
                line_x = (lines_list9[i])[0]
                line_y = (lines_list9[i])[1]
                angle_z = (lines_list9[i])[2]
                hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
                turtleangle = round(math.acos((line_x-x)/hypot)*180/math.pi)
                if hypot < 100 and angle_z-1<turtleangle<angle_z+1:
                    player.goto(-500, -200)
                i += 1
        player.forward(1)
        forwardplayer += 1

def gobackward():
    player.backward(15)
    x = player.xcor()
    y = player.ycor()
    if -400<x<-67 and -300<y<-100:
        i=0
        for i in range(len(lines_list1)):
            
            line_x = (lines_list1[i])[0]
            line_y = (lines_list1[i])[1]
            angle_z = (lines_list1[i])[2]
            hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
            if hypot < 100 and math.acos((line_x-x)/hypot)*180/math.pi == angle_z:
                player.goto(-500, -200)
            i += 1
    elif -400<x<-67 and -100<y<100:
        i=0
        for i in range(len(lines_list2)):
            
            line_x = (lines_list2[i])[0]
            line_y = (lines_list2[i])[1]
            angle_z = (lines_list2[i])[2]
            hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
            if hypot < 100 and math.acos((line_x-x)/hypot)*180/math.pi == angle_z:
                player.goto(-500, -200)
            i += 1
    elif -400<x<-67 and 100<y<300:
        i=0
        for i in range(len(lines_list3)):
            
            line_x = (lines_list3[i])[0]
            line_y = (lines_list3[i])[1]
            angle_z = (lines_list3[i])[2]
            hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
            if hypot < 100 and math.acos((line_x-x)/hypot)*180/math.pi == angle_z:
                player.goto(-500, -200)
            i += 1
    elif -67<x<266 and -300<y<-100:
        i=0
        for i in range(len(lines_list4)):
            
            line_x = (lines_list4[i])[0]
            line_y = (lines_list4[i])[1]
            angle_z = (lines_list4[i])[2]
            hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
            if hypot < 100 and math.acos((line_x-x)/hypot)*180/math.pi == angle_z:
                player.goto(-500, -200)
            i += 1
    elif -67<x<266 and -100<y<100:
        i=0
        for i in range(len(lines_list5)):
            
            line_x = (lines_list5[i])[0]
            line_y = (lines_list5[i])[1]
            angle_z = (lines_list5[i])[2]
            hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
            if hypot < 100 and math.acos((line_x-x)/hypot)*180/math.pi == angle_z:
                player.goto(-500, -200)
            i += 1
    elif -67<x<266 and 100<y<300:
        i=0
        for i in range(len(lines_list6)):
            
            line_x = (lines_list6[i])[0]
            line_y = (lines_list6[i])[1]
            angle_z = (lines_list6[i])[2]
            hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
            if hypot < 100 and math.acos((line_x-x)/hypot)*180/math.pi == angle_z:
                player.goto(-500, -200)
            i += 1
    elif 266<x<600 and -300<y<-100:
        i=0
        for i in range(len(lines_list7)):
            
            line_x = (lines_list7[i])[0]
            line_y = (lines_list7[i])[1]
            angle_z = (lines_list7[i])[2]
            hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
            if hypot < 100 and math.acos((line_x-x)/hypot)*180/math.pi == angle_z:
                player.goto(-500, -200)
            i += 1
    elif 266<x<600 and -100<y<100:
        i=0
        for i in range(len(lines_list8)):
            
            line_x = (lines_list8[i])[0]
            line_y = (lines_list8[i])[1]
            angle_z = (lines_list8[i])[2]
            hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
            if hypot < 100 and math.acos((line_x-x)/hypot)*180/math.pi == angle_z:
                player.goto(-500, -200)
            i += 1
    elif 266<x<600 and 100<y<300:
        i=0
        for i in range(len(lines_list9)):
        
            line_x = (lines_list9[i])[0]
            line_y = (lines_list9[i])[1]
            angle_z = (lines_list9[i])[2]
            hypot = (math.sqrt((x-line_x)**2 + (y-line_y)**2))
            if hypot < 100 and math.acos((line_x-x)/hypot)*180/math.pi == angle_z:
                player.goto(-500, -200)
            i += 1
        

def turnleft():
    player.left(1)

def turnright():
    player.right(1)

turtle.onkey(goforward, "Right")
turtle.onkey(gobackward, "Left")
turtle.onkey(turnleft, "Up")
turtle.onkey(turnright, "Down")
turtle.listen()
turtle.mainloop()
turtle.done()