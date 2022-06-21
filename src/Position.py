
class Position:

    def __init__(self, row, column):
        self.row = row # number
        self.column = column # letter


    def is_valid(self):
        return self.row >= 1 and self.row <= 8 and self.column >= "a" and self.column <= "h"


    def get_translation(self, nr_columns, nr_rows):
        new_column = chr(nr_columns + ord(self.column))
        new_row = self.row + nr_rows

        new_position = Position(new_row, new_column)
        return new_position # doesnt check whether the new position is valid or not
