import tkinter as tk
from tkinter import ttk #idk what ttk does but i saw someone smart do it so here it is
import random #for the easy bot, or when actually rolling the dice for who goes first.

def clicked(r, c, tile): # function is imbued in buttons
    global turn
    if board[r][c]["text"] != " ": # If the tile is not available, do nothing
        return
    else:
        board[r][c]["text"] = player[turn%2] #sets tile to current player.
        turn += 1
        announce_winner()
        return
    
#I am changing this to see if Git ackowledges it.

def announce_winner():
    winner = check_winner()
    if winner in player:
        label = tk.Label(window, text=winner+" wins!", fg="white", bg="black")
        label.pack()
        end_game()
    elif winner is False:
        label = tk.Label(window, text="It's a draw!", fg="white", bg="black")
        label.pack()
        end_game()
    else:
        return None #does nothing if winner is None, game continues
        
def end_game():
    #Pop up window asking to end game, restart, or return to menu
    pass

def check_winner(): #returns winner if exists, False if draw, None if game continues
    global player, turn
    if 4 < turn: # No need to check before a winner can exist
        for row in range(3): # Checks horizontal wins
            if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] != " ":
                if board[row][0]["text"] == player[0]:
                    return player[0]
                else:
                    return player[1]
        for col in range(3): # Checks vertical wins
            if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != " ":
                if board[0][col]["text"] == player[0]:
                    return player[0]
                else:
                    return player[1]
        if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != " ": # Checks diagonal 1
            if board[0][0]["text"] == player[0]:
                return player[0]
            else:
                return player[1]
        if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != " ": # Checks diagonal 2
            if board[0][2]["text"] == player[0]:
                return player[0]
            else:
                return player[1]
    if turn > 8: # Shows a draw only if board is full and no win is found
        return False
    
def generate_board():
    board = [] #Generates an empty board with a 3x3 array of buttons. Ensure that clicked calls next_turn when successful.
    for row in range(3):
        row_list = []
        for col in range(3):
            tile = tk.Button(frame, text = " ", width = 8, height = 4, command = lambda r = row, c = col: clicked(r,c, tile)) #links the rows and cols to button
            tile.grid(row = row, column = col) # Keyword from .grid = row & col we create ranging up to 3.
            row_list.append(tile) #appends the newest tile to row_list before overwriting tile
        board.append(row_list) #appends row_list before overwriting row_list. Elegant move here -- not my idea.
    return board

def reset_board():
    global board, turn
    board = generate_board()
    turn = 0 #change if desired
    return
    
#____________________________________________________________________________________________________________________________


window = tk.Tk()
window.title("Tic Tac Toe")
window.configure(bg="black")
# Creates window with a black background, obviously.
frame = tk.Frame(window)
frame.pack()

player = ["X", "O"] #a list of all players, and we'll index thru it mod2 to select our player
turn = 0 # Separates the turn count from the player -- eg after 9 turns, the game is over.

board = generate_board()

reset_button = tk.Button(window, text = "Restart", command = reset_board)
reset_button.pack(pady = 10)


window.mainloop()

