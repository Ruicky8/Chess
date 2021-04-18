class Board():
    """
    | A class for the board.
    """

    def __init__(self):
        """
        | Creates a board filled with dots and adds column letters and row
        | numbers.
        """

        self.board = [['.' for i in range(9)] for j in range(9)]
        self.board[0][0] = ' '
        for i in range(1, 9):
            self.board[0][i] = chr(i + 96)
        for i in range(1, 9):
            self.board[i][0] = i

    def set_pieces(self, pieces) -> None:
        """
        | Set pieces in the board to display the board later.
        """
        
        for i in range(1, 9):
            for j in range(1, 9):
                self.board[i][j] = '.'
        for p in pieces:
            self.board[p.row][p.column] = p.symbol

    def print_board(self):
        for x in self.board:
            for y in x:
                print(y, end=" ")
            print("") 

