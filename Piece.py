from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color):
        self.color = color

    @property
    @abstractmethod
    def symbol(self):
        pass

    @abstractmethod
    def can_move(self, board, move_from, move_to):
        pass

    @abstractmethod
    def path_is_clear(self, board, move_from, move_to):
        pass

    @staticmethod
    def color_of(piece):
        if piece is None or piece == ".":
            return None
        if hasattr(piece, "color"):
            return piece.color
        if isinstance(piece, str) and len(piece) > 0:
            return piece[0]
        return None

    def is_white(self):
        return self.color == "w"

    def is_black(self):
        return self.color_of(self) == "b"

    def same_color(self, other):
        return self.color_of(self) == self.color_of(other)
    
    def enemy(self, other):
        return self.color_of(other) is not None and self.color_of(self) != self.color_of(other)

    def to_string(self):
        return self.color + self.symbol


#     #בדיקה אם הם באותו צבע    
# def if_same_color(move_from,move_to,board):
#     piece_from = board[move_from[0]][move_from[1]]
#     piece_to = board[move_to[0]][move_to[1]]
#     if piece_to == ".":
#         return True
#     if piece_to[0]==piece_from[0]:#אם הם באותו צבע
#         return False
#     return True