import turtle
import random

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Maze Tic Tac Toe CPU")

# Easy / Medium / Hard AI difficulty
difficulty = screen.textinput("Difficulty", "Choose: easy / medium / hard").lower()

board_drawer = turtle.Turtle()
board_drawer.hideturtle()
board_drawer.speed(0)
board_drawer.pensize(5)

walls = [
    (-200,200,-200,-200), (200,200,200,-200),
    (-200,200,200,200), (-200,-200,200,-200),
    (-200,0,200,0), (0,200,0,-200)
]

def draw_maze():
    for x1,y1,x2,y2 in walls:
        board_drawer.penup()
        board_drawer.goto(x1,y1)
        board_drawer.pendown()
        board_drawer.goto(x2,y2)

draw_maze()

board = [" "]*9
current_player = "X"
marker = turtle.Turtle()
marker.hideturtle()
marker.speed(0)

win_lines = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def get_index(x,y):
    col = int((x + 200) // 200)
    row = int((200 - y) // 200)
    index = row*3 + col
    if 0 <= index < 9:
        return index
    return None

def draw_symbol(p,i):
    x = (-200 + (i%3)*200) + 100
    y = (200 - (i//3)*200) - 100
    marker.penup()
    marker.goto(x,y-50)
    marker.write(p, align="center", font=("Arial",48,"bold"))

def check_winner():
    return any(board[a]==board[b]==board[c]!=" " for a,b,c in win_lines)

def cpu_move():
    empty = [i for i in range(9) if board[i]==" "]

    # HARD: try to win or block
    if difficulty in ("medium","hard"):
        for p in ("O","X"):
            for i in empty:
                board[i]=p
                if check_winner():
                    board[i]="O"
                    return
                board[i]=" "

    # HARD: center priority
    if difficulty=="hard" and 4 in empty:
        board[4]="O"
        return

    # EASY fallback: random
    board[random.choice(empty)] = "O"

def end_game(msg):
    marker.goto(0,0)
    marker.write(msg, align="center", font=("Arial",36,"bold"))
    turtle.onscreenclick(None)

def click_handler(x,y):
    global current_player

    if current_player != "X": return
    i = get_index(x,y)
    if i is None or board[i]!=" ": return

    board[i]="X"
    draw_symbol("X",i)

    if check_winner(): end_game("You Win!"); return
    if " " not in board: end_game("Draw!"); return

    current_player="O"
    cpu_move()

    for j in range(9):
        if board[j]=="O":
            draw_symbol("O",j)

    if check_winner(): end_game("CPU Wins!"); return
    if " " not in board: end_game("Draw!"); return

    current_player="X"

turtle.onscreenclick(click_handler)
turtle.mainloop()
