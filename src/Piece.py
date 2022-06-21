from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, position, is_white):
        self.position = position
        self.is_white = is_white

    """
    Abstract Method that returns all the moves that this piece can make inside the chess board,
    whether they are possible or not
    """
    @abstractmethod
    def get_all_moves(self):
        pass

    def add_moves_in_direction(self, x, y, moves_list):
        aux_position = self.position.get_translation(x, y)
        while (aux_position.is_valid()):
            moves_list.append(aux_position)
            aux_position = aux_position.get_translation(x, y)