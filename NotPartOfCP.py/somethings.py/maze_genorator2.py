#BG 1st maze genorator

import turtle

grid_rows = [[1,1,0,0,1,0],
             [9,1,1,1,0,1],
             ]
grid_colums = [[0,1,1,0,0,1],
               [0,0,0,1,1,1]
               ]
def is_solvable(row_grid, col_grid):
    size = len(row_grid) -1 #wide maze
    visited = set() #cordanants you can rach
    stack = [(0,0)]

    while stack: #something is in the stack
        x,y = stack.pop()

        if x == size -1 and y == size -1:
            return True
        
        if (x, y) in visited:
            continue

        visited.add((x, y)) #go to line 23 and restarts

        if x < size - 1 and col_grid[y][x+1] == 0: #or "|"
            stack.append((x+1, y))
        if y < size -1 and row_grid[y+1][x] == 0: #or "|"
            stack.append((x, y+1))
        if x > 0 and col_grid[y][x] ==0:
            stack.append((x-1, y))
        if y > 0 and row_grid[y][x] == 0:
            stack.append((x,y-1))
    return False
