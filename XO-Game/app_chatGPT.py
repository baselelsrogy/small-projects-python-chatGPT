from tkinter import *
import random


# ---------------------- GAME LOGIC FUNCTIONS ---------------------- #

def next_turn(row, column):
    """Handles a player's move and updates game state."""
    global current_player, player1_score, player2_score

    # Ignore clicks if square already used or game over
    if board_buttons[row][column]["text"] != "" or check_winner() is not False:
        return

    # Mark the current square
    board_buttons[row][column]["text"] = current_player

    # Check for win or tie
    result = check_winner()

    if result is False:
        # Switch turns if no winner
        current_player = players[1] if current_player == players[0] else players[0]
        status_label.config(text=f"{current_player}'s Turn")

    elif result is True:
        # Update score for the winner
        if current_player == players[0]:
            player1_score += 1
            player1_score_label.config(text=str(player1_score))
            status_label.config(text="Player 1 Wins!")
        else:
            player2_score += 1
            player2_score_label.config(text=str(player2_score))
            status_label.config(text="Player 2 Wins!")

    elif result == "tie":
        status_label.config(text="It's a Tie!")


def check_winner():
    """Checks for a winner or tie, and highlights the winning cells."""
    # Check rows
    for row in range(3):
        if (board_buttons[row][0]["text"] ==
            board_buttons[row][1]["text"] ==
            board_buttons[row][2]["text"] != ""):
            highlight_cells([(row, 0), (row, 1), (row, 2)])
            return True

    # Check columns
    for col in range(3):
        if (board_buttons[0][col]["text"] ==
            board_buttons[1][col]["text"] ==
            board_buttons[2][col]["text"] != ""):
            highlight_cells([(0, col), (1, col), (2, col)])
            return True

    # Check diagonals
    if (board_buttons[0][0]["text"] ==
        board_buttons[1][1]["text"] ==
        board_buttons[2][2]["text"] != ""):
        highlight_cells([(0, 0), (1, 1), (2, 2)])
        return True

    if (board_buttons[0][2]["text"] ==
        board_buttons[1][1]["text"] ==
        board_buttons[2][0]["text"] != ""):
        highlight_cells([(0, 2), (1, 1), (2, 0)])
        return True

    # Check tie (no empty squares left)
    if not has_empty_squares():
        highlight_all("#78A083")
        return "tie"

    return False


def has_empty_squares():
    """Returns True if there are empty squares left on the board."""
    for row in range(3):
        for col in range(3):
            if board_buttons[row][col]["text"] == "":
                return True
    return False


def highlight_cells(cells):
    """Highlights specific cells (used when a player wins)."""
    for row, col in cells:
        board_buttons[row][col].config(bg="#78B9B5")


def highlight_all(color):
    """Highlights all cells (used when it's a tie)."""
    for row in range(3):
        for col in range(3):
            board_buttons[row][col].config(bg=color)


def restart_game():
    """Resets the board and starts a new round."""
    global current_player
    current_player = random.choice(players)
    status_label.config(text=f"{current_player}'s Turn")

    # Reset all cells
    for row in range(3):
        for col in range(3):
            board_buttons[row][col].config(text="", bg="#0F828C")


# ---------------------- UI SETUP ---------------------- #

app = Tk()
app.title("Tic-Tac-Toe (X-O Game)")
app.geometry("700x600")
app.configure(bg="#DEDED1")

# Players and scores
players = ["X", "O"]
current_player = random.choice(players)
player1_score = 0
player2_score = 0

# --- Title ---
title_frame = Frame(app, bg="#DEDED1")
Label(title_frame, text="X-O Game", fg="#222831", font="Arial 35 bold", bg="#DEDED1").grid(row=0, column=0, pady=10)
title_frame.pack()

# --- Scoreboard ---
score_frame = Frame(app, bg="#DEDED1")
Label(score_frame, text="Player 1:", font="Arial 23 bold", fg="#234C6A", bg="#DEDED1").grid(row=0, column=0)
player1_score_label = Label(score_frame, text=str(player1_score), font="Arial 27 bold", fg="#471396", bg="#DEDED1")
player1_score_label.grid(row=0, column=1, padx=(10, 50))

Label(score_frame, text="Player 2:", font="Arial 23 bold", fg="#234C6A", bg="#DEDED1").grid(row=0, column=2)
player2_score_label = Label(score_frame, text=str(player2_score), font="Arial 27 bold", fg="#471396", bg="#DEDED1")
player2_score_label.grid(row=0, column=3)
score_frame.pack(pady=(20, 0))

# --- Game Board ---
board_frame = Frame(app, bg="#DEDED1")
board_frame.pack(pady=(20, 0))

board_buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        btn = Button(
            board_frame,
            text="",
            font="Arial 20 bold",
            fg="white",
            width=10,
            height=3,
            bg="#0F828C",
            command=lambda r=row, c=col: next_turn(r, c)
        )
        btn.grid(row=row, column=col)
        board_buttons[row][col] = btn

# --- Restart + Status ---
bottom_frame = Frame(app, bg="#DEDED1")
bottom_frame.pack(fill="x", pady=10)

Button(bottom_frame, text="Restart", font="Arial 15 bold", bg="#1F7D53", fg="white", command=restart_game)\
    .grid(row=0, column=0, sticky="w", padx=94)

status_label = Label(bottom_frame, text=f"{current_player}'s Turn", font="Arial 18 bold", bg="#DEDED1", fg="#FF204E")
status_label.grid(row=0, column=1, sticky="e", padx=94)

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(1, weight=1)

# ---------------------- RUN APP ---------------------- #
app.mainloop()
