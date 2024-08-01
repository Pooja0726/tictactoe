import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
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
            print(turn, "wins the game")
            return  # Exit the function if there's a winner
        # If all positions are filled and no win detected, it's a draw
        if all(value != " " for value in board.values()):
            print("Game Draw")
            return  # Exit the function if it's a draw
        turn = "O" if turn == "X" else "X"
# Buttons
button1 = tk.Button(frame1, text="", width=4, height=2)
button1.grid(row=0, column=0)
button1.bind("<Button-1>", play)
button2 = tk.Button(frame1, text="", width=4, height=2)
button2.grid(row=0, column=1)
button2.bind("<Button-1>", play)
button3 = tk.Button(frame1, text="", width=4, height=2)
button3.grid(row=0, column=2)
button3.bind("<Button-1>", play)
button4 = tk.Button(frame1, text="", width=4, height=2)
button4.grid(row=1, column=0)
button4.bind("<Button-1>", play)
button5 = tk.Button(frame1, text="", width=4, height=2)
button5.grid(row=1, column=1)
button5.bind("<Button-1>", play)
button6 = tk.Button(frame1, text="", width=4, height=2)
button6.grid(row=1, column=2)
button6.bind("<Button-1>", play)
button7 = tk.Button(frame1, text="", width=4, height=2)
button7.grid(row=2, column=0)
button7.bind("<Button-1>", play)
button8 = tk.Button(frame1, text="", width=4, height=2)
button8.grid(row=2, column=1)
button8.bind("<Button-1>", play)
button9 = tk.Button(frame1, text="", width=4, height=2)
button9.grid(row=2, column=2)
button9.bind("<Button-1>", play)
root.mainloop()
