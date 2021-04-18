from piece_array import get_pieces
from board import Board

# Initialize.
pieces = get_pieces()
board = Board()

# Game variables.
counter = 0

def play(player: str) -> int:
    """
    | Get piece to move, get the new move check if its possible, if a piece is
    | eaten and finally returns 1 if the move was completed, returns 0 if the
    | move wasn't possible.
    """
    
    piece_pos = input(f"{player}'s turn, input the position of the piece you want to move: ")
    row = int(piece_pos[1])
    column = ord(piece_pos[0]) - 96
    
    for p in pieces:
        if p.row == row and p.column == column and p.color == player[0].lower():
            new_move = input("Input the new position: ")
            new_row = int(new_move[1])
            new_column = ord(new_move[0]) - 96
            
            if p.move(new_row, new_column, pieces):
                p.check_eat(new_row, new_column, pieces)
                return 1
    else:
        print(f"That's not a {player.lower()} piece or valid move.")
        return 0

while True:
    board.set_pieces(pieces)
    board.print_board()
    
    if counter % 2 == 0:
        counter += play("White")
    else:
        counter += play("Black")