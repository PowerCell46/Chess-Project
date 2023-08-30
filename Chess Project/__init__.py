from colorama import Fore
from pyfiglet import Figlet
import time
import webbrowser
from chess_project import chess_game

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
        time.sleep(0.5)
        webbrowser.open("https://www.youtube.com/watch?v=OCSbzArwB10")

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

print_type = input("How do you want the chess board to be printed? On the console or externally? (Console/Externally) ").lower()

print_type = print_type if print_type == "console" or print_type == "externally" else "console"

time.sleep(1.5)


the_game_is_on = True
white_player_victories = 0
black_player_victories = 0

while the_game_is_on:
    opponent_type = input("Are you going to play with another Person or are you going to play against Chat GPT? (Player/Bot) ").lower()
    opponent_type = "bot" if opponent_type != "player" and opponent_type != "bot" else opponent_type
    time.sleep(1)

    print(Fore.LIGHTWHITE_EX + f.renderText(f'The Game is Starting...'))
    time.sleep(2)

    current_game_result = chess_game(print_type, f, opponent_type)

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
