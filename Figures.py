from chess_project import *


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
