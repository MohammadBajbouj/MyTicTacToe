# Last updated: 2026-09-03 14:18:32

import sys

LEGEND_BOARD = [str(i + 1) for i in range(9)]


def board_lines(board):
    lines = []
    for row in range(3):
        cells = board[row * 3:row * 3 + 3]
        lines.append(" " + " | ".join(cells))
        if row < 2:
            lines.append("---+---+---")
    return lines


def print_board(board):
    legend_lines = board_lines(LEGEND_BOARD)
    play_lines = board_lines(board)

    print()
    print(f"{'Legend':<14}Board")
    for legend_line, play_line in zip(legend_lines, play_lines):
        print(f"{legend_line:<14}{play_line}")
    print()


def has_three_in_a_row(board, player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # across
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # down
        (0, 4, 8), (2, 4, 6),             # diagonally
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def get_valid_space(board, current_player):
    while True:
        choice = input(f"Player {current_player}, choose a space (1-9, or x to exit): ")

        if choice.strip().lower() == "x":
            print("Thanks for playing! Goodbye.")
            sys.exit()

        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        space = int(choice) - 1

        if space not in range(9):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if board[space] != " ":
            print("That space is taken. Choose another space.")
            continue

        return space


def play_game():
    # Make a 3 x 3 board and leave all the spaces empty.
    board = [" " for _ in range(9)]

    # Player X goes first.
    current_player = "X"

    while True:
        # Show the board to the players.
        print_board(board)

        # Ask the current player where they want to put their X or O.
        space = get_valid_space(board, current_player)

        # Place their symbol on the board.
        board[space] = current_player

        # Check if the player has three of their symbols in a row,
        # either across, down, or diagonally.
        if has_three_in_a_row(board, current_player):
            # Tell them they won.
            print_board(board)
            print(f"Player {current_player} won!")
            return

        # Check if the board is full with no winner.
        if " " not in board:
            print_board(board)
            print("It's a draw!")
            return

        # Switch to the other player for the next turn.
        current_player = "O" if current_player == "X" else "X"


# Start the game.
print("Welcome to Tic-Tac-Toe!")

while True:
    play_game()

    while True:
        answer = input("Play again? (y for yes, n for no): ").strip().upper()
        if answer in ("Y", "N"):
            break
        print("Invalid input. Please answer with y or n.")

    if answer == "N":
        print("Thanks for playing!")
        break
