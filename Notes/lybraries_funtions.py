#BG 1st ;ibrairied and built in funtionons

#What is a library?
# random but importing something is a type of library like import random




#What libraries have we used?
import random
import time


#What are some common python libraries?



#How do you call a built-in function?



#What are some common functions that we have used
import turtle as t
import random
colors = ["orange", "green", "blue", "purple", "red"]
side = random.randint(10, 500)
t.color(random.choice(colors))

t.fillcolor(random.choice(colors))
t.begin_fill()
for x in range (1,5):
    t.forward(side)
    t.right(90)
t.end_fill()

t.penup()
t.goto(50,50)



t.fillcolor(random.choice(colors))
t.begin_fill()
for x in range(1,4):

    t.forward(side)
    t.right(90)

t.end_fill()

t.done()