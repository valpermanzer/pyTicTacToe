board = ["-","-","-","-","-","-","-","-","-"]
gamegoing = True
winner = None
current_player = "X"

def disp_board():
  print(board[0]+ "|" + board[1] + "|" + board[2])
  print(board[3]+ "|" + board[4] + "|" + board[5])
  print(board[6]+ "|" + board[7] + "|" + board[8])

def play_game():
  disp_board()
  while gamegoing:
    turn(current_player)
    gameover()
    flip()

  if winner =="X" or winner =="0":
    print(winner +" won.")
  elif winner == None:
    print("Tie.")

def turn(player):
  pos = input(player + " Choose a position from 1-9: ")

  valid = False
  while not valid:

    while pos not in ["1","2","3","4","5","6","7","8","9"]:
       pos = input("Invalid input." + player + " Choose a position from 1-9: ")    
    pos = int(pos)-1
    if board[pos] == "-":
      valid = True
    else:
      print("You can't go there.")

  board[pos] = player
  disp_board()

def gameover():
  checkwin()
  checktie()

def checkwin():
  global winner

  rwin = checkrow()
  cwin = checkcol()
  dwin = checkdiag()
  if rwin:
    winner = rwin
  elif cwin:
    winner = cwin
  elif dwin:
    winner = dwin
  else:
    winner = None

def checkrow():
  global gamegoing
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"
  if row1 or row2 or row3:
    gamegoing = False
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
    
def checkcol():
  global gamegoing
  col1 = board[0] == board[3] == board[6] != "-"
  col2 = board[1] == board[4] == board[7] != "-"
  col3 = board[2] == board[5] == board[8] != "-"
  if col1 or col2 or col3:
    gamegoing = False
  if col1:
    return board[0]
  elif col2:
    return board[1]
  elif col3:
    return board[2]

def checkdiag():
  global gamegoing
  diag1 = board[0] == board[4] == board[8] != "-"
  diag2 = board[2] == board[4] == board[6] != "-"
  if diag1 or diag2:
    gamegoing = False
  if diag1:
    return board[0]
  elif diag2:
    return board[2]

def checktie():
  global gamegoing
  if "-" not in board:
    gamegoing = False

def flip():
  global current_player

  if current_player =="X":
    current_player = "O"
  elif current_player =="O":
    current_player = "X"

play_game()
