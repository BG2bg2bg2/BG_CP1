#BG 1st race the turtles

import turtle as t
import random
import time

turtles = []
finish_line = 500

def setup():
    #make the screen
    screen = t.Screen()
    screen.setup(1400, 700)
    screen.title("Racing Five Turtles")
    #colors for the turtles
    colors = ["red", "yellow", "blue", "purple", "green"]

    #draw the finish line
    a = t.Turtle()
    a.hideturtle()
    a.speed(0)
    a.penup()
    a.goto((finish_line -1), 250)
    a.pendown()
    a.pensize(5)
    a.color("black")
    a.right(90)
    a.forward(500)

    #Create and draw the turtles on the starting line
    for i in range(5):
        a = t.Turtle()
        a.shape("turtle")
        a.color(colors[i])
        a.penup()
        a.goto(-250, 100 - i * 50)
        a.showturtle()
        turtles.append(a)

#check for winner
def winner(c_turtle):
    if c_turtle.xcor() >= finish_line:
        print(f"The {c_turtle.pencolor()} turtle won!")
        return True
    else:
        return False

#run the race
def run():
    #start race
    racer = True
    while racer:
        for a_turtle in turtles:
            #randomly choose how big the step each turtle takes
            a_turtle.forward(random.randint(3,15))
            #help check for winner
            if winner(a_turtle) == True:
                racer = False
                break
        time.sleep(.01)

#main program
setup()
run()
t.done()
