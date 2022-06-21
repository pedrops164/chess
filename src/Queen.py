from Piece import Piece
from src.exceptions.InvalidPosition import InvalidPosition


class Queen(Piece):

    def __init__(self, position, is_white):
        super().__init__(self, position, is_white)

    def get_all_moves(self):
        all_moves = []

        # all moves to the right
        self.add_moves_in_direction(1, 0, all_moves)
        # all moves to the left
        self.add_moves_in_direction(-1, 0, all_moves)
        # all moves up
        self.add_moves_in_direction(0, 1, all_moves)
        # all moves down
        self.add_moves_in_direction(0, -1, all_moves)
        # all moves right up
        self.add_moves_in_direction(1, 1, all_moves)
        # all moves right down
        self.add_moves_in_direction(1, -1, all_moves)
        # all moves left up
        self.add_moves_in_direction(-1, 1, all_moves)
        # all moves left down
        self.add_moves_in_direction(-1, -1, all_moves)

        return all_moves


