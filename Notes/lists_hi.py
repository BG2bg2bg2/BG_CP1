# BG 1st list notes
#import random
#not_sibs = ["mom", "dad", "Ammon", "Fred", "Nielsen", "Russle", "Gabrel", "Alma", "Nephi", 5.76, False]

#for a in not_sibs:
    #print(not_sibs[5])
    #print(random.choice(not_sibs, weights=[10, 10, 10, 10, 10,10], k=5))
    #print(f"the list is, {len(not_sibs)} people long")
    #print(not_sibs)
    #replacing is this
   # not_sibs[0] = "Eric"
   # #not this
   # #not_sibsreplace("Fred", "Parker") this only works for strings

#    not_sibs[6:-1] = ["lavender", "Green"]
 #   not_sibs.pop()
 #   not_sibs.pop(6)
  #  not_sibs.remove("dad")

    #not_sibs clear()
    #not_sibs.append("Fred") adds to the end of the list
    #not_sibs.insert(2, "Anderwel")
    #adds things the the end of the list
   # not_sibs.extend(["Joseph", "Isreal", "USA"])
   # print(not_sibs)
   # continue
#else:


# Tic-Tac-Toe Game

# Step 1: Create the board
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# Step 2: Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Step 3: Function to make a move
def make_move(board, position, player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == position:
                board[i][j] = player
                return True
    return False  # if position is already taken

# Step 4: Function to check for a win
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Step 5: Function to check for a draw
def check_draw(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

# Step 6: Game loop
current_player = "X"
while True:
    print_board(board)
    move = input(f"Player {current_player}, choose a position: ")
    
    if not make_move(board, move, current_player):
        print("Invalid move, try again.")
        continue
    
    if check_win(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break
    
    if check_draw(board):
        print_board(board)
        print("It's a draw!")
        break
    
    current_player = "O" if current_player == "X" else "X"

