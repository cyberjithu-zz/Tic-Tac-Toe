# -*- coding: utf-8 -*-
import unittest

from ..tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def all_values_set_during_startup(self):
        '''Check whether all default values have been created properly'''
        game = TicTacToe()
        # check total number of possible move's
        self.assertEqual(len(game.possible_moves) == 9)
        # check total number of winning move's
        self.assertEqual(len(game.winning_combinations) == (game.dimension ** 2) + 2)
        self.assertEqual(game.status, None)
        self.assertEqual(game.game_end, None)


