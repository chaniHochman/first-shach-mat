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

    def enemy(self, other):
        return other is not None and other.color != self.color
