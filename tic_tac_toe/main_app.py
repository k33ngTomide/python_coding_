from tic_tac_toe.all_exceptions import *
from tic_tac_toe.board import Board
from tic_tac_toe.player import Player


class Play:

    def __init__(self):
        self.__first_player = Player("1")
        self.__second_player = Player("2")
        self.__board = Board()
        self.__current_player = 0
        self.__number = 1

    def welcome(self):

        print("""TIC-TAC-TOE \n Welcome
            press: 
            1. X
            2. O 
        """)
        try:
            user_input = input("Input your choice: ")
            if user_input == "1":
                print("Selected Player 1")
            elif user_input == "2":
                print("Selected Player 2")
            else:
                Player(user_input)
        except (InvalidPlayerException, InvalidInputException) as err:
            print(err)
            self.welcome()

    def play(self):

        print("Pick between 1 to 9 to select: ")
        winner = "None"

        while True:
            if winner != "None":
                print(winner)
                self.__play_again()

            try:
                self.__current_player = self.__first_player.get_player_number() if self.__number % 2 != 0 \
                    else self.__second_player.get_player_number()

                wanted_spot = input(f"Player {self.__current_player} turn \nPick a number: ")

                self.__board.move(int(self.__current_player), wanted_spot)
                self.__board.print_board()
                winner = self.__board.check_winner()
                self.__number += 1
            except InvalidMoveException as err:
                print(err)

    def __play_again(self):
        user_input = input("Play again? \n1. Yes \n2. No \n Enter: ")
        if user_input == "1":
            self.__board.game_restart()
            self.__number = 1
            self.welcome()
        elif user_input == "2":
            print("Closing...")
            exit(1)
