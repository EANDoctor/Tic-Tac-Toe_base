

Dávid — 2026. 05. 01. 17:59
Ez wifi, nyáron be kéne húznom egy kábelt
𝑬𝑨𝑵𝑫𝖔𝖈𝖙𝖔𝖗 — 2026. 05. 01. 18:00
az durván nagyotr menne
Dávid — 2026. 05. 01. 18:00
Gyakorlatban 1000/1000
Mármint papíron
𝑬𝑨𝑵𝑫𝖔𝖈𝖙𝖔𝖗 — 2026. 05. 01. 18:00
lesz az kábellel
Dávid — 2026. 05. 01. 18:00
Szerintem is.
𝑬𝑨𝑵𝑫𝖔𝖈𝖙𝖔𝖗 — 2026. 05. 01. 18:00
de ez így is k*va jó
Dávid — 2026. 05. 01. 18:01
Nem rossz, maradjunk annyiban 🙂
Dávid — 2026. 05. 14. 16:23
Továbbítva
Csatolt fájltípus: acrobat
ágazativ.pdf
4.00 MB
𝑬𝑨𝑵𝑫𝖔𝖈𝖙𝖔𝖗 — 2026. 05. 14. 18:40
Továbbítva
Csatolt fájltípus: unknown
ÁAV - 2025 - PG(1).pka
447.56 KB
Dávid — 21:01
danke
def get_empty_board():
    '''
    Returns a list with 3 sublists.
    Each sublist contains 3 "." characters representing an empty board.
    '''
    return [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]


def display_board(board):
    """
    Prints the tic tac toe board in the format:
       1   2   3
    A  . | . | .
      ---+---+---
    B  . | . | .
      ---+---+---
    C  . | . | .
    """
    print("   1   2   3")
    row_labels = ['A', 'B', 'C']
    for i, row in enumerate(board):
        print(f"{row_labels[i]}  {row[0]} | {row[1]} | {row[2]}")
        if i < 2:
            print("  ---+---+---")


def is_board_full(board):
    """
    Returns True if there are no more empty places on the board,
    otherwise returns False.
    """
    for row in board:
        for cell in row:
            if cell == '.':
                return False
    return True


def get_winning_player(board):
    """
    Returns 'X' or 'O' based on which player has three of their marks
    in a horizontal, vertical, or diagonal row on the board.
    Returns None if no player has won.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '.':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]

    return None


# Run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    empty_board = get_empty_board()
    print(empty_board)

    board = [
        ['X', 'O', '.'],
        ['X', 'O', '.'],
        ['0', 'X', '.']
    ]
    print("""
    should print 
        1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       ---+---+---
    C   0 | X | . 
       ---+---+---
    """)
    display_board(board)

    board_1 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("Should return False")
    print(is_board_full(board_1))

    board_2 = [
        [".", "O", "O"],
        [".", "O", "X"],
... (36 sor maradt)

board.py
4 KB
﻿
def get_empty_board():
    '''
    Returns a list with 3 sublists.
    Each sublist contains 3 "." characters representing an empty board.
    '''
    return [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]


def display_board(board):
    """
    Prints the tic tac toe board in the format:
       1   2   3
    A  . | . | .
      ---+---+---
    B  . | . | .
      ---+---+---
    C  . | . | .
    """
    print("   1   2   3")
    row_labels = ['A', 'B', 'C']
    for i, row in enumerate(board):
        print(f"{row_labels[i]}  {row[0]} | {row[1]} | {row[2]}")
        if i < 2:
            print("  ---+---+---")


def is_board_full(board):
    """
    Returns True if there are no more empty places on the board,
    otherwise returns False.
    """
    for row in board:
        for cell in row:
            if cell == '.':
                return False
    return True


def get_winning_player(board):
    """
    Returns 'X' or 'O' based on which player has three of their marks
    in a horizontal, vertical, or diagonal row on the board.
    Returns None if no player has won.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '.':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]

    return None


# Run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    empty_board = get_empty_board()
    print(empty_board)

    board = [
        ['X', 'O', '.'],
        ['X', 'O', '.'],
        ['0', 'X', '.']
    ]
    print("""
    should print 
        1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       ---+---+---
    C   0 | X | . 
       ---+---+---
    """)
    display_board(board)

    board_1 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("Should return False")
    print(is_board_full(board_1))

    board_2 = [
        [".", "O", "O"],
        [".", "O", "X"],
        [".", "X", "X"],
    ]
    print("Should return False")
    print(is_board_full(board_2))

    board_3 = [
        ["O", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "X"],
    ]
    print("Should return True")
    print(is_board_full(board_3))

    board_4 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("Should return X")
    print(get_winning_player(board_4))

    board_5 = [
        ["X", "O", "O"],
        ["X", "O", "."],
        ["O", "X", "X"],
    ]
    print("Should return O")
    print(get_winning_player(board_5))

    board_6 = [
        ["O", "O", "."],
        ["O", "X", "."],
        [".", "X", "."],
    ]
    print("Should return None")
    print(get_winning_player(board_6))