# -*- coding: utf-8 -*-
import unittest

# from src.game.tic_tac_toe import TicTacToe
# from src.game.tictactoe_exceptions import InvalidMoveException
from game.tic_tac_toe import TicTacToe
from game.tictactoe_exceptions import InvalidMoveException


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def tearDown(self):
        self.game.reset_game()

    def test_all_values_set_during_startup(self):
        '''Check whether all default values have been created properly'''
        # game = TicTacToe()
        # check total number of possible move's
        self.assertEqual(len(self.game.possible_moves), 9)
        # check total number of winning move's
        self.assertEqual(len(self.game.winning_combinations), (self.game.dimension * 2) + 2)
        self.assertEqual(self.game.status, None)
        self.assertEqual(self.game.game_end, None)

    def test_invalid_player_turn_check(self):
        '''After the toss, if other player is initiating the movement, raise error'''
        turn = self.game.player_one_turn
        if turn:
            with self.assertRaises(InvalidMoveException) as testexception:
                self.game.mark_choice('Two', (1, 1))
            # err = return_exception(self.game, "Two")
        else:
            with self.assertRaises(InvalidMoveException) as testexception:
                self.game.mark_choice('One', (1, 1))

    def test_validate_name(self):
        '''Check for raising error if we move using another unregisterd name'''
        with self.assertRaises(ValueError) as testexception:
            self.game.mark_choice('TestPlayer', (1, 1))


if __name__ == '__main__':
    unittest.main()
