#BG 1st maze genorator

#bring in turtle to run the code
import turtle

#Make the stuff for the lists
wall = "|"
floor = "_"
space = " "

w = wall
f = floor
s = space

x = 1
y = 0
z = 3

def maze():
    grid_rows = [[1,1,0,0,1,0],
                 [0,1,1,1,0,1],
                 ]
    grid_colums = [[0,1,1,0,0,1],
                   [0,0,0,1,1,1]
                   ]
    start = [[]]
    for a in grid_rows:
        print(a)
maze()
