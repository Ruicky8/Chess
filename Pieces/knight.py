from Pieces.piece import Piece

class Knight(Piece):
    """
    | Knight, can move in L.
    """

    def is_valid(self, i: int, j: int) -> bool:
        """
        | Check which moves are valid. Being i the row and j the column.
        """
        if (abs(self.row - i) != 0 and abs(self.column - j) != 0
                and abs(self.row - i) + abs(self.column - j) == 3):            
            return True
        return False