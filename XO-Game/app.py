from tkinter import *
import random

# logic game
def next_turn(row, column):
  """Handles a player's move and updates game state"""
  # to access variable outside function
  global player 
  global score_player
  global user2_score

  if game_sqares[row][column]["text"] == "" and is_win() is False:
    if player == chooses[0]:
      game_sqares[row][column]["text"] = player
      
      if is_win() is False:
        # swape player
        player = chooses[1]
        msg_label.config(text=f"{chooses[1]} Turn")

      elif is_win() is True:
        score_player += 1
        user_score_label.config(text=f"{score_player}")
        msg_label.config(text=f"{player} Win!")

      elif is_win() == "tie":
        msg_label.config(text="Tie!")

    else:
      game_sqares[row][column]["text"] = player
      
      if is_win() is False:
        # swape player
        player = chooses[0]
        msg_label.config(text=f"{chooses[0]} Turn")

      elif is_win() is True:
        user2_score += 1
        user2_score_label.config(text=f"{user2_score}")
        msg_label.config(text=f"{player} Win!")

      elif is_win() == "tie":
        msg_label.config(text="It's a Tie!")
    
def is_win():
  """Check if some player won! in cases"""
  for row in range(3):
    if game_sqares[row][0]["text"] == game_sqares[row][1]["text"] == game_sqares[row][2]["text"] != "" :
      game_sqares[row][0].config(bg="#78B9B5")
      game_sqares[row][1].config(bg="#78B9B5")
      game_sqares[row][2].config(bg="#78B9B5")
      return True
  
  for column in range(3):
    if game_sqares[0][column]["text"] == game_sqares[1][column]["text"] == game_sqares[2][column]["text"] != "":
      game_sqares[0][column].config(bg="#78B9B5")
      game_sqares[1][column].config(bg="#78B9B5")
      game_sqares[2][column].config(bg="#78B9B5")
      return True
  
  if game_sqares[0][0]["text"] == game_sqares[1][1]["text"] == game_sqares[2][2]["text"] != "":
    game_sqares[0][0].config(bg="#78B9B5")
    game_sqares[1][1].config(bg="#78B9B5")
    game_sqares[2][2].config(bg="#78B9B5")
    return True

  elif game_sqares[0][2]["text"] == game_sqares[1][1]["text"] == game_sqares[2][0]["text"] != "":
    game_sqares[0][2].config(bg="#78B9B5")
    game_sqares[1][1].config(bg="#78B9B5")
    game_sqares[2][0].config(bg="#78B9B5")
    return True
  
  elif is_empty() is False:
    for row in range(3):
      for column in range(3):
        game_sqares[row][column].config(bg="#78A083")
    return "tie"
  
  else:
    return False
  
def is_empty():
  """Returns True if there are empty squares left on the board."""
  empty_spaces = 9
  
  for row in range(3):
    for column in range(3):
      if game_sqares[row][column]["text"] != "":
        empty_spaces -= 1      

  if empty_spaces == 0:
    return False
  else:
    return True
  
def restart_game():
  """To restart game as you play first time with save the current score"""
  global player
  player = random.choice(chooses)

  msg_label.config(text=f"{player} Turn")
  for row in range(3):
    for column in range(3):
      game_sqares[row][column].config(text="", bg="#0F828C")

# initialize the app
app = Tk()
app.title("XO Game")
app.geometry("700x600")
app.configure(bg="#DEDED1") 

# random chooses
chooses = ["X", "O"]
player = random.choice(chooses)

# title
title_frame = Frame(app, bg="#DEDED1")
title_label = Label(title_frame, text="X-O Game", fg="#222831", font="Arial 35 bold", bg="#DEDED1")
title_label.grid(row=0, column=0, pady=10)
title_frame.pack()

score_player = 0
user2_score = 0

# Frame Scores
frame_score = Frame(app, bg="#DEDED1")
user_label = Label(frame_score, text="Player 1 :", font="Arial 23 bold", fg="#234C6A", bg="#DEDED1")
user_label.grid(row=0, column=0)
user_score_label = Label(frame_score, text=f"{score_player}", font="Arial 27 bold", fg="#471396", bg="#DEDED1")
user_score_label.grid(row=0, column=1)

user2_label = Label(frame_score, text="Player 2 :", font="Arial 23 bold", fg="#234C6A", bg="#DEDED1")
user2_label.grid(row=0, column=2, padx=(200, 0))
user2_score_label = Label(frame_score, text=f"{user2_score}", font="Arial 27 bold", fg="#471396", bg="#DEDED1")
user2_score_label.grid(row=0, column=3)

frame_score.pack(pady=(20,0))

# Frame 3x3
game_sqares = [[1, 2, 3], 
               [4, 5, 6],
               [7, 8, 9],]

square_Frame = Frame(app, bg="#DEDED1")
square_Frame.pack(pady=(20,0))

for row in range(3):
  for column in range(3):
    game_sqares[row][column] = Button(square_Frame, text="", font="Arial 20 bold", fg="white", width=10, height=3, bg="#0F828C", command= lambda row=row, column=column: next_turn(row, column))
    game_sqares[row][column].grid(row=row, column=column)

# Frame restart button and label message
end_frame = Frame(app, bg="#DEDED1")
end_frame.pack(fill="x")

btn_rest = Button(end_frame, text="Restart", font="Arial 15 bold", bg="#1F7D53", fg="white", command=restart_game)
btn_rest.grid(row=0, column=0, sticky="w", padx=(94,0), pady=10)

msg_label = Label(end_frame, text="Start", font="Arial 18 bold", bg="#DEDED1", fg="#FF204E")
msg_label.grid(row=0, column=1, sticky="e", padx=(0, 94), pady=10)

end_frame.columnconfigure(0, weight=1)
end_frame.columnconfigure(1, weight=1)

app.mainloop()