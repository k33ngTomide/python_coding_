import unittest

from tic_tac_toe.all_exceptions import InvalidPlayerException
from tic_tac_toe.player import Player


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.player_1 = Player("1")
        self.player_2 = Player("2")

    def tearDown(self) -> None:
        Player.clear_created_players()

    def test_that_player_can_be_created(self):
        player_number = self.player_1.get_player_number()
        self.assertEqual("1", player_number)

    def test_that_both_players_can_be_created(self):
        self.assertEqual("1", self.player_1.get_player_number())
        self.assertEqual("2", self.player_2.get_player_number())

    def test_that_player_can_only_be_one_and_two(self):
        self.assertEqual("1", self.player_1.get_player_number())
        self.assertEqual("2", self.player_2.get_player_number())

        self.assertRaises(InvalidPlayerException, Player, "3")

    def test_that_players_cannot_be_duplicated(self):
        self.assertRaises(InvalidPlayerException, Player, "2")
        self.assertRaises(InvalidPlayerException, Player, "1")


if __name__ == '__main__':
    unittest.main()
