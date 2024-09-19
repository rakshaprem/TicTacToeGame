import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentPlayer = "x"
winner = None
gameRunning = True

#printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("------------")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("-------------")      
    print(board[6] + " | " + board[7] + " | " + board[8] + " | ")

#take player input
def playerInput(board):
    inp = int(input(" Enter a number :"))
    if inp >= 1 and inp <=9 and board[inp-1]=="-":
        board[inp-1] = currentPlayer
    else:
        print("oops the input is invalid")
        
#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("its a tie!")
        gameRunning = False

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print("the winner is",winner)
        
        
#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"
#computer
def computer(board):
    while currentPlayer == "o":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "o"
            switchPlayer()

#Main Program
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)


