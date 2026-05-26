from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


def get_coordinates(game_mode, board, current_player):
    """
    Returns the appropriate coordinates based on game mode and current player.
    - HUMAN_VS_HUMAN:        both players are human
    - RANDOM_AI_VS_RANDOM_AI: both players are random AI
    - HUMAN_VS_RANDOM_AI:    X is human, O is random AI
    - HUMAN_VS_UNBEATABLE_AI: X is human, O is unbeatable AI
    """
    if game_mode == HUMAN_VS_HUMAN:
        return get_human_coordinates(board, current_player)

    if game_mode == RANDOM_AI_VS_RANDOM_AI:
        return get_random_ai_coordinates(board, current_player)

    if game_mode == HUMAN_VS_RANDOM_AI:
        if current_player == 'X':
            return get_human_coordinates(board, current_player)
        else:
            print("Random AI is making a move...")
            return get_random_ai_coordinates(board, current_player)

    if game_mode == HUMAN_VS_UNBEATABLE_AI:
        if current_player == 'X':
            return get_human_coordinates(board, current_player)
        else:
            print("Unbeatable AI is making a move...")
            return get_unbeatable_ai_coordinates(board, current_player)


def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    current_player = 'X'
    is_game_running = True

    while is_game_running:
        display_board(board)

        coordinates = get_coordinates(game_mode, board, current_player)

        if coordinates is None:
            break

        x, y = coordinates
        board[x][y] = current_player

        winning_player = get_winning_player(board)
        its_a_tie = is_board_full(board)

        if winning_player:
            display_board(board)
            print(f"{winning_player} has won!")
            is_game_running = False
        elif its_a_tie:
            display_board(board)
            print("It's a tie!")
            is_game_running = False
        else:
            # Alternate player: X -> O, O -> X
            current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()