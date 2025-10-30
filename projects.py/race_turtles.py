#BG 1st race the turtles

import turtle as t
import random
import time



#makes the screen
screen = t.Screen()
screen.setup(900, 900)
screen.title("Racing Five Turtles")

#colors for the turtles
acolors = ["red", "yellow", "blue", "purple", "green", "orange", "brown"]
#assines the colors
colors = random.sample(acolors, 5)


#how many steps the turtls take
step = [1,2,3,4,5,6,7,8,9,10]
turtles = []



#Makes the turtles

for i in range(5):
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-250, 100 - i * 50)
    turtles.append(t)

# Marks the finish line
a = t.Turtle()
a.hideturtle()
a.speed(0)
a.penup()
a.goto(500, 250)
a.pendown()
a.pensize(5)
a.color("black")
a.right(90)
a.forward(500)

finish_line = 500


race = True
while race:
    for t in turtles:
        t.forward(random.choice(step))
        if t.xcor() >= finish_line:
            race = False
            print(f"The {t.pencolor()} turtle won!")
            break
    time.sleep(.01)

t.done()

