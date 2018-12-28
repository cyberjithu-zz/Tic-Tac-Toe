# -*- coding: utf-8 -*-

class InvalidMoveException(Exception):

    def __init__(self, *args, **kwargs):
        super(InvalidMoveException, self).__init__(*args, **kwargs)
