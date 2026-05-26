import random


def get_human_coordinates(board, current_player):
    """
    Reads coordinates for the tic tac toe board from the terminal.
    Format: letter + number (e.g. A2, C1).
    Repeats if input is invalid or cell is already taken.
    Typing 'quit' (any capitalization) exits the program.
    Returns a tuple of two integers (row, col), both 0-indexed.
    """
    row_map = {'A': 0, 'B': 1, 'C': 2}
    col_map = {'1': 0, '2': 1, '3': 2}

    while True:
        user_input = input(f"Player {current_player}, enter your move (e.g. A1, quit to quit): ").strip()

        if user_input.lower() == 'quit':
            print("Thanks for playing! Goodbye.")
            exit()

        if len(user_input) != 2:
            print("Invalid input. Please enter a letter (A-C) followed by a number (1-3), e.g. B2.")
            continue

        row_char = user_input[0].upper()
        col_char = user_input[1]

        if row_char not in row_map or col_char not in col_map:
            print("Invalid coordinates. Row must be A-C and column must be 1-3.")
            continue

        row = row_map[row_char]
        col = col_map[col_char]

        if board[row][col] != '.':
            print("That cell is already taken. Please choose an empty cell.")
            continue

        return (row, col)


def get_random_ai_coordinates(board, current_player):
    """
    Returns a tuple of 2 integers (row, col) for a random free cell on the board.
    Each number is between 0-2.
    Returns None if the board is full.
    """
    free_cells = [
        (row, col)
        for row in range(3)
        for col in range(3)
        if board[row][col] == '.'
    ]

    if not free_cells:
        return None

    return random.choice(free_cells)


def get_unbeatable_ai_coordinates(board, current_player):
    """
    Returns a tuple of 2 integers (row, col) using the Minimax algorithm.
    Always blocks the opponent from winning and maximizes the AI's chances.
    Returns None if the board is full.
    """
    free_cells = [
        (row, col)
        for row in range(3)
        for col in range(3)
        if board[row][col] == '.'
    ]

    if not free_cells:
        return None

    opponent = 'O' if current_player == 'X' else 'X'

    def minimax(board, is_maximizing):
        winner = _get_winner(board)
        if winner == current_player:
            return 1
        if winner == opponent:
            return -1
        if _is_full(board):
            return 0

        if is_maximizing:
            best = -2
            for r in range(3):
                for c in range(3):
                    if board[r][c] == '.':
                        board[r][c] = current_player
                        score = minimax(board, False)
                        board[r][c] = '.'
                        best = max(best, score)
            return best
        else:
            best = 2
            for r in range(3):
                for c in range(3):
                    if board[r][c] == '.':
                        board[r][c] = opponent
                        score = minimax(board, True)
                        board[r][c] = '.'
                        best = min(best, score)
            return best

    best_score = -2
    best_move = None

    for (row, col) in free_cells:
        board[row][col] = current_player
        score = minimax(board, False)
        board[row][col] = '.'
        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move


def _get_winner(board):
    """Helper: returns 'X', 'O', or None based on the current board state."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '.':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '.':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]
    return None


def _is_full(board):
    """Helper: returns True if no empty cells remain."""
    return all(board[r][c] != '.' for r in range(3) for c in range(3))


# Run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    board_1 = [
        ["X", "X", "."],
        ["X", ".", "."],
        ["X", "X", "."],
    ]
    print("It should print the coordinates selected by the human player")
    coordinates = get_human_coordinates(board_1, "X")
    print(coordinates)

    board_2 = [
        ["O", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2))
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2))
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2))

    board_3 = [
        ["O", "X", "X"],
        ["X", "O", "X"],
        ["X", "O", "X"],
    ]
    print("The printed coordinate should be None")
    print(get_random_ai_coordinates(board_3))

    board_4 = [
        [".", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("The printed coordinate should always be (0, 0)")
    print(get_unbeatable_ai_coordinates(board_4, "X"))

    board_5 = [
        ["X", "O", "."],
        ["X", ".", "."],
        ["O", "O", "X"],
    ]
    print("The printed coordinate should always be (1, 1)")
    print(get_unbeatable_ai_coordinates(board_5, "O"))

    board_6 = [
        ["O", "O", "."],
        ["O", "X", "."],
        [".", "X", "."],
    ]
    print("The printed coordinate should either (0, 2) or (2, 0)")
    print(get_unbeatable_ai_coordinates(board_6, "X"))