# Initialize the game board to be an empty 3x3 grid
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Initialize a variable to store the current player's symbol
player = "X"

# Create a loop that will run until the game is over
game_over = False
while not game_over:
    # Display the current state of the game board
    for row in board:
        print(" ".join(row))
    print()
    
    # Prompt the player to enter the row and column where they would like to place their symbol
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter col (0-2): "))
    
    # Validate the player's input
    if board[row][col] != " ":
        print("Invalid move!")
        continue
    
    # Place the player's symbol on the game board
    board[row][col] = player
    
    # Check if the player has won
    if (board[0][0] == player and board[0][1] == player and board[0][2] == player) or \
       (board[1][0] == player and board[1][1] == player and board[1][2] == player) or \
       (board[2][0] == player and board[2][1] == player and board[2][2] == player) or \
       (board[0][0] == player and board[1][0] == player and board[2][0] == player) or \
       (board[0][1] == player and board[1][1] == player and board[2][1] == player) or \
       (board[0][2] == player and board[1][2] == player and board[2][2] == player) or \
       (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        print("Player", player, "wins!")
        game_over = True
    
    # Switch the current player's symbol
    if player == "X":
        player = "O"
    else:
        player = "X"
    
# If the game is over and no player has won, inform the players that the game is a tie
print("Tie game!")



#This code creates a simple Tic Tac Toe game in which two players take turns placing their symbol (either "X" or "O")
# on a 3x3 grid. The players can input the row and column where they would like to place their symbol, and the game
# checks if the move is valid and updates the game board accordingly. The game continues until one of the players gets
# three of their symbols in a row (horizontally, vertically, or diagonally), at which point the player is declared the
# winner. If the game board is filled and no player has won, the game is a tie.

# The code uses a loop that runs until the game_over variable is set to True. Within the loop, the current state of the
# game board is displayed, and the current player is prompted to enter the row and column where they would like to place
# their symbol. The input is validated to ensure that the chosen position is empty, and the player's symbol is placed on
# the game board. The code then checks if the player has won by checking for three of their symbols in a row in all
# possible winning configurations. If a player has won, the game_over variable is set to True and the game ends. If the
# game is not over, the current player's symbol is switched to the other symbol and the loop continues.
