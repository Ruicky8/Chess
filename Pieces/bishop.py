from Pieces.piece import Piece

class Bishop(Piece):
    """
    | Bishop, can move in diagonal.
    """

    def is_valid(self, i: int, j: int) -> bool:
        """
        | Check which moves are valid. Being i the row and j the column.
        """

        if abs(self.row - i) == abs(self.column - j):
            return True
        return False
