from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        if check_winner():
            label.config(text=f"{player} Kazandı")
        elif check_tie():
            label.config(text="Berabere")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player} .Sırası")

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            highlight_winner(i, 0, i, 1, i, 2)
            return True

        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            highlight_winner(0, i, 1, i, 2, i)
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_winner(0, 0, 1, 1, 2, 2)
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_winner(0, 2, 1, 1, 2, 0)
        return True

    return False

def highlight_winner(x1, y1, x2, y2, x3, y3):
    buttons[x1][y1].config(bg="green")
    buttons[x2][y2].config(bg="green")
    buttons[x3][y3].config(bg="green")

def check_tie():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return False
    return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player} turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
            buttons[row][column]['bg'] = "#F0F0F0"

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=f"{player} turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Yeniden Başlat", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
