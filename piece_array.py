from Pieces.piece import Piece
from Pieces.pawn import Pawn
from Pieces.rook import Rook
from Pieces.bishop import Bishop
from Pieces.knight import Knight
from Pieces.queen import Queen
from Pieces.king import King

def get_pieces() -> list:
    pieces = []

    # White team.
    pieces.append(Rook("White", 8, 'a', 'r'))
    pieces.append(Knight("White", 8, 'b', 'n'))
    pieces.append(Bishop("White", 8, 'c', 'b'))
    pieces.append(Queen("White", 8, 'd', 'q'))
    pieces.append(King("White", 8, 'e', 'k'))
    pieces.append(Bishop("White", 8, 'f', 'b'))
    pieces.append(Knight("White", 8, 'g', 'n'))
    pieces.append(Rook("White", 8, 'h', 'r'))

    pieces.append(Pawn("White", 7, 'a', 'p'))
    pieces.append(Pawn("White", 7, 'b', 'p'))
    pieces.append(Pawn("White", 7, 'c', 'p'))
    pieces.append(Pawn("White", 7, 'd', 'p'))
    pieces.append(Pawn("White", 7, 'e', 'p'))
    pieces.append(Pawn("White", 7, 'f', 'p'))
    pieces.append(Pawn("White", 7, 'g', 'p'))
    pieces.append(Pawn("White", 7, 'h', 'p'))

    # Black team.
    pieces.append(Pawn("Black", 2, 'a', 'p'))
    pieces.append(Pawn("Black", 2, 'b', 'p'))
    pieces.append(Pawn("Black", 2, 'c', 'p'))
    pieces.append(Pawn("Black", 2, 'd', 'p'))
    pieces.append(Pawn("Black", 2, 'e', 'p'))
    pieces.append(Pawn("Black", 2, 'f', 'p'))
    pieces.append(Pawn("Black", 2, 'g', 'p'))
    pieces.append(Pawn("Black", 2, 'h', 'p'))

    pieces.append(Rook("Black", 1, 'a', 'r'))
    pieces.append(Knight("Black", 1, 'b', 'n'))
    pieces.append(Bishop("Black", 1, 'c', 'b'))
    pieces.append(Queen("Black", 1, 'd', 'q'))
    pieces.append(King("Black", 1, 'e', 'k'))
    pieces.append(Bishop("Black", 1, 'f', 'b'))
    pieces.append(Knight("Black", 1, 'g', 'n'))
    pieces.append(Rook("Black", 1, 'h', 'r'))

    return pieces