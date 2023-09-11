import itertools
import re

from tic_tac_toe.all_exceptions import *


class Board:

    def __init__(self):
        self.__game_board = [
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."]
        ]
        self.__is_empty = True
        self.__winner = "None"

    def is_empty(self):
        for row in self.__game_board:
            for space in row:
                if space != ".":
                    self.__is_empty = False
        return self.__is_empty

    def game_restart(self):
        self.__game_board = [
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."]
        ]
        self.__is_empty = True
        self.__winner = "None"

    def __make_move(self, spot: str, shape):

        if re.fullmatch("[0-9]", spot) and 1 <= int(spot) <= 9:
            for extra_counter, (counter, new_counter) in enumerate(itertools.product(range(3), range(3)), start=1):
                if int(spot) == extra_counter:
                    self.__validate_spot_is_not_played(self.__game_board[counter][new_counter])
                    self.__game_board[counter][new_counter] = shape
        else:
            raise InvalidMoveException("Moves can only be between 1 to 9")

    @staticmethod
    def __validate_spot_is_not_played(space):
        if space != ".":
            raise InvalidMoveException("Filled space cannot be refilled")

    def move(self, player, spot):
        if player == 1:
            exact_shape = 'X'
        elif player == 2:
            exact_shape = 'O'
        else:
            raise InvalidPlayerException("Players can ONLY be 1 or 2")

        self.__make_move(spot, exact_shape)

    def is_filled(self) -> bool:
        for row in self.__game_board:
            for space in row:
                if space == '.':
                    return False
        return True

    def check_winner(self) -> str:

        self.__line_check_one()
        self.__line_check_two()
        self.__line_check_three()
        self.__line_check_four()
        self.__line_check_five()
        self.__line_check_six()
        self.__line_check_seven()
        self.__line_check_eight()

        if self.is_filled() and self.__winner == "None":
            self.__winner = "Draw"

        return self.__winner

    def check_player(self, equal, first_space):
        filled = first_space != "."
        if filled and equal:
            if first_space == "X":
                self.__winner = "Player 1 Won"
            elif first_space == "O":
                self.__winner = "Player 2 Won"

    def __line_check_eight(self):
        all_equal = self.__game_board[0][0] == self.__game_board[1][1] == self.__game_board[2][2]
        self.check_player(all_equal, self.__game_board[0][0])

    def __line_check_seven(self):
        all_equal = self.__game_board[0][2] == self.__game_board[1][2] == self.__game_board[2][2]
        self.check_player(all_equal, self.__game_board[0][2])

    def __line_check_six(self):
        all_equal = self.__game_board[0][1] == self.__game_board[1][1] == self.__game_board[2][1]
        self.check_player(all_equal, self.__game_board[0][1])

    def __line_check_five(self):
        all_equal = self.__game_board[2][0] == self.__game_board[1][1] == self.__game_board[0][2]
        self.check_player(all_equal, self.__game_board[2][0])

    def __line_check_four(self):
        all_equal = self.__game_board[2][0] == self.__game_board[2][1] == self.__game_board[2][2]
        self.check_player(all_equal, self.__game_board[2][0])

    def __line_check_three(self):
        all_equal = self.__game_board[1][0] == self.__game_board[1][1] == self.__game_board[1][2]
        self.check_player(all_equal, self.__game_board[1][0])

    def __line_check_two(self):
        all_equal = self.__game_board[0][0] == self.__game_board[1][0] == self.__game_board[2][0]
        self.check_player(all_equal, self.__game_board[0][0])

    def __line_check_one(self):
        all_equal = self.__game_board[0][0] == self.__game_board[0][1] == self.__game_board[0][2]
        self.check_player(all_equal, self.__game_board[0][0])

    def print_board(self):
        for row in self.__game_board:
            for space in row:
                print(space, end="   ")
            print()
