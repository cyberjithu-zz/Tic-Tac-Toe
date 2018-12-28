# -*- coding: utf-8 -*-

import random

from utils import gen_name
from tictactoe_exceptions import InvalidMoveException


class TicTacToe(object):

    def __init__(self, player_one_name='One', player_two_name='Two', bot=False, dimension=3):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.bot = bot
        self.dimension = dimension
        self.reset_game()

    def reset_game(self):
        '''Reset the values to defaults '''
        if self.bot:
            self.player_two_name = gen_name()
        self.player_one_moves = set()
        self.player_two_moves = set()
        self.toss()
        self.status = None
        self.game_end = None
        self.generate_moves()

    def toss(self):
        if random.randint(1, 2) == 1:
            self.player_one_turn = True
        else:
            self.player_one_turn = False

    def generate_moves(self):
        '''Generate all possible combinations of the game board along with
            the winning positions.
        '''
        # to store winning combinations
        self.winning_combinations = []
        # to store all the moves available in a game
        self.possible_moves = []
        # stores each row at a time, for winning moves
        row_set = set()
        # column storage, for winning moves
        column_set = set()
        # stores the two diagonal winning positions, for winning moves
        diagonal_set1 = set()
        diagonal_set2 = set()
        for ival in xrange(self.dimension):
            for jval in xrange(self.dimension):
                # for diagonal values
                if ival == jval:
                    diagonal_set1.add((ival, jval))
                    diagonal_set2.add((self.dimension - ival - 1, jval))
                # for all possible combos
                self.possible_moves.append((ival, jval))
                # winning row set
                row_set.add((ival, jval))
                # winning column set, interchange i and j here to get column
                column_set.add((jval, ival))
            # Add it to winning combinations
            self.winning_combinations.append(row_set)
            self.winning_combinations.append(column_set)
            # reset the values here
            row_set = set()
            column_set = set()
        self.winning_combinations.append(diagonal_set1)
        self.winning_combinations.append(diagonal_set2)
        del diagonal_set1
        del diagonal_set2
        del column_set
        del row_set

    def get_player_pointer(self, player):
        '''Reuturn the current player move set and a boolean value to
            update the `player_one_turn` value.

            Args:
                player:     str, name of the player


            Return:
                turn, choice_set:   tuple(bool, set)

                                        contains a boolean value,
                                        which indicates the first player turn status and

                                        a set, of that corresponding players choices he has
                                        already taken.
        '''
        if player == self.player_one_name:
            return False, self.player_one_moves
        elif player == self.player_two_name:
            return True, self.player_two_moves
        else:
            raise ValueError("Invalid Player Name")

    def update_player_moves(self, player, choice):
        '''Based on the player name update the move in their respective sets

            Args:

                player: str, name of the player
                choice: tuple, contians the row, column valuse as tuple

        '''
        # first player
        player_turn, player_choices = self.get_player_pointer(player)
        player_choices.add(choice)
        self.possible_moves.remove(choice)
        self.player_one_turn = player_turn
        self.check_game_status(player_choices, player)

    def make_bot_moves(self):
        pass

    def mark_choice(self, player, choice):
        '''Add the movement to respective player's choice set'''
        if choice not in self.possible_moves:
            raise InvalidMoveException("Not a valid choice of input")
        else:
            # restrict the player from making two moves together
            # `if` and `elif` can be combined by an `or` statment
            # but for readability purpose splitted into two.
            if self.player_one_turn and player == self.player_two_name:
                raise InvalidMoveException("Please wait for the opponent to play before you make further move")
            elif not self.player_one_turn and player == self.player_one_name:
                raise InvalidMoveException("Please wait for the opponent to play before you make further move")
            else:
                self.update_player_moves(player, choice)

    def check_game_status(self, player_choices, player):
        ''' '''
        message = ""
        for set_win in self.winning_combinations:
            if set_win.issubset(player_choices):
                self.game_end = True
                self.status = player
                message = "\n\nGame Over! {} won the match\n\n".format(player)
                break
        # if possible_moves is empty no further move is possible
        if not self.possible_moves:
            self.game_end = True
            self.status = "DRAW"
            message = "\n\nGame Over! Its a DRAW\n\n"
        self.show_console_board(message)

    def show_console_board(self, message=""):
        print '     ' + ' |  '.join([str(i) for i in xrange(self.dimension)])
        print '   ' + '-' * (self.dimension * 5)
        for i in xrange(self.dimension):
            print ' {} |'.format(i),
            for j in xrange(self.dimension):
                if (i, j) in self.player_one_moves:
                    print 'X ' + '| ',
                elif (i, j) in self.player_two_moves:
                    print 'O ' + '| ',
                else:
                    print '  | ',
            else:
                print
                print '   ' + '-' * (self.dimension * 5)
        print message

