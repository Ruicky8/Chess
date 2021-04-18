from Pieces.piece import Piece

class Pawn(Piece):
    """
    | Pawn, can move 2 blocks forward in its first move, then one block
    | each movement. It can only eat pieces in diagonal.
    """

    def is_valid(self, i: int, j: int) -> bool:
        """
        | Check which moves are valid. Being i the row and j the column.
        """
        
        if self.column == j:
            if self.row == 2:
                if i - self.row in [1,2]:
                    return True
            elif self.row == 7:
                if i - self.row in [-1,-2]:
                    return True
            else:
                if self.color == False:
                    if i - self.row == 1:
                        return True
                else:
                    if i - self.row == -1:
                        return True
        return False

    def eat_diagonal(self, i: int, j: int, pieces: list) -> bool:
        if abs(self.row - i) == 1 and abs(self.column - j) == 1:
            for p in pieces:
                if p.color != self.color and p.row == i and p.column == j:
                    return True
        return False
