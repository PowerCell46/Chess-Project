invalid_position_message = "The position that you wish to go to is invalid. Make your move again."


def white_pawn(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["White Pawn"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    if current_column == final_column:  # Moving forward
        if current_row == 1:
            new_selected_figure = input("Your Pawn has reached the End of the Board! Choose what you want to transorm it to: [White Pawn, White Rook, White Knight, White Bishop, White Queen] ")
            chess_board[1][final_column] = names_to_chess_figures_dictionary["Blank Space"]
            try:
                chess_board[0][final_column] = names_to_chess_figures_dictionary[new_selected_figure]
            except KeyError:
                chess_board[0][final_column] = names_to_chess_figures_dictionary["White Queen"]
                return f'You entered an invalid figure, so the program chose a White Queen.'

        elif current_row == 6:  # This is the pawn's first move
            if current_row - 1 == final_row:
                new_position_figure = chess_board[final_row][final_column]  # checking what is on the new position
                if new_position_figure != names_to_chess_figures_dictionary["Blank Space"]:
                    return invalid_position_message
                chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
                chess_board[final_row][current_column] = names_to_chess_figures_dictionary["White Pawn"]
                return successful_moving

            elif current_row - 2 == final_row:
                new_position_figure = chess_board[current_row - 1][final_column]  # checking what is on the new first position
                if new_position_figure != names_to_chess_figures_dictionary["Blank Space"]:
                    return invalid_position_message

                new_position_figure = chess_board[final_row][final_column]  # checking what is on the new second position
                if new_position_figure != names_to_chess_figures_dictionary["Blank Space"]:
                    return invalid_position_message
                chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
                chess_board[final_row][current_column] = names_to_chess_figures_dictionary["White Pawn"]
                return successful_moving

            else:
                return invalid_position_message

        else:  # This is not the pawn's first move
            if current_row - 1 == final_row:
                new_position_figure = chess_board[final_row][final_column]  # checking what is on the new position
                if new_position_figure != names_to_chess_figures_dictionary["Blank Space"]:
                    return invalid_position_message
                chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
                chess_board[final_row][current_column] = names_to_chess_figures_dictionary["White Pawn"]
                return successful_moving

            else:
                return invalid_position_message

    else:  # Taking another figure
        if current_row - 1 != final_row:  # Checking if the final row is invalid
            return invalid_position_message

        if current_column - 1 == final_column or current_column + 1 == final_column:
            new_position_figure = chess_board[final_row][final_column]
            if new_position_figure not in black_figures:
                return invalid_position_message

            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Pawn"]

            return f'{names_to_chess_figures_dictionary["White Pawn"]} successfully took {new_position_figure}!'

        else:
            return invalid_position_message


def black_pawn(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["Black Pawn"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    if current_column == final_column:  # Moving forward
        if current_row == 6:
            new_selected_figure = input("Your Pawn has reached the End of the Board! Choose what you want to transorm it to: [Black Pawn, Black Rook, Black Knight, Black Bishop, Black Queen] ")
            chess_board[6][final_column] = names_to_chess_figures_dictionary["Blank Space"]
            try:
                chess_board[7][final_column] = names_to_chess_figures_dictionary[new_selected_figure]
            except KeyError:
                chess_board[7][final_column] = names_to_chess_figures_dictionary["Black Queen"]
                return f'You entered an invalid figure, so the program chose a Black Queen.'

        elif current_row == 1:  # This is the pawn's first move
            if current_row + 1 == final_row:
                new_position_figure = chess_board[final_row][final_column]  # checking what is on the new position
                if new_position_figure != names_to_chess_figures_dictionary["Blank Space"]:
                    return invalid_position_message
                chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
                chess_board[final_row][current_column] = names_to_chess_figures_dictionary["Black Pawn"]
                return successful_moving

            elif current_row + 2 == final_row:
                new_position_figure = chess_board[current_row + 1][final_column]  # checking what is on the new first position
                if new_position_figure != names_to_chess_figures_dictionary["Blank Space"]:
                    return invalid_position_message

                new_position_figure = chess_board[final_row][final_column]  # checking what is on the new second position
                if new_position_figure != names_to_chess_figures_dictionary["Blank Space"]:
                    return invalid_position_message
                chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
                chess_board[final_row][current_column] = names_to_chess_figures_dictionary["Black Pawn"]
                return successful_moving

            else:
                return invalid_position_message

        else:  # This is not the pawn's first move
            if current_row + 1 == final_row:
                new_position_figure = chess_board[final_row][final_column]  # checking what is on the new position
                if new_position_figure != names_to_chess_figures_dictionary["Blank Space"]:
                    return invalid_position_message
                chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
                chess_board[final_row][current_column] = names_to_chess_figures_dictionary["Black Pawn"]
                return successful_moving

            else:
                return invalid_position_message

    else:  # Taking another figure
        if current_row + 1 != final_row:  # Checking if the final row is invalid
            return invalid_position_message

        if current_column - 1 == final_column or current_column + 1 == final_column:
            new_position_figure = chess_board[final_row][final_column]
            if new_position_figure not in white_figures:
                return invalid_position_message

            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Pawn"]

            return f'{names_to_chess_figures_dictionary["Black Pawn"]} successfully took {new_position_figure}!'

        else:
            return invalid_position_message


def white_rook(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["White Rook"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    if final_row < current_row:
        if current_column != final_column:
            return invalid_position_message

        current_working_row = current_row - 1
        while current_working_row > final_row:
            current_selected_figure = chess_board[current_working_row][current_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_row -= 1
        current_selected_figure = chess_board[final_row][current_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Rook"]
            return f'{names_to_chess_figures_dictionary["White Rook"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Rook"]
            return successful_moving

    elif final_row > current_row:
        if current_column != final_column:
            return invalid_position_message

        current_working_row = current_row + 1
        while current_working_row < final_row:
            current_selected_figure = chess_board[current_working_row][current_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_row += 1
        current_selected_figure = chess_board[final_row][current_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Rook"]
            return f'{names_to_chess_figures_dictionary["White Rook"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Rook"]
            return successful_moving

    elif final_column < current_column:
        if current_row != final_row:
            return invalid_position_message

        current_working_column = current_column - 1
        while current_working_column > final_column:
            current_selected_figure = chess_board[current_row][current_working_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_column -= 1
        current_selected_figure = chess_board[current_row][current_working_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Rook"]
            return f'{names_to_chess_figures_dictionary["White Rook"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Rook"]
            return successful_moving

    elif final_column > current_column:
        if current_row != final_row:
            return invalid_position_message

        current_working_column = current_column + 1
        while current_working_column < final_column:
            current_selected_figure = chess_board[current_row][current_working_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_column += 1
        current_selected_figure = chess_board[current_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Rook"]
            return f'{names_to_chess_figures_dictionary["White Rook"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Rook"]
            return successful_moving

    else:
        return "You have entered an invalid row and you have wasted your move"


def black_rook(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["Black Rook"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    if final_row < current_row:
        if current_column != final_column:
            return invalid_position_message

        current_working_row = current_row - 1
        while current_working_row > final_row:
            current_selected_figure = chess_board[current_working_row][current_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_row -= 1
        current_selected_figure = chess_board[final_row][current_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Rook"]
            return f'{names_to_chess_figures_dictionary["Black Rook"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Rook"]
            return successful_moving

    elif final_row > current_row:
        if current_column != final_column:
            return invalid_position_message

        current_working_row = current_row + 1
        while current_working_row < final_row:
            current_selected_figure = chess_board[current_working_row][current_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_row += 1
        current_selected_figure = chess_board[final_row][current_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Rook"]
            return f'{names_to_chess_figures_dictionary["Black Rook"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Rook"]
            return successful_moving

    elif final_column < current_column:
        if current_row != final_row:
            return invalid_position_message

        current_working_column = current_column - 1
        while current_working_column > final_column:
            current_selected_figure = chess_board[current_row][current_working_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_column -= 1
        current_selected_figure = chess_board[current_row][current_working_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Rook"]
            return f'{names_to_chess_figures_dictionary["Black Rook"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Rook"]
            return successful_moving

    elif final_column > current_column:
        if current_row != final_row:
            return invalid_position_message

        current_working_column = current_column + 1
        while current_working_column < final_column:
            current_selected_figure = chess_board[current_row][current_working_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_column += 1
        current_selected_figure = chess_board[current_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Rook"]
            return f'{names_to_chess_figures_dictionary["Black Rook"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Rook"]
            return successful_moving

    else:
        return "You have entered an invalid row and you have wasted your move"


def white_knight(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["White Knight"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    if current_column - 2 == final_column and current_row - 1 == final_row:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return f'{names_to_chess_figures_dictionary["White Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return successful_moving

    elif current_column - 2 == final_column and current_row + 1 == final_row:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return f'{names_to_chess_figures_dictionary["White Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return successful_moving

    elif current_column + 2 == final_column and current_row - 1 == final_row:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return f'{names_to_chess_figures_dictionary["White Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return successful_moving

    elif current_column + 2 == final_column and current_row + 1 == final_row:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return f'{names_to_chess_figures_dictionary["White Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return successful_moving

    elif current_row - 2 == final_row and current_column - 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return f'{names_to_chess_figures_dictionary["White Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return successful_moving

    elif current_row - 2 == final_row and current_column + 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return f'{names_to_chess_figures_dictionary["White Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return successful_moving

    elif current_row + 2 == final_row and current_column - 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return f'{names_to_chess_figures_dictionary["White Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return successful_moving

    elif current_row + 2 == final_row and current_column + 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return f'{names_to_chess_figures_dictionary["White Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Knight"]
            return successful_moving

    else:
        return invalid_position_message


def black_knight(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["Black Knight"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    if current_column - 2 == final_column and current_row - 1 == final_row:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return f'{names_to_chess_figures_dictionary["Black Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return successful_moving

    elif current_column - 2 == final_column and current_row + 1 == final_row:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return f'{names_to_chess_figures_dictionary["Black Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return successful_moving

    elif current_column + 2 == final_column and current_row - 1 == final_row:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return f'{names_to_chess_figures_dictionary["Black Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return successful_moving

    elif current_column + 2 == final_column and current_row + 1 == final_row:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return f'{names_to_chess_figures_dictionary["Black Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return successful_moving

    elif current_row - 2 == final_row and current_column - 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return f'{names_to_chess_figures_dictionary["Black Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return successful_moving

    elif current_row - 2 == final_row and current_column + 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return f'{names_to_chess_figures_dictionary["Black Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return successful_moving

    elif current_row + 2 == final_row and current_column - 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return f'{names_to_chess_figures_dictionary["Black Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return successful_moving

    elif current_row + 2 == final_row and current_column + 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return f'{names_to_chess_figures_dictionary["Black Knight"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Knight"]
            return successful_moving

    else:
        return invalid_position_message


def white_bishop(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["White Bishop"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    if final_row < current_row and final_column < current_column:
        current_working_row = current_row - 1
        current_working_column = current_column - 1
        while current_working_row > final_row and current_working_column > final_column and current_working_row > -1 and current_working_column > -1:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row -= 1
            current_working_column -= 1
        if current_working_row == -1 or current_working_column == -1:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Bishop"]
            return f'{names_to_chess_figures_dictionary["White Bishop"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Bishop"]
            return successful_moving

    elif final_row > current_row and final_column > current_column:
        current_working_row = current_row + 1
        current_working_column = current_column + 1
        while current_working_row < final_row and current_working_column < final_column and current_working_row < 8 and current_working_column < 8:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row += 1
            current_working_column += 1
        if current_working_row == 8 or current_working_column == 8:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Bishop"]
            return f'{names_to_chess_figures_dictionary["White Bishop"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Bishop"]
            return successful_moving

    elif final_row < current_row and final_column > current_column:
        current_working_row = current_row - 1
        current_working_column = current_column + 1
        while current_working_row > final_row and current_working_column < final_column and current_working_row > -1 and current_working_column < 8:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row -= 1
            current_working_column += 1
        if current_working_row == -1 or current_working_column == 8:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Bishop"]
            return f'{names_to_chess_figures_dictionary["White Bishop"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Bishop"]
            return successful_moving

    elif final_row > current_row and final_column < current_column:
        current_working_row = current_row + 1
        current_working_column = current_column - 1
        while current_working_row < final_row and current_working_column > final_column and current_working_row < 8 and current_working_column > -1:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row += 1
            current_working_column -= 1
        if current_working_row == 8 or current_working_column == -1:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Bishop"]
            return f'{names_to_chess_figures_dictionary["White Bishop"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Bishop"]
            return successful_moving
    else:
        return "You have entered an invalid position for the knight and you have wasted your move"


def black_bishop(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["Black Bishop"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    if final_row < current_row and final_column < current_column:
        current_working_row = current_row - 1
        current_working_column = current_column - 1
        while current_working_row > final_row and current_working_column > final_column and current_working_row > -1 and current_working_column > -1:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row -= 1
            current_working_column -= 1
        if current_working_row == -1 or current_working_column == -1:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Bishop"]
            return f'{names_to_chess_figures_dictionary["Black Bishop"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Bishop"]
            return successful_moving

    elif final_row > current_row and final_column > current_column:
        current_working_row = current_row + 1
        current_working_column = current_column + 1
        while current_working_row < final_row and current_working_column < final_column and current_working_row < 8 and current_working_column < 8:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row += 1
            current_working_column += 1
        if current_working_row == 8 or current_working_column == 8:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Bishop"]
            return f'{names_to_chess_figures_dictionary["Black Bishop"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Bishop"]
            return successful_moving

    elif final_row < current_row and final_column > current_column:
        current_working_row = current_row - 1
        current_working_column = current_column + 1
        while current_working_row > final_row and current_working_column < final_column and current_working_row > -1 and current_working_column < 8:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row -= 1
            current_working_column += 1
        if current_working_row == -1 or current_working_column == 8:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Bishop"]
            return f'{names_to_chess_figures_dictionary["Black Bishop"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Bishop"]
            return successful_moving

    elif final_row > current_row and final_column < current_column:
        current_working_row = current_row + 1
        current_working_column = current_column - 1
        while current_working_row < final_row and current_working_column > final_column and current_working_row < 8 and current_working_column > -1:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row += 1
            current_working_column -= 1
        if current_working_row == 8 or current_working_column == -1:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Bishop"]
            return f'{names_to_chess_figures_dictionary["Black Bishop"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Bishop"]
            return successful_moving
    else:
        return "You have entered an invalid position for the knight and you have wasted your move"


def white_queen(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["White Queen"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    # Rook's logic
    if final_row < current_row and current_column == final_column:
        current_working_row = current_row - 1
        while current_working_row > final_row:
            current_selected_figure = chess_board[current_working_row][current_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_row -= 1
        current_selected_figure = chess_board[final_row][current_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return f'{names_to_chess_figures_dictionary["White Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return successful_moving

    elif final_row > current_row and current_column == final_column:
        current_working_row = current_row + 1
        while current_working_row < final_row:
            current_selected_figure = chess_board[current_working_row][current_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_row += 1
        current_selected_figure = chess_board[final_row][current_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return f'{names_to_chess_figures_dictionary["White Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return successful_moving

    elif final_column < current_column and current_row == final_row:
        current_working_column = current_column - 1
        while current_working_column > final_column:
            current_selected_figure = chess_board[current_row][current_working_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_column -= 1
        current_selected_figure = chess_board[current_row][current_working_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return f'{names_to_chess_figures_dictionary["White Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return successful_moving

    elif final_column > current_column and current_row == final_row:
        current_working_column = current_column + 1
        while current_working_column < final_column:
            current_selected_figure = chess_board[current_row][current_working_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_column += 1
        current_selected_figure = chess_board[current_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return f'{names_to_chess_figures_dictionary["White Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return successful_moving

    # Bishop's logic
    elif final_row < current_row and final_column < current_column:
        current_working_row = current_row - 1
        current_working_column = current_column - 1
        while current_working_row > final_row and current_working_column > final_column and current_working_row > -1 and current_working_column > -1:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row -= 1
            current_working_column -= 1
        if current_working_row == -1 or current_working_column == -1:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return f'{names_to_chess_figures_dictionary["White Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return successful_moving

    elif final_row > current_row and final_column > current_column:
        current_working_row = current_row + 1
        current_working_column = current_column + 1
        while current_working_row < final_row and current_working_column < final_column and current_working_row < 8 and current_working_column < 8:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row += 1
            current_working_column += 1
        if current_working_row == 8 or current_working_column == 8:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return f'{names_to_chess_figures_dictionary["White Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return successful_moving

    elif final_row < current_row and final_column > current_column:
        current_working_row = current_row - 1
        current_working_column = current_column + 1
        while current_working_row > final_row and current_working_column < final_column and current_working_row > -1 and current_working_column < 8:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row -= 1
            current_working_column += 1
        if current_working_row == -1 or current_working_column == 8:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return f'{names_to_chess_figures_dictionary["White Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return successful_moving

    elif final_row > current_row and final_column < current_column:
        current_working_row = current_row + 1
        current_working_column = current_column - 1
        while current_working_row < final_row and current_working_column > final_column and current_working_row < 8 and current_working_column > -1:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row += 1
            current_working_column -= 1
        if current_working_row == 8 or current_working_column == -1:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return f'{names_to_chess_figures_dictionary["White Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White Queen"]
            return successful_moving
    else:
        return invalid_position_message


def black_queen(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["Black Queen"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    # Rook's logic
    if final_row < current_row and current_column == final_column:
        current_working_row = current_row - 1
        while current_working_row > final_row:
            current_selected_figure = chess_board[current_working_row][current_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_row -= 1
        current_selected_figure = chess_board[final_row][current_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return f'{names_to_chess_figures_dictionary["Black Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return successful_moving

    elif final_row > current_row and current_column == final_column:
        current_working_row = current_row + 1
        while current_working_row < final_row:
            current_selected_figure = chess_board[current_working_row][current_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_row += 1
        current_selected_figure = chess_board[final_row][current_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return f'{names_to_chess_figures_dictionary["Black Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return successful_moving

    elif final_column < current_column and current_row == final_row:
        current_working_column = current_column - 1
        while current_working_column > final_column:
            current_selected_figure = chess_board[current_row][current_working_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_column -= 1
        current_selected_figure = chess_board[current_row][current_working_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return f'{names_to_chess_figures_dictionary["Black Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return successful_moving

    elif final_column > current_column and current_row == final_row:
        current_working_column = current_column + 1
        while current_working_column < final_column:
            current_selected_figure = chess_board[current_row][current_working_column]
            if current_selected_figure in white_figures or current_selected_figure in black_figures:
                return invalid_position_message
            current_working_column += 1
        current_selected_figure = chess_board[current_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return f'{names_to_chess_figures_dictionary["Black Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return successful_moving

    # Bishop's logic
    elif final_row < current_row and final_column < current_column:
        current_working_row = current_row - 1
        current_working_column = current_column - 1
        while current_working_row > final_row and current_working_column > final_column and current_working_row > -1 and current_working_column > -1:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row -= 1
            current_working_column -= 1
        if current_working_row == -1 or current_working_column == -1:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return f'{names_to_chess_figures_dictionary["Black Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return successful_moving

    elif final_row > current_row and final_column > current_column:
        current_working_row = current_row + 1
        current_working_column = current_column + 1
        while current_working_row < final_row and current_working_column < final_column and current_working_row < 8 and current_working_column < 8:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row += 1
            current_working_column += 1
        if current_working_row == 8 or current_working_column == 8:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return f'{names_to_chess_figures_dictionary["Black Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return successful_moving

    elif final_row < current_row and final_column > current_column:
        current_working_row = current_row - 1
        current_working_column = current_column + 1
        while current_working_row > final_row and current_working_column < final_column and current_working_row > -1 and current_working_column < 8:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row -= 1
            current_working_column += 1
        if current_working_row == -1 or current_working_column == 8:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return f'{names_to_chess_figures_dictionary["Black Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return successful_moving

    elif final_row > current_row and final_column < current_column:
        current_working_row = current_row + 1
        current_working_column = current_column - 1
        while current_working_row < final_row and current_working_column > final_column and current_working_row < 8 and current_working_column > -1:
            current_selected_figure = chess_board[current_working_row][current_working_column]
            if current_selected_figure in black_figures or current_selected_figure in white_figures:
                return invalid_position_message
            current_working_row += 1
            current_working_column -= 1
        if current_working_row == 8 or current_working_column == -1:
            return invalid_position_message
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return f'{names_to_chess_figures_dictionary["Black Queen"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black Queen"]
            return successful_moving
    else:
        return invalid_position_message


def white_king(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["White King"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    if (current_row == 7 and final_row == 7 and current_column == 4 and final_column == 7) or (current_row == 7 and final_row == 7 and current_column == 4 and final_column == 0):
        if chess_board[7][5] == names_to_chess_figures_dictionary["Blank Space"] and chess_board[7][6] == names_to_chess_figures_dictionary["Blank Space"] and chess_board[7][7] == names_to_chess_figures_dictionary["White Rook"] and final_column == 7:
            chess_board[7][4] = names_to_chess_figures_dictionary["White Rook"]
            chess_board[7][7] = names_to_chess_figures_dictionary["White King"]
            return f'You successfully made a Rocade!'
        elif chess_board[7][3] == names_to_chess_figures_dictionary["Blank Space"] and chess_board[7][2] == names_to_chess_figures_dictionary["Blank Space"] and chess_board[7][1] == names_to_chess_figures_dictionary["Blank Space"] and chess_board[7][0] == names_to_chess_figures_dictionary["White Rook"] and final_column == 0:
            chess_board[7][4] = names_to_chess_figures_dictionary["White Rook"]
            chess_board[7][0] = names_to_chess_figures_dictionary["White King"]
            return f'You successfully made a Rocade!'
        else:
            return invalid_position_message

    # Upper row
    if current_row + 1 == final_row and current_column == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return f'{names_to_chess_figures_dictionary["White King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return successful_moving

    elif current_row + 1 == final_row and current_column - 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return f'{names_to_chess_figures_dictionary["White King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return successful_moving

    elif current_row + 1 == final_row and current_column + 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return f'{names_to_chess_figures_dictionary["White King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return successful_moving

    # Same row
    elif current_row == final_row and current_column - 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return f'{names_to_chess_figures_dictionary["White King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return successful_moving

    elif current_row == final_row and current_column + 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return f'{names_to_chess_figures_dictionary["White King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return successful_moving

    # Lower row
    elif current_row - 1 == final_row and current_column == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return f'{names_to_chess_figures_dictionary["White King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return successful_moving

    elif current_row - 1 == final_row and current_column - 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return f'{names_to_chess_figures_dictionary["White King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return successful_moving

    elif current_row - 1 == final_row and current_column + 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in white_figures:
            return invalid_position_message
        elif current_selected_figure in black_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return f'{names_to_chess_figures_dictionary["White King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["White King"]
            return successful_moving

    else:
        return invalid_position_message


def black_king(current_row, current_column, final_row, final_column):
    successful_moving = f'{names_to_chess_figures_dictionary["Black King"]} successfully moved from {chess_columns_dictionary_reversed_values[current_column]}{chess_rows_dictionary_reversed_values[current_row]} to {chess_columns_dictionary_reversed_values[final_column]}{chess_rows_dictionary_reversed_values[final_row]}!'

    if (current_row == 0 and final_row == 0 and current_column == 4 and final_column == 7) or (current_row == 0 and final_row == 0 and current_column == 4 and final_column == 0):
        if chess_board[0][5] == names_to_chess_figures_dictionary["Blank Space"] and chess_board[0][6] == names_to_chess_figures_dictionary["Blank Space"] and chess_board[0][7] == names_to_chess_figures_dictionary["Black Rook"] and final_column == 7:
            chess_board[0][4] = names_to_chess_figures_dictionary["Black Rook"]
            chess_board[0][7] = names_to_chess_figures_dictionary["Black King"]
            return f'You successfully made a Rocade!'
        elif chess_board[0][3] == names_to_chess_figures_dictionary["Blank Space"] and chess_board[0][2] == names_to_chess_figures_dictionary["Blank Space"] and chess_board[0][1] == names_to_chess_figures_dictionary["Blank Space"] and chess_board[0][0] == names_to_chess_figures_dictionary["Black Rook"] and final_column == 0:
            chess_board[0][4] = names_to_chess_figures_dictionary["Black Rook"]
            chess_board[0][0] = names_to_chess_figures_dictionary["Black King"]
            return f'You successfully made a Rocade!'
        else:
            return invalid_position_message

    # Upper row
    if current_row + 1 == final_row and current_column == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return f'{names_to_chess_figures_dictionary["Black King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return successful_moving

    elif current_row + 1 == final_row and current_column - 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return f'{names_to_chess_figures_dictionary["Black King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return successful_moving

    elif current_row + 1 == final_row and current_column + 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return f'{names_to_chess_figures_dictionary["Black King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return successful_moving

    # Same row
    elif current_row == final_row and current_column - 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return f'{names_to_chess_figures_dictionary["Black King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return successful_moving

    elif current_row == final_row and current_column + 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return f'{names_to_chess_figures_dictionary["Black King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return successful_moving

    # Lower row
    elif current_row - 1 == final_row and current_column == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return f'{names_to_chess_figures_dictionary["Black King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return successful_moving

    elif current_row - 1 == final_row and current_column - 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return f'{names_to_chess_figures_dictionary["Black King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return successful_moving

    elif current_row - 1 == final_row and current_column + 1 == final_column:
        current_selected_figure = chess_board[final_row][final_column]
        if current_selected_figure in black_figures:
            return invalid_position_message
        elif current_selected_figure in white_figures:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return f'{names_to_chess_figures_dictionary["Black King"]} successfully took {current_selected_figure}!'
        else:
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Blank Space"]
            chess_board[final_row][final_column] = names_to_chess_figures_dictionary["Black King"]
            return successful_moving

    else:
        return invalid_position_message


chess_figures_dictionary = {
    "♙": white_pawn,
    "♘": white_knight,
    "♗": white_bishop,
    "♖": white_rook,
    "♕": white_queen,
    "♔": white_king,

    "♟︎": black_pawn,
    "♞": black_knight,
    "♝": black_bishop,
    "♜": black_rook,
    "♛": black_queen,
    "♚": black_king
}

white_figures = ["♙", "♘", "♗", "♖", "♕", "♔"]
black_figures = ["♟︎", "♞", "♝", "♜", "♛", "♚"]
chess_rows_dictionary = {8: 0, 7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}
chess_rows_dictionary_reversed_values = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
chess_columns_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
chess_columns_dictionary_reversed_values = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
chess_figures_to_names_dictionary = {
    "♙": "White Pawn",
    "♘": "White Knight",
    "♗": "White Bishop",
    "♖": "White Rook",
    "♕": "White Queen",
    "♔": "White King",
    "♟︎": "Black Pawn",
    "♞": "Black Knight",
    "♝": "Black Bishop",
    "♜": "Black Rook",
    "♛": "Black Queen",
    "♚": "Black King",
    "⬜ ": "Blank Space"
}
names_to_chess_figures_dictionary = {
    "White Pawn": "♙",
    "White Knight": "♘",
    "White Bishop": "♗",
    "White Rook": "♖",
    "White Queen": "♕",
    "White King": "♔",
    "Black Pawn": "♟︎",
    "Black Knight": "♞",
    "Black Bishop": "♝",
    "Black Rook": "♜",
    "Black Queen": "♛",
    "Black King": "♚",
    "Blank Space": "⬜ "
}

chess_board = [[names_to_chess_figures_dictionary["Blank Space"] for pos in range(8)] for row in range(8)]


def initializing_black_figures():
    for pos in range(8):
        chess_board[1][pos] = names_to_chess_figures_dictionary["Black Pawn"]

    chess_board[0][0] = names_to_chess_figures_dictionary["Black Rook"]
    chess_board[0][7] = names_to_chess_figures_dictionary["Black Rook"]

    chess_board[0][1] = names_to_chess_figures_dictionary["Black Knight"]
    chess_board[0][6] = names_to_chess_figures_dictionary["Black Knight"]

    chess_board[0][2] = names_to_chess_figures_dictionary["Black Bishop"]
    chess_board[0][5] = names_to_chess_figures_dictionary["Black Bishop"]

    chess_board[0][3] = names_to_chess_figures_dictionary["Black Queen"]
    chess_board[0][4] = names_to_chess_figures_dictionary["Black King"]


def initializing_white_figures():
    for position in range(8):
        chess_board[6][position] = names_to_chess_figures_dictionary["White Pawn"]

    chess_board[7][0] = names_to_chess_figures_dictionary["White Rook"]
    chess_board[7][7] = names_to_chess_figures_dictionary["White Rook"]

    chess_board[7][1] = names_to_chess_figures_dictionary["White Knight"]
    chess_board[7][6] = names_to_chess_figures_dictionary["White Knight"]

    chess_board[7][2] = names_to_chess_figures_dictionary["White Bishop"]
    chess_board[7][5] = names_to_chess_figures_dictionary["White Bishop"]

    chess_board[7][3] = names_to_chess_figures_dictionary["White Queen"]
    chess_board[7][4] = names_to_chess_figures_dictionary["White King"]


initializing_white_figures()
initializing_black_figures()

# FIX IT
def print_chess_board():
    print("  " + "  ".join(chess_columns_dictionary.keys()))
    for index in range(len(chess_board)):
        row = chess_board[index]
        if row == 0 or row == 1 or row == 6 or row == 7:
            print(f'{chess_rows_dictionary_reversed_values[index]} ' + "  ".join(row) + f' {chess_rows_dictionary_reversed_values[index]}')
        else:
            print(f'{chess_rows_dictionary_reversed_values[index]} ' + " ".join(row) + f' {chess_rows_dictionary_reversed_values[index]}')
    print("  " + "  ".join(chess_columns_dictionary.keys()))


print_chess_board()


def validate_positions(current_selected_row, current_selected_column, final_selected_row, final_selected_column):
    if current_selected_row < 0 or current_selected_row > 7 or current_selected_column < 0 or current_selected_column > 7 or final_selected_row < 0 or final_selected_row > 7 or final_selected_column < 0 or final_selected_column > 7:
        print(f'White player, you have entered an invalid position on the chess board. Try again.') if current_player_index % 2 == 0 else print(f'Black player, you have entered an invalid position on the chess board. Try again.')
        return False

    current_selected_figure = chess_board[current_selected_row][current_selected_column]

    if current_selected_figure not in chess_figures_dictionary.keys():
        print(f'White player, you have selected an empty position. Try again.') if current_player_index % 2 == 0 else print(f'Black player, you have selected an empty position. Try again.')
        return False

    if (current_selected_figure not in white_figures) if current_player_index % 2 == 0 else (current_selected_figure not in black_figures):
        print(f'White player, you cannot move your opponent\'s figures. Try again.') if current_player_index % 2 == 0 else print(f'Black player, you cannot move your opponent\'s figures. Try again.')
        return False


def clear_history_file():
    history_file = open("current_chess_game_history.txt", "w")
    history_file.truncate(0)
    history_file.close()
    moves_file = open("current_chess_game_moves.txt", "w")
    moves_file.truncate(0)
    moves_file.close()


clear_history_file()

current_player_index = -1

while True:
    current_player_index += 1
    current_position = input("White player, enter the position that you want to move: (E2) ") if current_player_index % 2 == 0 else input("Black player, enter the position that you want to move: (E7) ")
    final_position = input("White player, enter the final position that you wish to make: (E4) ") if current_player_index % 2 == 0 else input("Black player, enter the final position that you wish to make: (E5) ")

    try:
        current_selected_row = chess_rows_dictionary[int(current_position[1])]
        current_selected_column = chess_columns_dictionary[current_position[0]]
        final_selected_row = chess_rows_dictionary[int(final_position[1])]
        final_selected_column = chess_columns_dictionary[final_position[0]]
    except (KeyError, ValueError):
        print(f'White player, you have selected an invalid position. Try again.') if current_player_index % 2 == 0 else print(f'Black player, you have selected an invalid position. Try again.')
        current_player_index -= 1
        continue
    validate_result = validate_positions(current_selected_row, current_selected_column, final_selected_row, final_selected_column)

    if validate_result == False:
        current_player_index -= 1
        continue

    current_selected_figure = chess_board[current_selected_row][current_selected_column]
    result = chess_figures_dictionary[current_selected_figure](current_selected_row, current_selected_column, final_selected_row, final_selected_column)

    if result == invalid_position_message:
        print(result)
        current_player_index -= 1
        continue

    print_chess_board()
    print(result)

    def writing_current_data():
        moves_file = open("current_chess_game_moves.txt", "a")
        moves_file.write(f'{current_selected_row}, {current_selected_column}, {final_selected_row}, {final_selected_column}\n')
        moves_file.close()

        history_file = open("current_chess_game_history.txt", "a", encoding="utf-8")
        history_file.write(f'{result}\n')
        history_file.close()

    writing_current_data()

    # FIX IT
    if names_to_chess_figures_dictionary["Black King"] == result[-2] or names_to_chess_figures_dictionary["White King"] == result[-2]:
        print(f'GAME OVER!')
        break

