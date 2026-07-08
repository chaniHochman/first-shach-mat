class Pawn(Piece):

    @property
    def symbol(self):
        return "P"

    def can_move(self, board, frm, to):
        ...