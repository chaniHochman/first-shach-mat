class Queen(Piece):

    @property
    def symbol(self):
        return "Q"

    def can_move(self, board, frm, to):
        ...