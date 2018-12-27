import random

from exceptions import InvalidMoveException


class TicTacToe(object):

    def __init__(self, player_one_name, player_two_name, bot=False):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.bot = bot
        self.player_one_moves = set()
        self.player_two_moves = set()
        self.toss()

    def toss(self):
        if random.randint(1, 2) == 1:
            self.player_one_turn = True
        else:
            self.player_one_turn = False

    def generate_moves(self, dimension=3):
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
        for ival in xrange(dimension):
            for jval in xrange(dimension):
                # for diagonal values
                if ival == jval:
                    diagonal_set1.add((ival, jval))
                    diagonal_set2.add((dimension - ival - 1, jval))
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

    def update_player_moves(self, player, choice):
        '''Based on the player name update the move in their respective sets

            Args:

                player: str, name of the player
                choice: tuple, contians the row, column valuse as tuple

        '''
        # first player
        if self.player_one_turn:
            self.player_one_moves.add(choice)
            self.possible_moves.remove(choice)
            self.player_one_turn = False
        else:
            self.player_two_moves.add(choice)
            self.possible_moves.remove(choice)
            self.player_one_turn = True

    def mark_choice(self, player, choice):
        '''Add the movement to respective player's choice set'''
        if choice in self.possible_moves:
            pass
        else:
            raise  InvalidMoveException("Not a valid choice of input")