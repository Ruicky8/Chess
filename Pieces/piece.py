from board import Board

class Piece():
    """
    | General piece. Super class for all the pieces in the game.
    """

    def __init__(self, color, row, column, letter):
        self.color = 'w' if color.lower() == 'white' else 'b'
        # int value from 1 to 8 due to the board borders.
        self.row = row
        self.column = ord(column) - 96

        # Piece position to make it more visual
        self.position = column + str(row)
        # Get the symbol to display in board
        self.symbol = self.get_symbol(color[0].lower(), letter)
        

    def get_symbol(self, color: chr, letter: chr) -> str:
        """
        | Unicode codes for chess pieces.
        """

        if color == 'w':
            if letter == 'k':
                return "\u2654"
            elif letter == 'q':
                return "\u2655"
            elif letter == 'r':
                return "\u2656"
            elif letter == 'b':
                return "\u2657"
            elif letter == 'n':
                return "\u2658"
            elif letter == 'p':
                return "\u2659"
        else:
            if letter == 'k':
                return "\u265A"
            elif letter == 'q':
                return "\u265B"
            elif letter == 'r':
                return "\u265C"
            elif letter == 'b':
                return "\u265D"
            elif letter == 'n':
                return "\u265E"
            elif letter == 'p':
                return "\u265F"

    def move(self, new_row: int, new_column: int, pieces: list) -> bool:
        """
        | Check if the move is in the list of valid moves and does the move.
        | Returns True if the move was done, False if it wasn't. 
        """
        
        self.valid_moves = self.get_valid_moves(pieces)
        for move in self.valid_moves:
            if move == (new_row, new_column):
                self.row = new_row
                self.column = new_column
                return True
        else:
            return False

    def get_valid_moves(self, pieces: list) -> list:
        """
        | Get valid positions in a list.
        """
        
        moves = []
        for i in range(1,9):
            for j in range(1,9): 
                if not self.free_position(i, j, pieces):
                    continue
                elif self.is_valid(i, j):
                    moves.append((i, j))
                elif self.symbol == "\u2659" or self.symbol == "\u265F":
                    # If its a pawn and there is a piece in the diagonal it can
                    # be eaten.
                    if self.eat_diagonal(i, j, pieces):
                        moves.append((i, j))
                elif self.symbol == "\u2654" or self.symbol == "\u265A":
                    # If its a king and the way to the rook is clear it can castle.
                    if self.can_castle(i, j, pieces):
                        moves.append((i, j))
        return moves

    def free_position(self, new_row: int, new_column: int, pieces: list) -> bool:
        """
        | Check if there is a piece of your team in that position.
        | False if there is a piece in that position, True if there isn't
        """

        for p in pieces:
            if p.row == new_row and p.column == new_column and p.color == self.color:
                return False
            else:
                continue
        else:
            return True

    def check_eat(self, new_row: int, new_column: int, pieces: list) -> None:
        """
        | Pop out the eaten piece if there is one.
        """

        for p in pieces:
            if p.row == new_row and p.column == new_column and p.color != self.color:
                pieces.remove(p)
                break