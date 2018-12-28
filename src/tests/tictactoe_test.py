# -*- coding: utf-8 -*-
import unittest

from game.tic_tac_toe import TicTacToe
from game.tictactoe_exceptions import InvalidMoveException


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def tearDown(self):
        self.game.reset_game()

    def all_values_set_during_startup(self):
        '''Check whether all default values have been created properly'''
        # game = TicTacToe()
        # check total number of possible move's
        self.assertEqual(len(self.game.possible_moves) == 9)
        # check total number of winning move's
        self.assertEqual(len(self.game.winning_combinations) == (self.game.dimension ** 2) + 2)
        self.assertEqual(self.game.status, None)
        self.assertEqual(self.game.game_end, None)

    def return_exception(self, player):
        '''Make a move based on the player and return the exception class'''
        try:
            self.game.mark_choice(player, (1, 1))
        except InvalidMoveException as err:
            return err
        except Exception as er:
            return er

    def invalid_player_turn_check(self):
        '''After the toss, if other player is initiating the movement, raise error'''
        # game = TicTacToe()
        err_msg = 'Please wait for the opponent to play before you make further move'
        turn = self.game.player_one_turn
        if turn:
            err = self.return_exception("Two")
        else:
            err = self.return_exception("One")
        self.assertIsInstance(err, InvalidMoveException)
        self.assertEqual(err_msg, err.args[0].strip())


if __name__ == '__main__':
    unittest.main()
