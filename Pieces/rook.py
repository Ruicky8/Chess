from Pieces.piece import Piece

class Rook(Piece):
    """
    | Rook, can move in the whole column or row.
    """

    def is_valid(self, i: int, j: int) -> bool:
        """
        | Check which moves are valid. Being i the row and j the column.
        """

        if self.column == j or self.row == i:
            return True
        return False