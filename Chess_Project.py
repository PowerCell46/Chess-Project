def white_pawn(current_row, current_column, final_row, final_column):
    if current_column == final_column:  # Moving forward

        if current_row == 6:  # This is the pawn's first move
            if current_row - 1 == final_row:
                new_position_figure = chess_board[current_row - 1][final_column]  # checking what is on the new position
                if new_position_figure != "⬜ ":
                    return "The entered position is invalid and you have wasted your move"
                chess_board[current_row][current_column] = "⬜ "
                chess_board[current_row - 1][current_column] = "♙"

            elif current_row - 2 == final_row:
                new_position_figure = chess_board[current_row - 1][final_column]  # checking what is on the new position
                if new_position_figure != "⬜ ":
                    return "The entered position is invalid and you have wasted your move"

                new_position_figure = chess_board[current_row - 2][final_column]  # checking what is on the new position
                if new_position_figure != "⬜ ":
                    return "The entered position is invalid and you have wasted your move"
                chess_board[current_row][current_column] = "⬜ "
                chess_board[current_row - 2][current_column] = "♙"

            else:
                return "You have entered an invalid row and you have wasted your move"

        else:  # This is not the pawn's first move
            if current_row - 1 == final_row:
                new_position_figure = chess_board[current_row - 1][final_column]  # checking what is on the new position
                if new_position_figure != "⬜ ":
                    return "The entered position is invalid and you have wasted your move"
                chess_board[current_row][current_column] = "⬜ "
                chess_board[current_row - 1][current_column] = "♙"

            else:
                return "You have entered an invalid row and you have wasted your move"

    else:  # Taking another figure
        if current_row - 1 != final_row:  # Checking if the final row is invalid
            return "You have entered an invalid row and you have wasted your move"

        if current_column - 1 == final_column or current_column + 1 == final_column:
            new_position_figure = chess_board[final_row][final_column]
            if new_position_figure not in black_figures:
                return "The position that you want to take is not valid and you have wasted your move."

            chess_board[current_row][current_column] = "⬜ "
            chess_board[final_row][final_column] = "♙"
            return f'You took an opponent\'s figure!'

        else:
            return "The entered position is invalid and you have wasted your move"


def black_pawn(current_row, current_column, final_row, final_column):
    if current_column == final_column:  # Moving forward

        if current_row == 1:  # This is the pawn's first move
            if current_row + 1 == final_row:
                new_position_figure = chess_board[current_row + 1][final_column]  # checking what is on the new position
                if new_position_figure != "⬜ ":
                    return "The entered position is invalid and you have wasted your move"
                chess_board[current_row][current_column] = "⬜ "
                chess_board[current_row + 1][current_column] = "♟︎"

            elif current_row + 2 == final_row:
                new_position_figure = chess_board[current_row + 1][final_column]  # checking what is on the new position
                if new_position_figure != "⬜ ":
                    return "The entered position is invalid and you have wasted your move"

                new_position_figure = chess_board[current_row + 2][final_column]  # checking what is on the new position
                if new_position_figure != "⬜ ":
                    return "The entered position is invalid and you have wasted your move"
                chess_board[current_row][current_column] = "⬜ "
                chess_board[current_row + 2][current_column] = "♟︎"

            else:
                return "You have entered an invalid row and you have wasted your move"

        else:  # This is not the pawn's first move
            if current_row + 1 == final_row:
                new_position_figure = chess_board[current_row + 1][final_column]  # checking what is on the new position
                if new_position_figure != "⬜ ":
                    return "The entered position is invalid and you have wasted your move"
                chess_board[current_row][current_column] = "⬜ "
                chess_board[current_row + 1][current_column] = "♟︎"
                return f'You took an opponent\'s figure!'

            else:
                return "You have entered an invalid row and you have wasted your move"

    else:  # Taking another figure
        if current_row + 1 != final_row:  # Checking if the final row is invalid
            return "You have entered an invalid row and you have wasted your move"

        if current_column - 1 == final_column or current_column + 1 == final_column:
            new_position_figure = chess_board[final_row][final_column]
            if new_position_figure not in white_figures:
                return "The position that you want to take is not valid and you have wasted your move."

            chess_board[current_row][current_column] = "⬜ "
            chess_board[final_row][final_column] = "♟︎"

        else:
            return "The entered position is invalid and you have wasted your move"


chess_board = [["⬜ " for pos in range(8)] for row in range(8)]

chess_figures_dictionary = {
    "♙": white_pawn,
    "♘": "white_knight",
    "♗": "white_bishop",
    "♖": "white_rook",
    "♕": "white_queen",
    "♔": "white_king",

    "♟︎": black_pawn,
    "♞": "black_knight",
    "♝": "black_bishop",
    "♜": "black_rook",
    "♛": "black_queen",
    "♚": "black_king"}

white_figures = ["♙", "♘", "♗", "♖", "♕", "♔"]
black_figures = ["♟︎", "♞", "♝", "♜", "♛", "♚"]
chess_rows_dictionary = {8: 0, 7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}
chess_columns_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}


def initializing_black_figures():
    for pos in range(8):
        chess_board[1][pos] = "♟︎"

    chess_board[0][0] = "♜"
    chess_board[0][7] = "♜"

    chess_board[0][1] = "♞"
    chess_board[0][6] = "♞"

    chess_board[0][2] = "♝"
    chess_board[0][5] = "♝"

    chess_board[0][3] = "♚"
    chess_board[0][4] = "♛"


def initializing_white_figures():
    for position in range(8):
        chess_board[6][position] = "♙"

    chess_board[7][0] = "♖"
    chess_board[7][7] = "♖"

    chess_board[7][1] = "♘"
    chess_board[7][6] = "♘"

    chess_board[7][2] = "♗"
    chess_board[7][5] = "♗"

    chess_board[7][3] = "♕"
    chess_board[7][4] = "♔"


initializing_white_figures()
initializing_black_figures()

for row in chess_board:
    print(" ".join(row))


def validate_positions(current_selected_row, current_selected_column, final_selected_row, final_selected_column):
    if current_selected_row < 0 or current_selected_row > 7 or current_selected_column < 0 or current_selected_column > 7 or final_selected_row < 0 or final_selected_row > 7 or final_selected_column < 0 or final_selected_column > 7:
        print(f'White player, you have wasted your move, because you entered an invalid position on the chess board.') if current_player_index % 2 == 0 else print(f'Black player, you have wasted your move, because you entered an invalid position on the chess board.')
        return "Invalid position"

    current_selected_figure = chess_board[current_selected_row][current_selected_column]

    if current_selected_figure not in chess_figures_dictionary.keys():
        print(f'White player, you have selected an empty position and you have wasted your move.') if current_player_index % 2 == 0 else print(f'Black player, you have selected an empty position and you have wasted your move.')
        return "Invalid position"

    if (current_selected_figure not in white_figures) if current_player_index % 2 == 0 else (current_selected_figure not in black_figures):
        print(f'White player, you cannot move your opponent\'s figures. You have wasted your move.') if current_player_index % 2 == 0 else print(f'Black player, you cannot move your opponent\'s figures. You have wasted your move.')
        return "Invalid position"


current_player_index = -1

while True:
    current_player_index += 1
    current_position = input("White player, enter the position that you want to move: (E2)") if current_player_index % 2 == 0 else input("Black player, enter the position that you want to move: (E2)")
    final_position = input("White player, enter the final position that you wish to make: (E7)") if current_player_index % 2 == 0 else input("Black player, enter the final position that you wish to make: (E4)")

    current_selected_row = chess_rows_dictionary[int(current_position[1])]
    current_selected_column = chess_columns_dictionary[current_position[0]]
    final_selected_row = chess_rows_dictionary[int(final_position[1])]
    final_selected_column = chess_columns_dictionary[final_position[0]]

    validate_result = validate_positions(current_selected_row, current_selected_column, final_selected_row, final_selected_column)
    if validate_result == False:
        continue

    current_selected_figure = chess_board[current_selected_row][current_selected_column]
    result = chess_figures_dictionary[current_selected_figure](current_selected_row, current_selected_column, final_selected_row, final_selected_column)

    if result is None or result == "You took an opponent\'s figure!":
        for row in chess_board:
            print(" ".join(row))
        if result == "You took an opponent\'s figure!":
            print(result)
    else:
        print(result)


