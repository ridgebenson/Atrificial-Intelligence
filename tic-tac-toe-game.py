#Generate random moves
import random

#Print current state of the board
def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

#Check whether the board is full
def isBoardFull(board):
    return ' ' not in board[1:]

#Check all possible win conditions
def isWinner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter))

#Player inputs their move
def playerMove(board):
    while True:
        move = input("Please select a position to enter X between 1 and 9: ")
        try:
            move = int(move)
            if 1 <= move <= 9 and board[move] == ' ':
                #Updating the board
                insertLetter(board, 'X', move)
                break
            else:
                print('Sorry, this space is occupied or not valid. Please try again.')
        except ValueError:
            print('Please type a valid number between 1 and 9.')

#Computer's move
def computerMove(board):
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = None

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = [i for i in possibleMoves if i in [1, 3, 7, 9]]

    if cornersOpen:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = [i for i in possibleMoves if i in [2, 4, 6, 8]]

    if edgesOpen:
        #Randomly choosing among available moves
        move = selectRandom(edgesOpen)
        return move

#Returns a random choice from a list of possible moves
def selectRandom(lst):
    return random.choice(lst)

#Updating the board with a the letter "O" at a given position
def insertLetter(board, letter, pos):
    board[pos] = letter

def main():
    board = [' '] * 10
    print("Welcome to the game!")
    printBoard(board)

    while not isBoardFull(board):
        if not isWinner(board, 'O'):
            playerMove(board)
            printBoard(board)
        else:
            print("Sorry, you lose!")
            break

        if not isWinner(board, 'X'):
            move = computerMove(board)
            if move is None:
                print("It's a tie!")
            else:
                insertLetter(board, 'O', move)
                print('Computer placed an O on position', move, ':')
                printBoard(board)
        else:
            print("You win!")
            break

    if isBoardFull(board):
        print("Tie game")

while True:
    choice = input("Do you want to play? Press 'y' for yes or 'n' for no: ")
    if choice.lower() == 'y':
        main()
    else:
        break
