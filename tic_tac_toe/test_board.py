import unittest

from tic_tac_toe.all_exceptions import *
from tic_tac_toe.board import Board


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board()

    def test_that_board_is_empty_before_game_start(self):
        self.assertTrue(self.board.is_empty())

    def test_that_board_is_not_empty_if_player_play(self):
        self.board.move(1, "1")
        self.assertFalse(self.board.is_empty())

    def test_that_board_can_be_filled_totally(self):
        self.board.move(1, "1")
        self.board.move(2, "2")
        self.board.move(1, "3")
        self.board.move(2, "4")
        self.board.move(1, "5")
        self.board.move(2, "6")
        self.board.move(1, "7")
        self.board.move(2, "8")
        self.board.move(1, "9")

        self.assertTrue(self.board.is_filled())

    def test_that_board_raises_exception_if_move_is_invalid(self):
        self.assertRaises(InvalidMoveException, self.board.move, 1, "10")
        self.assertRaises(InvalidMoveException, self.board.move, 1, "0")
        self.assertRaises(InvalidMoveException, self.board.move, 1, "-10")
        self.assertRaises(InvalidMoveException, self.board.move, 1, "19")
        self.assertRaises(InvalidMoveException, self.board.move, 1, " ")
        self.assertRaises(InvalidMoveException, self.board.move, 1, "a")
        self.assertRaises(InvalidMoveException, self.board.move, 1, "-1")

    def test_that_board_raises_exception_if_player_is_invalid(self):
        self.assertRaises(InvalidPlayerException, self.board.move, 8, "1")

    def test_that_game_can_be_restarted(self):
        self.board.move(1, "1")
        self.board.move(2, "2")
        self.board.move(1, "3")
        self.board.move(2, "4")
        self.board.move(1, "5")

        self.assertFalse(self.board.is_empty())
        self.assertFalse(self.board.is_filled())

        self.board.game_restart()
        self.assertTrue(self.board.is_empty())

    def test_that_a_spot_that_has_been_filled_cannot_be_refilled(self):
        self.board.move(2, "1")
        self.board.move(1, "5")

        self.assertRaises(InvalidMoveException, self.board.move, 2, "5")

    def test_that_board_can_decide_Player_one_win(self):
        self.board.move(1, "1")
        self.board.move(2, "5")
        self.board.move(1, "9")
        self.board.move(2, "4")
        self.board.move(1, "6")
        self.board.move(2, "2")
        self.board.move(1, "8")
        self.board.move(2, "7")
        self.board.move(1, "3")

        winner = self.board.check_winner()
        self.assertEqual("Player 1 Won", winner)

    def test_that_board_can_decide_Player_two_win(self):
        self.board.move(1, "7")
        self.board.move(2, "1")
        self.board.move(1, "2")
        self.board.move(2, "5")
        self.board.move(1, "6")
        self.board.move(2, "9")

        winner = self.board.check_winner()
        self.assertEqual("Player 2 Won", winner)

    def test_that_board_can_determine_draw(self):
        self.board.move(1, "6")
        self.board.move(2, "3")
        self.board.move(1, "1")
        self.board.move(2, "8")
        self.board.move(1, "2")
        self.board.move(2, "5")
        self.board.move(1, "7")
        self.board.move(2, "4")
        self.board.move(1, "9")

        winner = self.board.check_winner()
        self.assertEqual("Draw", winner)

    def test_that_board_can_be_printed(self):
        self.board.move(1, "6")
        self.board.move(2, "3")
        self.board.move(1, "1")
        self.board.move(2, "8")
        self.board.move(1, "2")
        self.board.move(2, "5")
        self.board.move(1, "7")
        self.board.move(2, "4")
        self.board.move(1, "9")

        self.board.print_board()


if __name__ == '__main__':
    unittest.main()
