import re

from tic_tac_toe.all_exceptions import *


class Player:
    __created_player = []

    def __init__(self, player_number):
        self.__validate_player_number(player_number)
        self.__player_number = player_number
        self.__created_player.append(player_number)

    def __validate_player_number(self, player_number):
        if not re.fullmatch("[0-9]", player_number):
            raise InvalidInputException("Player Number must be a number 1 or 2")

        if int(player_number) > 2 or int(player_number) < 1:
            raise InvalidPlayerException("Player can be 1 or 2 ONLY")

        if player_number in self.__created_player:
            raise InvalidPlayerException("Player cannot be created twice")

    def get_player_number(self) -> str:
        return self.__player_number

    @classmethod
    def clear_created_players(cls):
        cls.__created_player.clear()
