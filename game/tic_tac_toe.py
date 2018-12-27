
class TicTacToe(object):

    def __init__(self, player_one_name, player_two_name, bot=False):
        pass
    

    def generate_moves(self, dimension=3):
        '''Generate all possible combinations of the game board along with 
            the winning positions. 
        '''
        # to store winning combinations
        self.winning_combinations = []
        # to store all the moves available in a game
        self.possible_moves = []
        # stores intermediate moves while generating the moves
        inter_moves = set()
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
                inter_moves.add((ival, jval))
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
            self.possible_moves.append(inter_moves)
            inter_moves = set()
        self.winning_combinations.append(diagonal_set1)
        self.winning_combinations.append(diagonal_set2)
        del diagonal_set1
        del diagonal_set2
        del column_set
        del row_set
