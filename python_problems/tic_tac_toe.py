import random

def display_board(board):
    print(board[9]+"|"+board[8]+"|"+board[7])
    print("-"+"+"+"-"+"+"+"-")
    print(board[6]+"|"+board[5]+"|"+board[4])
    print("-" + "+" + "-" + "+" + "-")
    print(board[3]+"|"+board[2]+"|"+board[1])

def user_input():
   marker=""
   while not ( marker.upper()=="X" or marker.upper()=="O"):
       marker=input(" player 1 choose X or O")
   player1=marker
   if player1=="X":
       player2="O"
   else:
       player2="X"
   return (player1,player2)

def place_marker(board,position,marker):
    board[position]=marker
def win_check(board,mark):
    return ((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or (board[7]==board[4]==board[1]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or (board[7]==board[5]==board[3]==mark) or (board[9]==board[5]==board[1]==mark))
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return "player1"
    else:
        return 'player2'
def space_check(board,position):
    return board[position] == " "
def fullboard_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
   pos=0
   while pos not in range(1,10) or not space_check(board,pos):
       pos=int(input("enter your position 1 to 9"))
   return pos
def replay():
    choice=input("play again? yes or no")
    return choice=="yes"
print("-----Welcome to Tic Tac Toe game-----")
while True:
    oboard = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    player1_marker, player2_marker = user_input()
    print("now choosing who is going to play first")
    turn = choose_first()
    print(turn, "going to play first")
    while True:
        if turn == "player1":
            display_board(oboard)
            position = player_choice(oboard)
            place_marker(oboard, position, player1_marker)
            if win_check(oboard, player1_marker):
                display_board(oboard)
                print("player 1 has won")
                break
            else:
                if fullboard_check(oboard):
                    display_board(oboard)
                    print("game is a TIE")
                    break
                else:
                    turn="player2"
        else:
            display_board(oboard)
            position = player_choice(oboard)
            place_marker(oboard, position, player2_marker)
            if win_check(oboard, player2_marker):
                display_board(oboard)
                print("player 2 has won")
                break
            else:
                if fullboard_check(oboard):
                    display_board(oboard)
                    print("game is a TIE")
                    break
                else:
                    turn = "player1"
    if not replay():
        break


