import numpy as np

board = np.array([['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']])
player1_symbol = "X"
player2_symbol = "O"


def check_rows(symbol):
    for row in range(len(board)):
        count = 0
        for column in range(len(board)):
            if board[row][column] == symbol:
                count += 1
        if count == 3:
            print(symbol, "won")
            return True
    return False

def check_columns(symbol):
    for column in range(len(board)):
        count = 0
        for row in range(len(board)):
            if board[row][column] == symbol:
                count += 1
        if count == 3:
            print(symbol, "won")
            return True
    return False

def check_diagonals(symbol):
    if board[2][0] == board[1][1] == board[0][2] == symbol:
        print(symbol, "won")
        return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        print(symbol, "won")
        return True
    return False


def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagonals(symbol)


def place_the_symbol(symbol):
    print(np.matrix(board))
    while (1):
        row = int(input("Enter the row(max row is 3): "))
        column = int(input("Enter the column(max column is 3): "))
        if 0 < row < 4 and 0 < column < 4 and board[row - 1][column - 1] == "*":
            break
        else:
            print("Wrong choice!!!")
    board[row - 1][column - 1] = symbol



def play():
    for turn in range(9):
        if turn % 2 == 0:
            print("Player 1 it's your chance: ")
            place_the_symbol(player1_symbol)
            if won(player1_symbol):
                break
        else:
            print("Player 2 it's your chance: ")
            place_the_symbol(player2_symbol)
            if won(player2_symbol):
                break
    if turn == 8 and not (won(player1_symbol)) and not won((player2_symbol)):
        print("It's a Draw")

play()