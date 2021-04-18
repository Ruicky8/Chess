from Pieces.piece import Piece

class Queen(Piece):
    """
    | Queen, can move in diagonal or in the same row|column
    """

    def is_valid(self, i: int, j: int) -> bool:
        """
        | Check which moves are valid. Being i the row and j the column.
        """
        
        if abs(self.row - i) == abs(self.column - j):
            return True
        elif self.column == j or self.row == i:
            return True
        return False
