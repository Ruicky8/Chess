from Pieces.piece import Piece

class King(Piece):
    """
    | King, can move one in any direction
    """

    def is_valid(self, i: int, j: int) -> bool:
        """
        | Check which moves are valid. Being i the row and j the column.
        """

        if abs(self.row - i) <= 1 and abs(self.column - j) <= 1:
            return True
        return False

    def can_castle(self, i: int, j: int) -> bool:
        """
        | Check if there is free path to the rook.
        """
        pass
