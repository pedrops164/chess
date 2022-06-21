from src.Piece import Piece

class Pawn(Piece):

    def __init__(self, position, is_white):
        super().__init__(self, position, is_white)
        self.first_move = True


    def get_all_moves(self):
        all_moves = []

        if (self.is_white):
            all_moves.append(self.position.get_translation(1,0))
            if (self.first_move):
                all_moves.append(self.position.get_translation(2, 0))
        else:
            all_moves.append(self.position.get_translation(-1, 0))
            if (self.first_move):
                all_moves.append(self.position.get_translation(-2, 0))

        return all_moves

