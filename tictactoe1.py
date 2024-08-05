import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("400x300")
root.title("Tic Tac Toe")
frame = tk.Frame(root)
frame.pack()
titlelabel = tk.Label(frame, text="Tic Tac Toe", font=("Serif", 12), bg="pink")
titlelabel.pack()
frame1 = tk.Frame(root)
frame1.pack()
board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}
turn = "X"
def checkforwin(player):
    if (board[1] == board[2] and board[2] == board[3] and board[1] == player):
        return True
    elif (board[4] == board[5] and board[5] == board[6] and board[6] == player):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[9] == player):
        return True
    elif (board[1] == board[5] and board[5] == board[9] and board[9] == player):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[7] == player):
        return True
    elif (board[1] == board[4] and board[4] == board[7] and board[7] == player):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[8] == player):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[9] == player):
        return True
    else:
        return False
def play(event):
    global turn
    button = event.widget
    buttontext = str(button)
    clicked = buttontext[-1]
    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)
    if button["text"] == "":
        button["text"] = turn
        board[clicked] = turn
        if checkforwin(turn):
            tk.messagebox.showinfo("Game Over", f"{turn} wins the game!")
            reset_board()
            return  # Exit the function if there's a winner
        # If all positions are filled and no win detected, it's a draw
        if all(value != " " for value in board.values()):
            tk.messagebox.showinfo("Game Over", "Game Draw")
            reset_board()
            return  # Exit the function if it's a draw
        turn = "O" if turn == "X" else "X"
def reset_board():
    global board, turn
    board = {1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "}
    turn = "X"
    for button in buttons:
        button["text"] = ""
# Buttons
buttons = []
for i in range(9):
    button = tk.Button(frame1, text="", width=8, height=4, bg="yellow")
    button.grid(row=i//3, column=i%3)
    button.bind("<Button-1>", play)
    buttons.append(button)
root.mainloop()
