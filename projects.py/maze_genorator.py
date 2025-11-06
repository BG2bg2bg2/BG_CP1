# BG 1st maze_generator


#start the program
# involve the turtle and random libraries
import turtle as t
import random as ran

# assign the number of rows and columns
rows = 9
columns = 9

# make empty lists H and V for maze walls
H = []
V = []

# for each row: add a list of True values (walls exist)
for r in range(rows + 1):
    row = []
    for c in range(columns):
        row.append(True)
    H.append(row)

# for each column: add a list of True values (walls exist)
for c in range(columns + 1):
    column = []
    for r in range(rows):
        column.append(True)
    V.append(column)

# make a 2D list "visited" initialized to False
visited = [[False for c in range(columns)] for r in range(rows)]



def draw_maze(H, V):
    # setup screen size and turtle properties
    screen = t.Screen()
    box_size = 24
    line_width = 5
    screen.setup(width = columns * (box_size + 2) * line_width,
                 height = rows * (box_size + 2) * line_width)
    screen.setworldcoordinates(-line_width, -line_width,
                               columns * (box_size + line_width),
                               rows * (box_size + line_width))

    screen.tracer(False)
    tu = t.Turtle()
    tu.hideturtle()
    t.speed(90)
    t.pensize(line_width)

    # define helper function draw_line(x1, y1, x2, y2)
    def draw_line(x1, y1, x2, y2):
        tu.penup()
        tu.goto(x1, y1)
        tu.pendown()
        tu.goto(x2, y2)
        tu.penup()
    # write all horizontal walls
    for r in range(rows + 1):
        y = (rows - r) * box_size
        for c in range(columns):
            if H[r][c]:
                x1 = c * box_size
                x2 = (c + 1) * box_size
                draw_line(x1, y, x2, y)
            
    # write all vertical walls
    for r in range(rows):
        y1 = (rows - r - 1) * box_size
        y2 = (rows - r) * box_size
        for c in range(columns + 1):
            if V[c][r]:
                x = c * box_size
                draw_line(x, y1, x, y2)

    # update the screen
    screen.tracer(True)

#make a path for each direction:
def path(r, c):
    #mark the visited boxes
    visited[r][c] = True
    directions = ['U', 'D', 'L', 'R']
    # Shuffle movement directions
    ran.shuffle(directions)
    #if next box is inside maze AND unvisited:
    for d in directions:
        #remove wall between boxes
        nr, nc = r, c
        if d == 'U' and r > 0: nr -= 1
        if d == 'D' and r < rows - 1: nr += 1
        if d == 'L' and c > 0: nc -= 1
        if d == 'R' and c < columns - 1: nc += 1

        #reapeat calling the path on the next box
        if not visited[nr][nc]:
            if d == 'U': H[r][c] = False
            if d == 'D': H[r+1][c] = False
            if d == 'L': V[c][r] = False
            if d == 'R': V[c+1][r] = False
            path(nr, nc)


# Start maze generation at top-left
path(0, 0)

# Remove entrance and exit walls
H[0][0] = False
H[rows][columns - 1] = False


# Draw maze using turtle
draw_maze(H, V)

#end the program
t.done()
