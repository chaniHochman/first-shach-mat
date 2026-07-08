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

    def is_white(self):
        return self.color == "w"

    def is_black(self):
        return self.color == "b"

    def same_color(self, other):
        return other is not None and self.color == other.color
    
    def enemy(self, other):
        return other is not None and other.color != self.color

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