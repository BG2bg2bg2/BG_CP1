#set Veriables
import turtle as t

#make the spaces
rows = 6
columns = 6
#make empty lists for later use
H = []
V = []
#see how many rows we need to add
for r in range(rows + 1):
    row = []
    #for how many rows we need to add one more column
    for c in range(columns):
        row.append(True)
    H.append(row)
#how many columns we need
for c in range(columns + 1):
    column = []
    #what rows in the columns need to be added
    for r in range(rows):
        column.append(True)
    V.append(column)
#if we have already been in that box before
visited = [[False for c in range(columns)] for r in range(rows)]


#makes the maze
def draw_maze(H,V):
    #how big is the screen
    screen = t.Screen()
    #how many picksl is the box
    box_size = 24
    #how many picksles is the line
    line_width = 5
    #sets up the size of the screen
    screen.setup(width = columns * (box_size + 2) * line_width, height = rows * (box_size + 2) * line_width)
    #starts at the top left
    screen.setworldcoordinates(-line_width,-line_width,columns * (box_size+line_width), rows * (box_size + line_width))
    
    screen.tracer(False)
    tu = t.Turtle()
    tu.hideturtle()
    t.speed(90)
    t.pensize(line_width)


    def draw_line(x1,y1,x2,y2):
        tu.penup()
        tu.goto(x1,y1)
        tu.pendown()
        tu.goto(x2,y2)
        tu.penup()

    for r in range(rows + 1):
        y = (rows - r) * box_size
        for c in range(columns):
            if  H[r][c]:
                x1 = c * box_size
                x2 = (c+1) * box_size
                draw_line(x1, y, x2,y)


    for r in range(rows):
        y1 = (rows - r - 1) * box_size
        y2 = (rows - r) * box_size
        for c in range(columns + 1):
            if V[c][r]:
                x = c * box_size
                draw_line(x, y1, x, y2)


    screen.tracer(True)

import random

def carve_path(r, c):
    visited[r][c] = True
    directions = ['U', 'D', 'L', 'R']
    random.shuffle(directions)

    for d in directions:
        nr, nc = r, c
        if d == 'U' and r > 0: nr -= 1
        if d == 'D' and r < rows - 1: nr += 1
        if d == 'L' and c > 0: nc -= 1
        if d == 'R' and c < columns - 1: nc += 1

        if not visited[nr][nc]:
            if d == 'U': H[r][c] = False
            if d == 'D': H[r+1][c] = False
            if d == 'L': V[c][r] = False
            if d == 'R': V[c+1][r] = False
            carve_path(nr, nc)


# Start carving at top-left
carve_path(0, 0)
H[0][0] = False
H[rows][columns -1] = False
draw_maze(H,V)
t.done()


