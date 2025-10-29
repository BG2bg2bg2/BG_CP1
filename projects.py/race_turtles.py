#BG 1st race the turtles

import turtle
import random
import time


screen = turtle.Screen()
screen.setup(600, 400)
screen.title("Racing Five Turtles")


colors = ["red", "yellow", "blue", "purple", "green", "orange", "brown"]
step = [1,2,3,4,5,6,7,8,9,10]
r = random.choice(len(step))
distence = 200
speed = 50
delay = speed / step
turtles = []

for i in range(5):
    t = turtle.Turtle()
    t.color(random.choice(colors))
    t.penup()
    t.goto(-250, 100 - i * 50)
    turtles.append(t)

for i in range(distence // step):
    t.forward(step)
    time.sleep(delay)
    
    

turtle.done()

