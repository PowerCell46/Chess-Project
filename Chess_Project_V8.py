from colorama import Fore
from pyfiglet import Figlet
import time
import tkinter as tk

f = Figlet(font="big", justify='center')

print(Fore.LIGHTCYAN_EX + f.renderText("Welcome to PowerCell's Chess Game!"))
time.sleep(1.5)

if input("Are you familiar with the game? Y/N ").upper() != "Y":
    chess_data_list = ['Chess is a strategic board game that is played between two players on a square checkered board consisting of 64 squares.',
    'Chess is a game of skill and intellect, where players use their pieces to capture the opponent\'s pieces and ultimately aim to checkmate the opponent\'s king.',
    'Chess is a game that requires careful planning, calculation, and foresight, as players must anticipate their opponent\'s moves and adjust their own strategies accordingly.',
    'Chess is known as the "game of kings" due to its historical association with nobility and its reputation as a game that tests and sharpens one\'s mental abilities.',
    'Chess is a timeless game with a rich history, dating back centuries, and has evolved into a competitive sport with professional players and international tournaments.',
    'Chess is played worldwide and transcends language and cultural barriers, serving as a universal language of strategy and logic.',
    'Chess is a game that offers countless possibilities and challenges, fostering creativity, problem-solving, and critical thinking skills in its players.']
    time.sleep(0.5)
    for row in chess_data_list:
        print(Fore.YELLOW + row)
        time.sleep(5)

    if input(Fore.LIGHTCYAN_EX + "Do you need more explanations before starting? Y/N ").upper() == "Y":
        time.sleep(0.5)
        print(f'For more information, watch this clip: https://www.youtube.com/watch?v=OCSbzArwB10')

time.sleep(1.5)

if input(Fore.LIGHTCYAN_EX + "Do you want to read the specifics of this particular game? Y/N ").upper() == "Y":
    rules_list = ["You can write the commands in Upper or Lower case, whatever you prefer.",
                  "If you enter an invalid position, the Game will inform you and you will have to enter again.",
                  "You can make a Rocade even if you have moved the King or the Rook before, but they MUST be in their right positions!",
                  "After finishing the game you'll have the ability to see every step that each player has made.",
                  "The program ends when one of the Kings is taken out of the board.",
                  # "Printing externally is more eye-appealing, but for some reason the second row of the chessboard is moved. It will be fixed at a later time.",  # Future work
                  "Printing on the console is faster but it's possible to mistake the figures, so be careful if you choose this option.",  # Future work
                  "If you choose to print externally, you have to close the Window and then you can continue the Game!"]

    time.sleep(0.5)
    for row in rules_list:
        print(Fore.YELLOW + row)
        time.sleep(5)

time.sleep(1.5)

print_type = input("How do you want the chess board to be printed? On the console or externally? (console/externally) ").lower()
print_type = print_type if print_type == "console" or print_type == "externally" else "console"

time.sleep(1.5)


def chess_game():
    invalid_position_message = "The position that you wish to go to is invalid. Make your move again."


    def successful_moving(figure, previous_column, previous_row, new_column, new_row):
        return f'{names_to_chess_figures_dictionary[figure]} [{figure}] successfully moved from {chess_columns_dictionary_reversed_values[previous_column]}{chess_rows_dictionary_reversed_values[previous_row]} to {chess_columns_dictionary_reversed_values[new_column]}{chess_rows_dictionary_reversed_values[new_row]}!'


    def successful_taking(current_figure, previous_column, previous_row, taken_figure, new_column, new_row):
        return f'{names_to_chess_figures_dictionary[current_figure]} [{current_figure}] ({chess_columns_dictionary_reversed_values[previous_column]}{chess_rows_dictionary_reversed_values[previous_row]}) successfully took {taken_figure} [{chess_figures_to_names_dictionary[taken_figure]}] ({chess_columns_dictionary_reversed_values[new_column]}{chess_rows_dictionary_reversed_values[new_row]})!'


    def check_message(row, column):
        return f'{names_to_chess_figures_dictionary["Black King"]} [Black King], you are being checked by {chess_board[row][column]} [{chess_figures_to_names_dictionary[chess_board[row][column]]}]!' if chess_board[row][column] in white_figures else f'{names_to_chess_figures_dictionary["White King"]} [White King], you are being checked by {chess_board[row][column]} [{chess_figures_to_names_dictionary[chess_board[row][column]]}]!'


    def successful_moving_operations_function(current_row, current_column, final_row, final_column, chess_figure_name):

        if (current_row % 2 == 0 and current_column % 2 == 0):
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["White Space"]

        elif (current_row % 2 == 0 and current_column % 2 != 0):
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Black Space"]

        elif (current_row % 2 != 0 and current_column % 2 == 0):
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["Black Space"]

        elif (current_row % 2 != 0 and current_column % 2 != 0):
            chess_board[current_row][current_column] = names_to_chess_figures_dictionary["White Space"]

        chess_board[final_row][final_column] = names_to_chess_figures_dictionary[chess_figure_name]


    def white_pawn(current_row, current_column, final_row, final_column):

        def white_pawn_check_next_move(row, column):
            if (chess_board[row - 1][column - 1] == names_to_chess_figures_dictionary["Black King"] and row - 1 > -1 and column - 1 > -1) or (chess_board[row - 1][column + 1] == names_to_chess_figures_dictionary["Black King"] and row - 1 > -1 and column + 1 < 8):
                return check_message(row, column)

        if current_column == final_column:  # Moving forward

            if current_row == 1 and final_row == 0 and chess_board[final_row][final_column] in blank_spaces:  # Reaching the end of the Board
                new_selected_figure = input("Your Pawn has reached the End of the Board! Choose what you want to transform it to: (White Pawn, White Rook, White Knight, White Bishop, White Queen) ")
                try:
                    successful_moving_operations_function(current_row, current_column, final_row, final_column, new_selected_figure)
                except KeyError:
                    successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                    return f'You entered an invalid figure, so the program chose a White Queen.'

            elif current_row == 6:  # This is the pawn's first move
                if current_row - 1 == final_row:
                    new_position_figure = chess_board[final_row][final_column]  # checking what is on the new position
                    if new_position_figure not in blank_spaces:
                        return invalid_position_message
                    successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Pawn")
                    current_check_checker = white_pawn_check_next_move(final_row, final_column)
                    if current_check_checker != None:
                        check_message_list.append(current_check_checker)
                    return successful_moving("White Pawn", current_column, current_row, final_column, final_row)

                elif current_row - 2 == final_row:
                    new_position_figure = chess_board[current_row - 1][final_column]  # checking what is on the new first position
                    if new_position_figure not in blank_spaces:
                        return invalid_position_message

                    new_position_figure = chess_board[final_row][final_column]  # checking what is on the new second position
                    if new_position_figure not in blank_spaces:
                        return invalid_position_message
                    successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Pawn")
                    current_check_checker = white_pawn_check_next_move(final_row, final_column)
                    if current_check_checker != None:
                        check_message_list.append(current_check_checker)
                    return successful_moving("White Pawn", current_column, current_row, final_column, final_row)

                else:
                    return invalid_position_message

            else:  # This is not the pawn's first move
                if current_row - 1 == final_row:
                    new_position_figure = chess_board[final_row][final_column]  # checking what is on the new position
                    if new_position_figure not in blank_spaces:
                        return invalid_position_message
                    successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Pawn")
                    current_check_checker = white_pawn_check_next_move(final_row, final_column)
                    if current_check_checker != None:
                        check_message_list.append(current_check_checker)
                    return successful_moving("White Pawn", current_column, current_row, final_column, final_row)

                else:
                    return invalid_position_message

        else:  # Taking another figure
            if current_row - 1 != final_row:  # Checking if the final row is invalid
                return invalid_position_message

            if current_column - 1 == final_column or current_column + 1 == final_column:
                current_selected_figure = chess_board[final_row][final_column]
                if current_selected_figure not in black_figures:
                    return invalid_position_message
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Pawn")
                current_check_checker = white_pawn_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Pawn", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                return invalid_position_message


    def black_pawn(current_row, current_column, final_row, final_column):

        def black_pawn_check_next_move(row, column):
            if (chess_board[row + 1][column - 1] == names_to_chess_figures_dictionary["White King"] and row + 1 < 8 and column - 1 > -1) or (chess_board[row + 1][column + 1] == names_to_chess_figures_dictionary["White King"] and row + 1 < 8 and column + 1 < 8):
                return check_message(row, column)

        if current_column == final_column:  # Moving forward

            if current_row == 6 and final_row == 7 and chess_board[final_row][final_column] in blank_spaces:  # Reaching the end of the Board
                new_selected_figure = input("Your Pawn has reached the End of the Board! Choose what you want to transform it to: (Black Pawn, Black Rook, Black Knight, Black Bishop, Black Queen) ")
                try:
                    successful_moving_operations_function(current_row, current_column, final_row, final_column, new_selected_figure)
                except KeyError:
                    successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                    return f'You entered an invalid figure, so the program chose a Black Queen.'

            elif current_row == 1:  # This is the pawn's first move
                if current_row + 1 == final_row:
                    new_position_figure = chess_board[final_row][final_column]  # checking what is on the new position
                    if new_position_figure not in blank_spaces:
                        return invalid_position_message
                    successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Pawn")
                    current_check_checker = black_pawn_check_next_move(final_row, final_column)
                    if current_check_checker != None:
                        check_message_list.append(current_check_checker)
                    return successful_moving("Black Pawn", current_column, current_row, final_column, final_row)

                elif current_row + 2 == final_row:
                    new_position_figure = chess_board[current_row + 1][final_column]  # checking what is on the new first position
                    if new_position_figure not in blank_spaces:
                        return invalid_position_message

                    new_position_figure = chess_board[final_row][final_column]  # checking what is on the new second position
                    if new_position_figure not in blank_spaces:
                        return invalid_position_message
                    successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Pawn")
                    current_check_checker = black_pawn_check_next_move(final_row, final_column)
                    if current_check_checker != None:
                        check_message_list.append(current_check_checker)
                    return successful_moving("Black Pawn", current_column, current_row, final_column, final_row)

                else:
                    return invalid_position_message

            else:  # This is not the pawn's first move
                if current_row + 1 == final_row:
                    new_position_figure = chess_board[final_row][final_column]  # checking what is on the new position
                    if new_position_figure not in blank_spaces:
                        return invalid_position_message
                    successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Pawn")
                    current_check_checker = black_pawn_check_next_move(final_row, final_column)
                    if current_check_checker != None:
                        check_message_list.append(current_check_checker)
                    return successful_moving("Black Pawn", current_column, current_row, final_column, final_row)

                else:
                    return invalid_position_message

        else:  # Taking another figure
            if current_row + 1 != final_row:  # Checking if the final row is invalid
                return invalid_position_message

            if current_column - 1 == final_column or current_column + 1 == final_column:
                current_selected_figure = chess_board[final_row][final_column]
                if current_selected_figure not in white_figures:
                    return invalid_position_message
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Pawn")
                current_check_checker = black_pawn_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Pawn", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                return invalid_position_message


    def white_rook(current_row, current_column, final_row, final_column):

        def white_rook_check_next_move(row, column):
            current_working_row = row - 1
            while current_working_row > -1:
                current_selected_figure = chess_board[current_working_row][column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1

            current_working_row = row + 1
            while current_working_row < 8:
                current_selected_figure = chess_board[current_working_row][column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1

            current_working_column = column - 1
            while current_working_column > -1:
                current_selected_figure = chess_board[row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_column -= 1

            current_working_column = column + 1
            while current_working_column < 8:
                current_selected_figure = chess_board[row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_column += 1

        if (current_row == 7 and final_row == 7 and current_column == 0 and final_column == 4) or (current_row == 7 and final_row == 7 and current_column == 7 and final_column == 4):  # Making a Rocade

            if chess_board[7][5] in blank_spaces and chess_board[7][6] in blank_spaces and chess_board[7][4] == names_to_chess_figures_dictionary["White King"] and current_column == 7:
                chess_board[7][4] = names_to_chess_figures_dictionary["White Rook"]
                chess_board[7][7] = names_to_chess_figures_dictionary["White King"]
                return f'You successfully made a Rocade!'

            elif chess_board[7][3] in blank_spaces and chess_board[7][2] in blank_spaces and chess_board[7][1] in blank_spaces and chess_board[7][4] == names_to_chess_figures_dictionary["White King"] and current_column == 0:
                chess_board[7][4] = names_to_chess_figures_dictionary["White Rook"]
                chess_board[7][0] = names_to_chess_figures_dictionary["White King"]
                return f'You successfully made a Rocade!'

            else:
                return invalid_position_message

        elif final_row < current_row:
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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Rook")
                current_check_checker = white_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Rook", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Rook")
                current_check_checker = white_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Rook", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Rook")
                current_check_checker = white_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Rook", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Rook")
                current_check_checker = white_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Rook", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Rook")
                current_check_checker = white_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Rook", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Rook")
                current_check_checker = white_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Rook", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Rook")
                current_check_checker = white_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Rook", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Rook")
                current_check_checker = white_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Rook", current_column, current_row, final_column, final_row)

        else:
            return invalid_position_message


    def black_rook(current_row, current_column, final_row, final_column):

        def black_rook_check_next_move(row, column):
            current_working_row = row - 1
            while current_working_row > -1:
                current_selected_figure = chess_board[current_working_row][column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1

            current_working_row = row + 1
            while current_working_row < 8:
                current_selected_figure = chess_board[current_working_row][column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1

            current_working_column = column - 1
            while current_working_column > -1:
                current_selected_figure = chess_board[row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_column -= 1

            current_working_column = column + 1
            while current_working_column < 8:
                current_selected_figure = chess_board[row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_column += 1

        if (current_row == 0 and final_row == 0 and current_column == 0 and final_column == 4) or (current_row == 0 and final_row == 0 and current_column == 7 and final_column == 4):  # Making a Rocade

            if chess_board[0][5] in blank_spaces and chess_board[0][6] in blank_spaces and chess_board[0][4] == names_to_chess_figures_dictionary["Black King"] and current_column == 7:
                chess_board[0][4] = names_to_chess_figures_dictionary["Black Rook"]
                chess_board[0][7] = names_to_chess_figures_dictionary["Black King"]
                return f'You successfully made a Rocade!'

            elif chess_board[0][3] in blank_spaces and chess_board[0][2] in blank_spaces and chess_board[0][1] in blank_spaces and chess_board[7][4] == names_to_chess_figures_dictionary["Black King"] and current_column == 0:
                chess_board[0][4] = names_to_chess_figures_dictionary["Black Rook"]
                chess_board[0][0] = names_to_chess_figures_dictionary["Black King"]
                return f'You successfully made a Rocade!'

            else:
                return invalid_position_message

        elif final_row < current_row:
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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Rook")
                current_check_checker = black_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Rook", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Rook")
                current_check_checker = black_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Rook", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Rook")
                current_check_checker = black_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Rook", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Rook")
                current_check_checker = black_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Rook", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Rook")
                current_check_checker = black_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Rook", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Rook")
                current_check_checker = black_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Rook", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Rook")
                current_check_checker = black_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Rook", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Rook")
                current_check_checker = black_rook_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Rook", current_column, current_row, final_column, final_row)

        else:
            return invalid_position_message


    def white_knight(current_row, current_column, final_row, final_column):

        def white_knight_check_next_move(row, column):
            if (
                    (chess_board[row - 1][column - 2] == names_to_chess_figures_dictionary["Black King"] and column - 2 > -1 and row - 1 > -1) or
                    (chess_board[row + 1][column - 2] == names_to_chess_figures_dictionary["Black King"] and column - 2 > -1 and row + 1 < 8) or
                    (chess_board[row - 1][column + 2] == names_to_chess_figures_dictionary["Black King"] and column + 2 < 8 and row - 1 > -1) or
                    (chess_board[row + 1][column + 2] == names_to_chess_figures_dictionary["Black King"] and column + 2 < 8 and row + 1 < 8) or
                    (chess_board[row - 2][column + 1] == names_to_chess_figures_dictionary["Black King"] and row - 2 > -1 and column + 1 < 8) or
                    (chess_board[row - 2][column - 1] == names_to_chess_figures_dictionary["Black King"] and row - 2 > -1 and column - 1 > -1) or
                    (chess_board[row + 2][column - 1] == names_to_chess_figures_dictionary["Black King"] and row + 2 < 8 and column - 1 > -1) or
                    (chess_board[row + 2][column + 1] == names_to_chess_figures_dictionary["Black King"] and row + 2 < 8 and column + 1 < 8)):
                return check_message(row, column)

        if (    # All valid Knight positions
                (current_column - 2 == final_column and current_row - 1 == final_row and current_column - 2 > -1 and current_row - 1 > -1) or
                (current_column - 2 == final_column and current_row + 1 == final_row and current_column - 2 > -1 and current_row + 1 < 8) or
                (current_column + 2 == final_column and current_row - 1 == final_row and current_column + 2 < 8 and current_row - 1 > -1) or
                (current_column + 2 == final_column and current_row + 1 == final_row and current_column + 2 < 8 and current_row + 1 < 8) or
                (current_row - 2 == final_row and current_column + 1 == final_column and current_row - 2 > -1 and current_column + 1 < 8) or
                (current_row - 2 == final_row and current_column - 1 == final_column and current_row - 2 > -1 and current_column - 1 > -1) or
                (current_row + 2 == final_row and current_column - 1 == final_column and current_row + 2 < 8 and current_column - 1 > -1) or
                (current_row + 2 == final_row and current_column + 1 == final_column and current_row + 2 < 8 and current_column + 1 < 8)):

            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in white_figures:
                return invalid_position_message

            elif current_selected_figure in black_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Knight")
                current_check_checker = white_knight_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Knight", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Knight")
                current_check_checker = white_knight_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Knight", current_column, current_row, final_column, final_row)

        else:
            return invalid_position_message


    def black_knight(current_row, current_column, final_row, final_column):

        def black_knight_check_next_move(row, column):
            if (
                    (chess_board[row - 1][column - 2] == names_to_chess_figures_dictionary["White King"] and column - 2 > -1 and row - 1 > -1) or
                    (chess_board[row + 1][column - 2] == names_to_chess_figures_dictionary["White King"] and column - 2 > -1 and row + 1 < 8) or
                    (chess_board[row - 1][column + 2] == names_to_chess_figures_dictionary["White King"] and column + 2 < 8 and row - 1 > -1) or
                    (chess_board[row + 1][column + 2] == names_to_chess_figures_dictionary["White King"] and column + 2 < 8 and row + 1 < 8) or
                    (chess_board[row - 2][column + 1] == names_to_chess_figures_dictionary["White King"] and row - 2 > -1 and column + 1 < 8) or
                    (chess_board[row - 2][column - 1] == names_to_chess_figures_dictionary["White King"] and row - 2 > -1 and column - 1 > -1) or
                    (chess_board[row + 2][column - 1] == names_to_chess_figures_dictionary["White King"] and row + 2 < 8 and column - 1 > -1) or
                    (chess_board[row + 2][column + 1] == names_to_chess_figures_dictionary["White King"] and row + 2 < 8 and column + 1 < 8)):
                return check_message(row, column)

        if (    # All valid Knight positions
                (current_column - 2 == final_column and current_row - 1 == final_row and current_column - 2 > -1 and current_row - 1 > -1) or
                (current_column - 2 == final_column and current_row + 1 == final_row and current_column - 2 > -1 and current_row + 1 < 8) or
                (current_column + 2 == final_column and current_row - 1 == final_row and current_column + 2 < 8 and current_row - 1 > -1) or
                (current_column + 2 == final_column and current_row + 1 == final_row and current_column + 2 < 8 and current_row + 1 < 8) or
                (current_row - 2 == final_row and current_column + 1 == final_column and current_row - 2 > -1 and current_column + 1 < 8) or
                (current_row - 2 == final_row and current_column - 1 == final_column and current_row - 2 > -1 and current_column - 1 > -1) or
                (current_row + 2 == final_row and current_column - 1 == final_column and current_row + 2 < 8 and current_column - 1 > -1) or
                (current_row + 2 == final_row and current_column + 1 == final_column and current_row + 2 < 8 and current_column + 1 < 8)):

            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in black_figures:
                return invalid_position_message

            elif current_selected_figure in white_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Knight")
                current_check_checker = black_knight_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Knight", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Knight")
                current_check_checker = black_knight_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Knight", current_column, current_row, final_column, final_row)

        else:
            return invalid_position_message


    def white_bishop(current_row, current_column, final_row, final_column):

        def white_bishop_check_next_move(row, column):
            current_working_row = row - 1
            current_working_column = column - 1
            while current_working_row > -1 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1
                current_working_column -= 1

            current_working_row = row + 1
            current_working_column = column + 1
            while current_working_row < 8 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1
                current_working_column += 1

            current_working_row = row - 1
            current_working_column = column + 1
            while current_working_row > -1 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1
                current_working_column += 1

            current_working_row = row + 1
            current_working_column = column - 1
            while current_working_row < 8 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1
                current_working_column -= 1

        if final_row < current_row and final_column < current_column:
            current_working_row = current_row - 1
            current_working_column = current_column - 1
            while current_working_row > final_row and current_working_column > final_column and current_working_row > -1 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row -= 1
                current_working_column -= 1
            if current_working_row == -1 or current_working_column == -1 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in white_figures:
                return invalid_position_message
            elif current_selected_figure in black_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Bishop")
                current_check_checker = white_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Bishop", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Bishop")
                current_check_checker = white_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Bishop", current_column, current_row, final_column, final_row)

        elif final_row > current_row and final_column > current_column:
            current_working_row = current_row + 1
            current_working_column = current_column + 1
            while current_working_row < final_row and current_working_column < final_column and current_working_row < 8 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row += 1
                current_working_column += 1
            if current_working_row == 8 or current_working_column == 8 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in white_figures:
                return invalid_position_message
            elif current_selected_figure in black_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Bishop")
                current_check_checker = white_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Bishop", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Bishop")
                current_check_checker = white_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Bishop", current_column, current_row, final_column, final_row)

        elif final_row < current_row and final_column > current_column:
            current_working_row = current_row - 1
            current_working_column = current_column + 1
            while current_working_row > final_row and current_working_column < final_column and current_working_row > -1 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row -= 1
                current_working_column += 1
            if current_working_row == -1 or current_working_column == 8 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in white_figures:
                return invalid_position_message
            elif current_selected_figure in black_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Bishop")
                current_check_checker = white_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Bishop", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Bishop")
                current_check_checker = white_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Bishop", current_column, current_row, final_column, final_row)

        elif final_row > current_row and final_column < current_column:
            current_working_row = current_row + 1
            current_working_column = current_column - 1
            while current_working_row < final_row and current_working_column > final_column and current_working_row < 8 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row += 1
                current_working_column -= 1
            if current_working_row == 8 or current_working_column == -1 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in white_figures:
                return invalid_position_message
            elif current_selected_figure in black_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Bishop")
                current_check_checker = white_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Bishop", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Bishop")
                current_check_checker = white_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Bishop", current_column, current_row, final_column, final_row)
        else:
            return invalid_position_message


    def black_bishop(current_row, current_column, final_row, final_column):

        def black_bishop_check_next_move(row, column):
            current_working_row = row - 1
            current_working_column = column - 1
            while current_working_row > -1 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1
                current_working_column -= 1

            current_working_row = row + 1
            current_working_column = column + 1
            while current_working_row < 8 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1
                current_working_column += 1

            current_working_row = row - 1
            current_working_column = column + 1
            while current_working_row > -1 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1
                current_working_column += 1

            current_working_row = row + 1
            current_working_column = column - 1
            while current_working_row < 8 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1
                current_working_column -= 1

        if final_row < current_row and final_column < current_column:
            current_working_row = current_row - 1
            current_working_column = current_column - 1
            while current_working_row > final_row and current_working_column > final_column and current_working_row > -1 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row -= 1
                current_working_column -= 1
            if current_working_row == -1 or current_working_column == -1 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in black_figures:
                return invalid_position_message
            elif current_selected_figure in white_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Bishop")
                current_check_checker = black_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Bishop", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Bishop")
                current_check_checker = black_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Bishop", current_column, current_row, final_column, final_row)

        elif final_row > current_row and final_column > current_column:
            current_working_row = current_row + 1
            current_working_column = current_column + 1
            while current_working_row < final_row and current_working_column < final_column and current_working_row < 8 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row += 1
                current_working_column += 1
            if current_working_row == 8 or current_working_column == 8 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in black_figures:
                return invalid_position_message
            elif current_selected_figure in white_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Bishop")
                current_check_checker = black_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Bishop", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Bishop")
                current_check_checker = black_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Bishop", current_column, current_row, final_column, final_row)

        elif final_row < current_row and final_column > current_column:
            current_working_row = current_row - 1
            current_working_column = current_column + 1
            while current_working_row > final_row and current_working_column < final_column and current_working_row > -1 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row -= 1
                current_working_column += 1
            if current_working_row == -1 or current_working_column == 8 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in black_figures:
                return invalid_position_message
            elif current_selected_figure in white_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Bishop")
                current_check_checker = black_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Bishop", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Bishop")
                current_check_checker = black_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Bishop", current_column, current_row, final_column, final_row)

        elif final_row > current_row and final_column < current_column:
            current_working_row = current_row + 1
            current_working_column = current_column - 1
            while current_working_row < final_row and current_working_column > final_column and current_working_row < 8 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row += 1
                current_working_column -= 1
            if current_working_row == 8 or current_working_column == -1 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in black_figures:
                return invalid_position_message
            elif current_selected_figure in white_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Bishop")
                current_check_checker = black_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Bishop", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Bishop")
                current_check_checker = black_bishop_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Bishop", current_column, current_row, final_column, final_row)
        else:
            return invalid_position_message


    def white_queen(current_row, current_column, final_row, final_column):

        def white_queen_check_next_move(row, column):
            # Rook's logic
            current_working_row = row - 1
            while current_working_row > -1:
                current_selected_figure = chess_board[current_working_row][column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1

            current_working_row = row + 1
            while current_working_row < 8:
                current_selected_figure = chess_board[current_working_row][column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1

            current_working_column = column - 1
            while current_working_column > -1:
                current_selected_figure = chess_board[row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_column -= 1

            current_working_column = column + 1
            while current_working_column < 8:
                current_selected_figure = chess_board[row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_column += 1

            current_working_row = row - 1
            current_working_column = column - 1
            while current_working_row > -1 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1
                current_working_column -= 1

            current_working_row = row + 1
            current_working_column = column + 1
            while current_working_row < 8 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1
                current_working_column += 1

            # Bishop's logic
            current_working_row = row - 1
            current_working_column = column + 1
            while current_working_row > -1 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1
                current_working_column += 1

            current_working_row = row + 1
            current_working_column = column - 1
            while current_working_row < 8 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["Black King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1
                current_working_column -= 1

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Queen", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Queen", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Queen", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Queen", current_column, current_row, final_column, final_row)

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
            if current_working_row == -1 or current_working_column == -1 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in white_figures:
                return invalid_position_message
            elif current_selected_figure in black_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Queen", current_column, current_row, final_column, final_row)

        elif final_row > current_row and final_column > current_column:
            current_working_row = current_row + 1
            current_working_column = current_column + 1
            while current_working_row < final_row and current_working_column < final_column and current_working_row < 8 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row += 1
                current_working_column += 1
            if current_working_row == 8 or current_working_column == 8 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in white_figures:
                return invalid_position_message
            elif current_selected_figure in black_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Queen", current_column, current_row, final_column, final_row)

        elif final_row < current_row and final_column > current_column:
            current_working_row = current_row - 1
            current_working_column = current_column + 1
            while current_working_row > final_row and current_working_column < final_column and current_working_row > -1 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row -= 1
                current_working_column += 1
            if current_working_row == -1 or current_working_column == 8 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in white_figures:
                return invalid_position_message
            elif current_selected_figure in black_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Queen", current_column, current_row, final_column, final_row)

        elif final_row > current_row and final_column < current_column:
            current_working_row = current_row + 1
            current_working_column = current_column - 1
            while current_working_row < final_row and current_working_column > final_column and current_working_row < 8 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row += 1
                current_working_column -= 1
            if current_working_row == 8 or current_working_column == -1 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in white_figures:
                return invalid_position_message
            elif current_selected_figure in black_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White Queen")
                current_check_checker = white_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White Queen", current_column, current_row, final_column, final_row)
        else:
            return invalid_position_message


    def black_queen(current_row, current_column, final_row, final_column):

        def black_queen_check_next_move(row, column):
            # Rook's logic
            current_working_row = row - 1
            while current_working_row > -1:
                current_selected_figure = chess_board[current_working_row][column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1

            current_working_row = row + 1
            while current_working_row < 8:
                current_selected_figure = chess_board[current_working_row][column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1

            current_working_column = column - 1
            while current_working_column > -1:
                current_selected_figure = chess_board[row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_column -= 1

            current_working_column = column + 1
            while current_working_column < 8:
                current_selected_figure = chess_board[row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_column += 1

            # Bishop's logic
            current_working_row = row - 1
            current_working_column = column - 1
            while current_working_row > -1 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1
                current_working_column -= 1

            current_working_row = row + 1
            current_working_column = column + 1
            while current_working_row < 8 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1
                current_working_column += 1

            current_working_row = row - 1
            current_working_column = column + 1
            while current_working_row > -1 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row -= 1
                current_working_column += 1

            current_working_row = row + 1
            current_working_column = column - 1
            while current_working_row < 8 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure == names_to_chess_figures_dictionary["White King"]:
                    return check_message(row, column)
                elif current_selected_figure in white_figures or current_selected_figure in black_figures:
                    break
                current_working_row += 1
                current_working_column -= 1

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Queen", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Queen", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Queen", current_column, current_row, final_column, final_row)

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
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Queen", current_column, current_row, final_column, final_row)

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
            if current_working_row == -1 or current_working_column == -1 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in black_figures:
                return invalid_position_message
            elif current_selected_figure in white_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Queen", current_column, current_row, final_column, final_row)

        elif final_row > current_row and final_column > current_column:
            current_working_row = current_row + 1
            current_working_column = current_column + 1
            while current_working_row < final_row and current_working_column < final_column and current_working_row < 8 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row += 1
                current_working_column += 1
            if current_working_row == 8 or current_working_column == 8 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in black_figures:
                return invalid_position_message
            elif current_selected_figure in white_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Queen", current_column, current_row, final_column, final_row)

        elif final_row < current_row and final_column > current_column:
            current_working_row = current_row - 1
            current_working_column = current_column + 1
            while current_working_row > final_row and current_working_column < final_column and current_working_row > -1 and current_working_column < 8:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row -= 1
                current_working_column += 1
            if current_working_row == -1 or current_working_column == 8 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in black_figures:
                return invalid_position_message
            elif current_selected_figure in white_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Queen", current_column, current_row, final_column, final_row)

        elif final_row > current_row and final_column < current_column:
            current_working_row = current_row + 1
            current_working_column = current_column - 1
            while current_working_row < final_row and current_working_column > final_column and current_working_row < 8 and current_working_column > -1:
                current_selected_figure = chess_board[current_working_row][current_working_column]
                if current_selected_figure in black_figures or current_selected_figure in white_figures:
                    return invalid_position_message
                current_working_row += 1
                current_working_column -= 1
            if current_working_row == 8 or current_working_column == -1 or current_working_row != final_row or current_working_column != final_column:
                return invalid_position_message
            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in black_figures:
                return invalid_position_message
            elif current_selected_figure in white_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black Queen", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black Queen")
                current_check_checker = black_queen_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black Queen", current_column, current_row, final_column, final_row)
        else:
            return invalid_position_message


    def white_king(current_row, current_column, final_row, final_column):

        def white_king_check_next_move(row, column):
            if (  # Upper row
                    (chess_board[row + 1][column - 1] == names_to_chess_figures_dictionary["Black King"] and row + 1 < 8 and column - 1 > -1) or
                    (chess_board[row + 1][column] == names_to_chess_figures_dictionary["Black King"] and row + 1 < 8) or
                    (chess_board[row + 1][column + 1] == names_to_chess_figures_dictionary["Black King"] and row + 1 < 8 and column + 1 < 8) or
                    # Same row
                    (chess_board[row][column - 1] == names_to_chess_figures_dictionary["Black King"] and column - 1 > -1) or
                    (chess_board[row][column + 1] == names_to_chess_figures_dictionary["Black King"] and column + 1 < 8) or
                    # Lower row
                    (chess_board[row - 1][column - 1] == names_to_chess_figures_dictionary["Black King"] and row - 1 > -1 and column - 1 > -1) or
                    (chess_board[row - 1][column] == names_to_chess_figures_dictionary["Black King"] and row - 1 > -1) or
                    (chess_board[row - 1][column + 1] == names_to_chess_figures_dictionary["Black King"] and row - 1 > -1 and column + 1 < 8)):
                return check_message(row, column)

        if (current_row == 7 and final_row == 7 and current_column == 4 and final_column == 7) or (current_row == 7 and final_row == 7 and current_column == 4 and final_column == 0):  # Making a Rocade

            if chess_board[7][5] in blank_spaces and chess_board[7][6] in blank_spaces and chess_board[7][7] == names_to_chess_figures_dictionary["White Rook"] and final_column == 7:
                chess_board[7][4] = names_to_chess_figures_dictionary["White Rook"]
                chess_board[7][7] = names_to_chess_figures_dictionary["White King"]
                return f'You successfully made a Rocade!'

            elif chess_board[7][3] in blank_spaces and chess_board[7][2] in blank_spaces and chess_board[7][1] in blank_spaces and chess_board[7][0] == names_to_chess_figures_dictionary["White Rook"] and final_column == 0:
                chess_board[7][4] = names_to_chess_figures_dictionary["White Rook"]
                chess_board[7][0] = names_to_chess_figures_dictionary["White King"]
                return f'You successfully made a Rocade!'

            else:
                return invalid_position_message

        elif (    # Upper row
                (current_row + 1 == final_row and current_column - 1 == final_column and current_row + 1 < 8 and current_column - 1 > -1) or
                (current_row + 1 == final_row and current_column == final_column and current_row + 1 < 8) or
                (current_row + 1 == final_row and current_column + 1 == final_column and current_row + 1 < 8 and current_column + 1 < 8) or
                # Same row
                (current_row == final_row and current_column - 1 == final_column and current_column - 1 > -1) or
                (current_row == final_row and current_column + 1 == final_column and current_column + 1 < 8) or
                # Lower row
                (current_row - 1 == final_row and current_column - 1 == final_column and current_row - 1 > -1 and current_column - 1 > -1) or
                (current_row - 1 == final_row and current_column == final_column and current_row - 1 > -1) or
                (current_row - 1 == final_row and current_column + 1 == final_column and current_row - 1 > -1 and current_column + 1 < 8)):

            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in white_figures:
                return invalid_position_message
            elif current_selected_figure in black_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White King")
                current_check_checker = white_king_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("White King", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "White King")
                current_check_checker = white_king_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("White King", current_column, current_row, final_column, final_row)

        else:
            return invalid_position_message


    def black_king(current_row, current_column, final_row, final_column):

        def black_king_check_next_move(row, column):
            if (  # Upper row
                    (chess_board[row + 1][column - 1] == names_to_chess_figures_dictionary["White King"] and row + 1 < 8 and column - 1 > -1) or
                    (chess_board[row + 1][column] == names_to_chess_figures_dictionary["White King"] and row + 1 < 8) or
                    (chess_board[row + 1][column + 1] == names_to_chess_figures_dictionary["White King"] and row + 1 < 8 and column + 1 < 8) or
                    # Same row
                    (chess_board[row][column - 1] == names_to_chess_figures_dictionary["White King"] and column - 1 > -1) or
                    (chess_board[row][column + 1] == names_to_chess_figures_dictionary["White King"] and column + 1 < 8) or
                    # Lower row
                    (chess_board[row - 1][column - 1] == names_to_chess_figures_dictionary["White King"] and row - 1 > -1 and column - 1 > -1) or
                    (chess_board[row - 1][column] == names_to_chess_figures_dictionary["White King"] and row - 1 > -1) or
                    (chess_board[row - 1][column + 1] == names_to_chess_figures_dictionary["White King"] and row - 1 > -1 and column + 1 < 8)):
                return check_message(row, column)

        if (current_row == 0 and final_row == 0 and current_column == 4 and final_column == 7) or (current_row == 0 and final_row == 0 and current_column == 4 and final_column == 0):  # Making a Rocade

            if chess_board[0][5] in blank_spaces and chess_board[0][6] in blank_spaces and chess_board[0][7] == names_to_chess_figures_dictionary["Black Rook"] and final_column == 7:
                chess_board[0][4] = names_to_chess_figures_dictionary["Black Rook"]
                chess_board[0][7] = names_to_chess_figures_dictionary["Black King"]
                return f'You successfully made a Rocade!'

            elif chess_board[0][3] in blank_spaces and chess_board[0][2] in blank_spaces and chess_board[0][1] in blank_spaces and chess_board[0][0] == names_to_chess_figures_dictionary["Black Rook"] and final_column == 0:
                chess_board[0][4] = names_to_chess_figures_dictionary["Black Rook"]
                chess_board[0][0] = names_to_chess_figures_dictionary["Black King"]
                return f'You successfully made a Rocade!'

            else:
                return invalid_position_message

        elif (  # Upper row
                (current_row + 1 == final_row and current_column - 1 == final_column and current_row + 1 < 8 and current_column - 1 > -1) or
                (current_row + 1 == final_row and current_column == final_column and current_row + 1 < 8) or
                (current_row + 1 == final_row and current_column + 1 == final_column and current_row + 1 < 8 and current_column + 1 < 8) or
                # Same row
                (current_row == final_row and current_column - 1 == final_column and current_column - 1 > -1) or
                (current_row == final_row and current_column + 1 == final_column and current_column + 1 < 8) or
                # Lower row
                (current_row - 1 == final_row and current_column - 1 == final_column and current_row - 1 > -1 and current_column - 1 > -1) or
                (current_row - 1 == final_row and current_column == final_column and current_row - 1 > -1) or
                (current_row - 1 == final_row and current_column + 1 == final_column and current_row - 1 > -1 and current_column + 1 < 8)):

            current_selected_figure = chess_board[final_row][final_column]
            if current_selected_figure in black_figures:
                return invalid_position_message
            elif current_selected_figure in white_figures:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black King")
                current_check_checker = black_king_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_taking("Black King", current_column, current_row, current_selected_figure, final_column, final_row)

            else:
                successful_moving_operations_function(current_row, current_column, final_row, final_column, "Black King")
                current_check_checker = black_king_check_next_move(final_row, final_column)
                if current_check_checker != None:
                    check_message_list.append(current_check_checker)
                return successful_moving("Black King", current_column, current_row, final_column, final_row)

        else:
            return invalid_position_message


    white_figures = ["♙", "♘", "♗", "♖", "♕", "♔"]
    black_figures = ["♟︎", "♞", "♝", "♜", "♛", "♚"]
    blank_spaces = ["□", "◼"]
    blank_white_space = "□"
    blank_black_space = "◼"
    chess_rows_dictionary = {8: 0, 7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}  # | rows
    chess_rows_dictionary_reversed_values = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}  # | rows
    chess_columns_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}  # _ columns
    chess_columns_dictionary_reversed_values = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}  # _ columns
    chess_figures_dictionary = {
        white_figures[0]: white_pawn,
        white_figures[1]: white_knight,
        white_figures[2]: white_bishop,
        white_figures[3]: white_rook,
        white_figures[4]: white_queen,
        white_figures[5]: white_king,

        black_figures[0]: black_pawn,
        black_figures[1]: black_knight,
        black_figures[2]: black_bishop,
        black_figures[3]: black_rook,
        black_figures[4]: black_queen,
        black_figures[5]: black_king
    }
    chess_figures_to_names_dictionary = {
        white_figures[0]: "White Pawn",
        white_figures[1]: "White Knight",
        white_figures[2]: "White Bishop",
        white_figures[3]: "White Rook",
        white_figures[4]: "White Queen",
        white_figures[5]: "White King",
        black_figures[0]: "Black Pawn",
        black_figures[1]: "Black Knight",
        black_figures[2]: "Black Bishop",
        black_figures[3]: "Black Rook",
        black_figures[4]: "Black Queen",
        black_figures[5]: "Black King",
        blank_white_space: "White Space",
        blank_black_space: "Black Space"
    }
    names_to_chess_figures_dictionary = {
        "White Pawn": white_figures[0],
        "White Knight": white_figures[1],
        "White Bishop": white_figures[2],
        "White Rook": white_figures[3],
        "White Queen": white_figures[4],
        "White King": white_figures[5],
        "Black Pawn": black_figures[0],
        "Black Knight": black_figures[1],
        "Black Bishop": black_figures[2],
        "Black Rook": black_figures[3],
        "Black Queen": black_figures[4],
        "Black King": black_figures[5],
        "White Space": blank_white_space,
        "Black Space": blank_black_space
    }


    chess_board = []


    def initializing_chess_board():
        for i in range(8):
            current_chess_row = []

            for index in range(8):

                # Even Rows even Columns
                if (i % 2 == 0 and index % 2 == 0):
                    current_chess_row.append("□")
                # Even Rows uneven Columns
                elif (i % 2 == 0 and index % 2 != 0):
                    current_chess_row.append("◼")
                # Uneven Rows even Columns
                elif (i % 2 != 0 and index % 2 == 0):
                    current_chess_row.append("◼")
                # Uneven Rows uneven Columns
                elif (i % 2 != 0 and index % 2 != 0):
                    current_chess_row.append("□")

            chess_board.append(current_chess_row)


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


    initializing_chess_board()
    initializing_white_figures()
    initializing_black_figures()


    def console_print_chess_board():
        print("   " + "   ".join(chess_columns_dictionary.keys()))
        for index in range(len(chess_board)):
            row = chess_board[index]
            if row == 0 or row == 1 or row == 6 or row == 7:
                print(f'{chess_rows_dictionary_reversed_values[index]}  ' + "  ".join(
                    row) + f'  {chess_rows_dictionary_reversed_values[index]}')
            else:
                print(f'{chess_rows_dictionary_reversed_values[index]}  ' + "  ".join(
                    row) + f'  {chess_rows_dictionary_reversed_values[index]}')
        print("   " + "   ".join(chess_columns_dictionary.keys()))


    def external_print_chess_board():
        root = tk.Tk()
        label = tk.Label(root, font=("Arial", 20))
        label.pack()

        label_text = "  " + "   ".join([str(el) for el in chess_columns_dictionary.keys()])

        for index in range(len(chess_board)):
            row = chess_board[index]
            label_text += f'\n{chess_rows_dictionary_reversed_values[index]} ' + "  ".join(
                row) + f' {chess_rows_dictionary_reversed_values[index]}'

        label_text += f'\n  ' + "   ".join([str(el) for el in chess_columns_dictionary.keys()])

        label.config(text=label_text)
        root.mainloop()


    console_print_chess_board() if print_type == "console" else external_print_chess_board()


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


    clear_history_file()

    current_player_index = -1
    check_message_list = []

    while True:  # The cycle is necessary because we don't know how many times the game will last
        current_player_index += 1
        time.sleep(1.5)
        current_position = input(Fore.LIGHTWHITE_EX + ("White player, enter the position that you want to move: (E2) ")) if current_player_index % 2 == 0 else input(Fore.LIGHTGREEN_EX + ("Black player, enter the position that you want to move: (E7) "))
        time.sleep(0.5)
        final_position = input("White player, enter the final position that you wish to make: (E4) ") if current_player_index % 2 == 0 else input("Black player, enter the final position that you wish to make: (E5) ")

        try:
            current_selected_row = chess_rows_dictionary[int(current_position[1])]
            current_selected_column = chess_columns_dictionary[current_position[0].upper()]
            final_selected_row = chess_rows_dictionary[int(final_position[1])]
            final_selected_column = chess_columns_dictionary[final_position[0].upper()]

        except (KeyError, ValueError, IndexError):
            time.sleep(1)
            print(f'White player, you have selected an invalid position. Try again.') if current_player_index % 2 == 0 else print(f'Black player, you have selected an invalid position. Try again.')
            current_player_index -= 1
            continue

        validate_result = validate_positions(current_selected_row, current_selected_column, final_selected_row, final_selected_column)

        if validate_result == False:
            current_player_index -= 1
            continue

        current_selected_figure = chess_board[current_selected_row][current_selected_column]
        result = chess_figures_dictionary[current_selected_figure](current_selected_row, current_selected_column, final_selected_row, final_selected_column)
        time.sleep(1)

        if result == invalid_position_message:
            print(result)
            current_player_index -= 1
            continue

        console_print_chess_board() if print_type == "console" else external_print_chess_board()
        time.sleep(1.5)
        print(result)

        if len(check_message_list) > 0:
            time.sleep(1)
            print(Fore.YELLOW + f.renderText("Check!"))
            time.sleep(1.2)
            print(Fore.YELLOW + check_message_list[0])
            check_message_list = []


        def writing_current_data():

            history_file = open("current_chess_game_history.txt", "a", encoding="utf-8")
            history_file.write(f'{result}\n')
            history_file.close()

        writing_current_data()

        if names_to_chess_figures_dictionary["Black King"] in result or names_to_chess_figures_dictionary["White King"] in result:  # One of the kings is in the result string
            if result.index(names_to_chess_figures_dictionary["Black King"]) > result.index("took"):
                time.sleep(1.5)
                print(Fore.LIGHTCYAN_EX + f.renderText('GAME OVER!'))
                time.sleep(1.5)
                print(Fore.LIGHTCYAN_EX + f.renderText('White player won!'))
                return "white_player"
            elif result.index(names_to_chess_figures_dictionary["White King"]) > result.index("took"):
                time.sleep(1.5)
                print(Fore.LIGHTCYAN_EX + f.renderText('GAME OVER!'))
                time.sleep(1.5)
                print(Fore.LIGHTCYAN_EX + f.renderText('Black player won!'))
                return "black_player"


the_game_is_on = True
white_player_victories = 0
black_player_victories = 0

while the_game_is_on:
    print(Fore.LIGHTWHITE_EX + f.renderText(f'The Game is Starting...'))
    time.sleep(2)

    current_game_result = chess_game()

    if current_game_result == "white_player":
        white_player_victories += 1
    elif current_game_result == "black_player":
        black_player_victories += 1

    time.sleep(1.5)

    if input(Fore.LIGHTCYAN_EX + "Do you want to see the moves that both of you made during the game? Y/N ").upper() == "Y":
        reading_history_file = open("current_chess_game_history.txt", "r", encoding="utf-8")
        current_game_history = reading_history_file.readlines()

        for index in range(len(current_game_history)):
            time.sleep(2)
            row = current_game_history[index]
            row = row.replace("\n", "")
            if index % 2 == 0:
                print(Fore.LIGHTWHITE_EX + row)
            else:
                print(Fore.LIGHTGREEN_EX + row)
        time.sleep(2)

    print(Fore.LIGHTCYAN_EX + f'The current score is White: {white_player_victories} victories, Black: {black_player_victories} victories.')

    time.sleep(2)

    if input("Do you wish to play another game? Y/N ").upper() != "Y":
        the_game_is_on = False
        time.sleep(1)


        def print_text(text):
            for letter in text:
                print(Fore.LIGHTCYAN_EX + letter, end="")
                time.sleep(0.28)


        print_text("Thank you for playing!")
        time.sleep(1.5)
        print('\n')
        print(Fore.LIGHTRED_EX + f.renderText("Until next time!"))
    else:
        time.sleep(1.5)
