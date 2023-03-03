# Importing necessary libraries
import sys 
import os

# Constants to represent the dimensions of the game board
ROWS = 6
COLS = 7

# Constants to represent empty spaces and players
EMPTY_SPACE = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'

# Variable to keep track of whether the game is over or not
game_over = False

# Function to create the game board
def createBoard():
    board = {}
    for rowIndex in range(ROWS):
        for columnIndex in range(COLS):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board

# Function to display the game board on the console
def showBoard(board):
    board_spaces = []
    for rowIndex in range(ROWS):
        for columnIndex in range(COLS):
            board_spaces.append(board[(columnIndex, rowIndex)])
            
    print("""
    | 1 2 3 4 5 6 7 |
    +---------------+
    | {} {} {} {} {} {} {} |
    | {} {} {} {} {} {} {} |
    | {} {} {} {} {} {} {} |
    | {} {} {} {} {} {} {} |
    | {} {} {} {} {} {} {} |
    | {} {} {} {} {} {} {} |
    +---------------+
    """.format(*board_spaces))

# Function to get the player's move
def PlayerMove(player_in_turn, board):
    while True:  
        print(f'Player {player_in_turn}, enter a column:')
        response = input('> ').upper().strip()
        columnIndex = int(response) - 1

        # Checking if the selected column is already full
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print('That column is full, select another one.')
            continue  
        
        # Finding the first empty slot from the bottom of the selected column
        for rowIndex in range(ROWS - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)

# Function to check if a player has won
def isWinner(player_in_turn, board):

    # Checking for horizontal wins
    for columnIndex in range(COLS - 3):
        for rowIndex in range(ROWS):
            
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == player_in_turn:
                return True
            
    # Checking for vertical wins        
    for columnIndex in range(COLS):
        for rowIndex in range(ROWS - 3):
            
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_in_turn:
                return True
            
    # Checking for diagonal wins (top-left to bottom-right)        
    for columnIndex in range(COLS - 3):
        for rowIndex in range(ROWS - 3):
            
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_in_turn:
                return True
            
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_in_turn:
                return True
    return False
# Define a function to check if the board is full
def isFull(board):
    # Iterate over each row and column in the board
    for rowIndex in range(ROWS):
        for columnIndex in range(COLS):
            # If any space is empty, return False
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False  
    # If all spaces are filled, return True
    return True  

# Define a function to clear the console screen
def clearScreen():
    os.system('cls')

# Define the main logic of the game
def main_logic():
    # Create a new game board
    game_board = createBoard()
    # Set the first player to move as X
    player_in_turn = PLAYER_X

    # Start an infinite loop to keep playing the game
    while True:  
        # Clear the console screen
        clearScreen()
        # Show the current state of the game board
        showBoard(game_board)
        # Ask the current player to make a move
        playerMove = PlayerMove(player_in_turn, game_board)
        # Update the game board with the player's move
        game_board[playerMove] = player_in_turn

        # Check if the current player has won the game
        if isWinner(player_in_turn, game_board):
            # Clear the console screen
            clearScreen() 
            # Show the final state of the game board
            showBoard(game_board)  
            # Print a message indicating the winner
            print('Player ' + player_in_turn + ' has won!')
            # Exit the program
            sys.exit()

        # Check if the game board is full (i.e., a tie)
        elif isFull(game_board):
            # Clear the console screen
            clearScreen() 
            # Show the final state of the game board
            showBoard(game_board)  
            # Print a message indicating a tie
            print('There is a tie!')
            # Exit the program
            sys.exit()

        # Switch the turn to the other player
        if player_in_turn == PLAYER_X:
            player_in_turn = PLAYER_O
        elif player_in_turn == PLAYER_O:
            player_in_turn = PLAYER_X

# Call the main logic function to start the game
main_logic()
